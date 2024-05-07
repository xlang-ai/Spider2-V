#coding=utf8
import logging, time, json, re, os, random, platform, requests
from typing import List, Union
from playwright.sync_api import sync_playwright, expect, TimeoutError
from .general import (
    get_browser,
    copyfile_from_guest_to_host_setup,
    copyfile_from_host_to_guest_setup,
    get_element_desktop_position,
    simulate_human_click,
    expand_toggle_button
)

logger = logging.getLogger("desktopenv.setup")


def google_account_login_in(page, email, password, timeout=60000):
    try:
        email_box = page.locator('input[type="email"]')
        expect(email_box).to_be_editable(timeout=timeout)
        email_box.fill(email)
        next_button = page.locator('#identifierNext > div > button')
        expect(next_button).to_be_enabled()
        next_button.click()

        password_box = page.locator('input[type="password"]')
        expect(password_box).to_be_editable(timeout=timeout)
        password_box.fill(password)
        next_button = page.locator('#passwordNext > div > button')
        expect(next_button).to_be_enabled()
        next_button.click()

        page.wait_for_load_state('load')
    except TimeoutError:
        logger.info('[WARNING]: timeout when trying to login in Google Account, probably network problem or already logined in!')
    except Exception as e:
        logger.info('[ERROR]: unexpected error when trying to login in Google Account!')
    return


def google_account_login_in_alert(page):
    try:
        button = page.locator('button').filter(has_text=re.compile('not now', flags=re.I))
        expect(button).to_be_enabled(timeout=5000) # use short waiting time, because the alert is not always shown
        button.click()
        page.wait_for_load_state('load')
    except:
        # logger.info('[INFO]: Some alert is popped up, just skip!')
        pass
    return


def gcp_first_login_popup_webgui(page):
    """ If it is the first time to login in the GCP, a popup will appear to ask for the agreement of terms of service. This function is to handle the popup and agree to the terms of service.
    """
    try:
        popup = page.locator('mat-dialog-container form div[formgroupname="tosAcceptancesFormGroup"]')
        expect(popup).to_be_visible(timeout=5000) # use short waiting time, because the popup only appears for the first time
        checkbox = popup.locator('mat-checkbox input[type="checkbox"]')
        expect(checkbox).to_be_visible()
        checkbox.check()
        agree_button = page.locator('mat-dialog-actions button').filter(has_text=re.compile("Agree and continue"))
        expect(agree_button).to_be_enabled()
        agree_button.click()
        page.wait_for_load_state('load')
    except:
        # logger.info('[INFO]: No first login popup is seen, just skip!')
        pass
    return


def gcp_upload_keyfile_setup(controller, **config):
    """ Upload the GCP keyfile to the guest machine. The keyfile is used to authenticate the GCP account. The keyfile is usually a json file and can be downloaded from the GCP console.
    @args:
        config_file(str): the path to the GCP keyfile, default is 'evaluation_examples/settings/google/gcp_config.json'
        project_name(str): the GCP name to search in the config file, if not provided, use project_index to get the project
        project_index(int): the index of the project in the config file, default is 0
        dest(str): the path to save the keyfile on the guest machine, default is '/home/user/gcp_keyfile.json'
    """
    config_file = config.get('config_file', 'evaluation_examples/settings/google/gcp_config.json')
    if platform.system() == 'Windows':
        config_file = config_file.replace('/', '\\')
    gcp_config = json.load(open(config_file, 'r'))
    if 'project_name' in config:
        prj_name = config['project_name']
        for proj in gcp_config:
            if prj_name == proj['project_name']:
                gcp_config = proj
                break
        else:
            raise ValueError(f'[ERROR]: The specified project name {prj_name} is not found in the GCP config file!')
    else:
        assert 'project_index' in config, "Must specify either project_name or project_index in config!"
        gcp_config = gcp_config[config['project_index']]
    keyfile = gcp_config['keyfile_path']
    dest = config.get('dest', '/home/user/gcp_keyfile.json')
    copyfile_from_host_to_guest_setup(controller, keyfile, dest)
    return


def gcp_delete_via_webgui(page, **config):
    """ Given the project name or id, delete the project, note that the deletion is not immediate and can be restored within 30 days. Sadly, the deleted project still occupies the quota regarding the number of projects. If the target project is not found, return None; If multiple projects found, return the 1st project id according to the last accessed time (sorted by default on web).
    """
    page.goto("https://console.cloud.google.com/cloud-resource-manager")
    page.wait_for_load_state('load')

    prj_name, prj_id = config.get('project_name', None), config.get("project_id", None)
    assert prj_name is not None or prj_id is not None, "At least provide project name or id for GCP deletion"
    def compare_function(name, id):
        if prj_name and name != prj_name:
            return False
        if prj_id and id != prj_id:
            return False
        return True

    # firstly, check whether the toggle node is expanded, if not, click it to expand all GCPs
    button = page.locator("button[aria-label='Toggle node']")
    try:
        expect(button).to_be_visible()
    except:
        logger.info('[INFO]: The toggle button is not found, probably no GCP is found currently!')
        return
    expand_toggle_button(button, 'aria-expanded', 'true')

    # second, iterate through the list of projects and delete them according to project name
    table = page.locator('table')
    expect(table).to_have_attribute("aria-busy", "false")
    rows = table.locator('tbody tr')

    def duplication_check(entries):
        count = 0
        for row in entries:
            project_name = row.evaluate('el => el.children[1].innerText').strip()
            project_id = row.evaluate('el => el.children[2].innerText').strip()
            if project_id == "": continue # No organization, not a GCP
            if compare_function(project_name, project_id): count += 1
        if count > 1: return True
        return False

    if duplication_check(rows.all()):
        logger.warning("[WARNING]: Multiple projects with the same name found, only the first one is deleted!")

    for row in rows.all():
        project_name = row.evaluate('el => el.children[1].innerText').strip()
        project_id = row.evaluate('el => el.children[2].innerText').strip()
        if project_id == "": continue # No organization, not a GCP

        if compare_function(project_name, project_id):
            checkbox = row.locator('[role="checkbox"]')
            checkbox.check()

            delete_button = page.locator('#resource-manager-action-bar-delete-button')
            expect(delete_button).to_be_enabled()
            delete_button.click()
            cfc_loader = page.locator('mat-dialog-container >> cfc-loader')
            expect(cfc_loader).to_have_class(re.compile(r"cfc-loader-resolved"))

            popup = page.locator('mat-dialog-container[role="dialog"]')
            input_box = popup.locator('input[aria-required="true"]')
            input_box.fill(project_id)

            button = popup.locator('button[aria-label="Shut down anyway" i]')
            expect(button).to_be_enabled()
            button.click()

            popup = page.locator('mat-dialog-container[role="dialog"] #project-deletion-dialog-content')
            expect(popup).to_be_visible(timeout=30000) # maybe very slow just wait
            page.locator('mat-dialog-container[role="dialog"] button').click()

            entry = page.locator('table tbody tr td').filter(has_text=re.compile(project_id))
            expect(entry).to_have_count(0, timeout=30000)
            logger.info(f'Deleting GCP: project_name={project_name}, project_id={project_id}')
            return project_id
    logger.error(f'[ERROR]: The project(name={"?" if project_name is None else project_name}, id={"?" if project_id is None else project_id}) to delete not found, no action is taken!')
    return


def gcp_rename_via_webgui(page, **config):
    """ Rename a existing google cloud project via web GUI. Note that the project id and project number is unique and cannot be altered once created. And the old project must exist before renaming. The new name should not conflict with other existing project names (This check can be relaxed by setting argument `allow_conflict=True`).
    @args:
        project_id(str): the project id, if unknown, use gcp_info_via_webgui to get it from project name
        project_name(str): the project name, easier to remember than project id
        new_name(str): the new name of the project, required
        allow_conflict(bool): check project name conflict before renaming, default is False
    @return:
        None if project not found, otherwise return the id of the renamed project or existing project with the new name
    """
    page.goto("https://console.cloud.google.com/cloud-resource-manager")
    page.wait_for_load_state('load')

    button = page.locator("button[aria-label='Toggle node']")
    try:
        expect(button).to_be_visible()
    except:
        logger.info('[INFO]: The toggle button is not found, probably no GCP is found currently!')
        return
    expand_toggle_button(button, 'aria-expanded', 'true')

    table = page.locator('table')
    expect(table).to_have_attribute("aria-busy", "false")
    rows = table.locator('tbody tr')

    new_name = config['new_name']
    allow_conflict = config.get('allow_conflict', False)
    if not allow_conflict:
        for row in rows.all():
            project_name = row.evaluate('el => el.children[1].innerText').strip()
            project_id = row.evaluate('el => el.children[2].innerText').strip()
            if project_name == new_name:
                logger.warning(f'[WARNING]: The new project name {new_name} already exists in project id {project_id}, GCP rename aborted to avoid conflict!')
                return project_id

    prj_name, prj_id = config.get('project_name', None), config.get("project_id", None)
    assert prj_name is not None or prj_id is not None, "At least provide old project name or project id"

    def compare_function(name, id):
        if prj_name and name != prj_name:
            return False
        if prj_id and id != prj_id:
            return False
        return True

    def duplication_check(entries):
        count = 0
        for row in entries:
            project_name = row.evaluate('el => el.children[1].innerText').strip()
            project_id = row.evaluate('el => el.children[2].innerText').strip()
            if project_id == "": continue # No organization, not a GCP
            if compare_function(project_name, project_id): count += 1
        if count > 1: return True
        return False

    if duplication_check(rows.all()):
        logger.info('[WARNING]: Multiple projects with the same old name found, only the first one is renamed!')

    for row in rows.all():
        project_name = row.evaluate('el => el.children[1].innerText').strip()
        project_id = row.evaluate('el => el.children[2].innerText').strip()
        if project_id == "": continue # No organization, not a GCP

        if compare_function(project_name, project_id):
            action_button = row.locator('button[aria-label="Actions menu" i]')
            action_button.click()
            expect(action_button).to_have_attribute("aria-expanded", "true")
            page.locator('cfc-menu-section cfc-menu-item[label="Settings"] a').click()
            input_box = page.locator('input#resourceName')
            expect(input_box).to_be_editable()
            input_box.fill(new_name)
            button = page.locator('button#renameResource')
            expect(button).to_be_enabled() # changed to a new project name, button is activated
            button.click()
            expect(button).to_be_disabled() # waiting for the response
            logger.info(f'Renaming GCP: project_id={project_id}, old_name={project_name}, new_name={new_name}')
            return project_id

    logger.error(f'[ERROR]: The project(name={"?" if project_name is None else project_name}, id={"?" if project_id is None else project_id}) to rename not found, no action is taken!')
    return


def gcp_create_via_webgui(page, **config):
    """ Create a new GCP via web GUI according to the specified `project_name` and return the project id. If the GCP with the target name already exists, do nothing and return the project id (This check can be relaxed by setting `allow_duplicate=True`). Note that, `project_id` is unique and can not be duplicated.
    @args:
        project_name(str): optional, the name of the new project (better specified), if not provided, the name will be generated by Google Cloud automatically (not recommended)
        project_id(str): optional, the unique id of the new project (better not specified directly), if not provided, the id will be generated by Google Cloud (recommended)
        allow_duplicate(bool): check project name conflict before creating, default is False
    @return:
        id of the created project, or existing project with the same name
    """
    page.goto("https://console.cloud.google.com/cloud-resource-manager")
    page.wait_for_load_state('load')

    prj_name, prj_id = config.get('project_name', None), config.get('project_id', None)
    allow_duplicate = config.get('allow_duplicate', False)
    if prj_name is not None and not allow_duplicate:
        button = page.locator("button[aria-label='Toggle node']")
        try:
            expect(button).to_be_visible()
        except:
            logger.info('[INFO]: The toggle button is not found, probably no GCP is found currently!')
            allow_duplicate = True
        if not allow_duplicate:
            expand_toggle_button(button, 'aria-expanded', 'true')
            table = page.locator('table')
            expect(table).to_have_attribute("aria-busy", "false")
            rows = table.locator('tbody tr') # only one table body
            for row in rows.all():
                project_name = row.evaluate('el => el.children[1].innerText').strip()
                if project_name == prj_name:
                    project_id = row.evaluate('el => el.children[2].innerText').strip()
                    logger.warning(f'[WARNING]: GCP (id={project_id}) with name {project_name} already exists, no need to create a new one')
                    return project_id

    create_button = page.locator("button#create-project-button")
    expect(create_button).to_be_enabled()
    create_button.click()

    try:
        quota_button = page.locator('a#p6ntest-quota-submit-button')
        expect(quota_button).to_be_visible(timeout=5000)
        logger.error('[ERROR]: Quota button is seen, GCP creation is not permitted due to quota limitation!')
        return
    except Exception as e:
        logger.info(f'[INFO]: Quota button is not invoked, GCP creation is permitted!')
        pass

    input_box = page.locator('input#p6ntest-name-input')
    expect(input_box).to_be_editable()
    if prj_name is not None:
        match_obj = re.match(r"^[a-z\d'\- !]{4,30}$", prj_name, flags=re.I)
        if not match_obj:
            logger.error(f'[ERROR]: The specified project name {prj_name} is invalid, GCP creation failed!')
            return
        input_box.fill(prj_name)
    else:
        prj_name = input_box.input_value().strip()

    def get_default_project_id():
        refresh_button = page.locator('button#p6ntest-refresh-id')
        if refresh_button.count() > 0: # click the refresh button to generate one default valid project id
            expect(refresh_button).to_be_enabled()
            refresh_button.click()
            input_box = page.locator('input#p6ntest-id-input')
            expect(input_box).to_have_attribute('aria-invalid', 'false')
            project_id = input_box.input_value().strip()
            return project_id
        else:
            text_string = page.locator('proj-name-id-input mat-hint').inner_text()
            matched = re.search(r'Project ID: (.*?)\. It cannot be changed later', text_string)
            if not matched:
                logger.error(f'[ERROR]: The default project id is not found, GCP creation failed!')
                return
            project_id = matched.group(1)
            return project_id

    if prj_id is None: # extract and use the default project id
        prj_id = get_default_project_id()
    else:
        edit_button = page.locator('button#p6ntest-show-edit-proj-id')
        edit_button.click()
        input_box = page.locator('input#p6ntest-id-input')
        expect(input_box).to_be_editable()
        input_box.fill(prj_id)
        if input_box.get_attribute("aria-invalid") == "true":
            logger.error(f'[ERROR]: The specified project id {prj_id} is invalid, use the default project id!')
            prj_id = get_default_project_id()
    # leave the organization as default, that is `No organization`

    button = page.locator('button[type="submit"]')
    expect(button).to_be_enabled()
    button.click()
    page.wait_for_load_state('load')

    # the newly created project should be visible after refreshing the page
    new_entry_name = page.locator('tbody tr td').filter(has_text=re.compile(prj_name)).first
    new_entry_id = page.locator('tbody tr td').filter(has_text=re.compile(prj_id))
    expect(new_entry_name.or_(new_entry_id)).to_be_visible(timeout=30000) # maybe very slow, just wait
    logger.info(f'Creating GCP: project_name={prj_name}, project_id={prj_id}')
    return prj_id


def gcp_restore_via_webgui(page, **config):
    """ Restore the GCP from the pending deletion list via web GUI. If the target project is not found, return None; If multiple projects match the condition, restore all of them; If no project is specified, restore all deleted projects.
    @args:
        project_name(str): optional, the name of the project to restore, if multiple projects match the condition, restore all of them
        project_id(str): optional, the id of the project to restore
        if both are not provided, restore all deleted projects
    @return:
        None: no project is restored (either not found or the pending deletion list is empty)
        prjs_list(List[str]): restored project_id list
    """
    page.goto("https://console.cloud.google.com/cloud-resource-manager")
    restore_button = page.locator('#pending-deletion-button')
    expect(restore_button).to_be_enabled()
    restore_button.click()
    page.wait_for_load_state('networkidle')

    prj_name, prj_id = config.get('project_name', None), config.get("project_id", None)
    if prj_name is None and prj_id is None:
        logger.warning('[WARNING]: No project is specified, will restore all pending deletion GCPs!')
    table = page.locator('table')
    expect(table).to_have_attribute("aria-label", "Resources pending deletion table")
    expect(table).to_have_attribute("aria-busy", "false")
    rows = table.locator('tbody tr')

    def compare_function(name, id):
        if prj_name and name != prj_name:
            return False
        if prj_id and not id.endswith(prj_id): # id may have prefix projects/
            return False
        return True

    prjs_to_restore = []
    for row in rows.all():
        project_name = row.evaluate('el => el.children[1].innerText').strip()
        project_id = row.evaluate('el => el.children[2].innerText').strip()
        if compare_function(project_name, project_id):
            checkbox = row.locator('[role="checkbox"]')
            checkbox.check()
            prjs_to_restore.append((project_name, project_id))

    if len(prjs_to_restore) == 0:
        logger.warning(f'[WARNING]: GCP (project_name={"?" if prj_name is None else prj_name}, project_id={"?" if prj_id is None else prj_id}) not found in the pending deletion list, no action is taken!')
        return

    button = page.locator('button#restore-button')
    expect(button).to_be_enabled()
    button.click()

    confirm_button = page.locator('mat-dialog-container[role="dialog"] button').filter(has_text="Restore")
    expect(confirm_button).to_be_enabled()
    confirm_button.click()
    timeout = len(prjs_to_restore) * 5000
    for project_name, project_id in prjs_to_restore:
        column = page.locator('tbody tr td').filter(has_text=re.compile(project_id))
        expect(column).to_have_count(0, timeout=timeout) # waiting for the response
        logger.info(f'Restoring GCP: project_name={project_name}, project_id={project_id}')
    prj_ids = list(map(lambda x: x[1], prjs_to_restore))
    if len(prj_ids) == 1: return prj_ids[0]
    return prj_ids


def gcp_info_via_webgui(page, **config):
    """ Given the project name or id, return the project metainfo, including 1) project id, 2) project name, 3) project number, etc. By default, the google account is logined in (in web browser cache).
    If the target project is not found, return None;
    If multiple projects found, return the 1st according to the last accessed time (sorted by default on web).
    """
    page.goto("https://console.cloud.google.com/cloud-resource-manager")
    button = page.locator("button[aria-label='Toggle node']")
    try:
        expect(button).to_be_visible()
    except:
        logger.info('[INFO]: The toggle button is not found, probably no GCP is found currently!')
        return
    expand_toggle_button(button, 'aria-expanded', 'true')

    table = page.locator('table')
    expect(table).to_have_attribute("aria-busy", "false")
    rows = table.locator('tbody tr')
    
    prj_name, prj_id = config.get('project_name', None), config.get("project_id", None)
    assert prj_name is not None or prj_id is not None, "At least provide project name or project id"

    def compare_function(name, id):
        if prj_name and name != prj_name:
            return False
        if prj_id and id != prj_id:
            return False
        return True

    def duplication_check(entries):
        count = 0
        for row in entries:
            project_name = row.evaluate('el => el.children[1].innerText').strip()
            project_id = row.evaluate('el => el.children[2].innerText').strip()
            if project_id == "": continue # No organization, not a GCP
            if compare_function(project_name, project_id): count += 1
        if count > 1: return True
        return False

    if duplication_check(rows.all()):
        logger.warning("[WARNING]: Multiple projects with the same name found, infos of the first one is retrieved!")

    output = {"project_name": "", "project_id": "", "project_number": ""}
    for row in rows.all():
        project_name = row.evaluate('el => el.children[1].innerText').strip()
        project_id = row.evaluate('el => el.children[2].innerText').strip()
        if project_id == "": continue # No organization, not a GCP

        if compare_function(project_name, project_id):
            output["project_name"], output["project_id"] = project_name, project_id
            action_button = row.locator('button[aria-label="Actions menu" i]')
            action_button.click()
            expect(action_button).to_have_attribute("aria-expanded", "true")
            page.locator('cfc-menu-section cfc-menu-item[label="Settings"] a').click()
            project_number = page.locator('form > mat-form-field').filter(has_text="Project number:").locator('input[name="resourceId" i][readonly="true"]')
            expect(project_number).to_be_visible()
            output['project_number'] = project_number.input_value()
            logger.info('Get GCP info: project_name=%s, project_id=%s, project_number=%s' % (project_name, project_id, output['project_number']))
            return output
    logger.error(f'[ERROR]: GCP (project_name={"?" if project_name is None else project_name}, project_id={"?" if project_id is None else project_id}) not found, no information is retrieved!')
    return


def gcp_api_via_webgui(page, **config):
    """ Enable or disable the GCP API via web GUI. By default, the google account is logined in.
    @args:
        project_id(str): the project id, if unknown, use gcp_info_via_webgui to get it from project name
        project_name(str): the project name, easier to remember than project id
        apis(List[str]): the products/APIs to manipulate (insert into the url template below), default is ['serviceusage', 'servicemanagement', 'cloudresourcemanager', 'bigquery', 'cloudapis'],
            f'https://console.cloud.google.com/apis/library/{api_name}.googleapis.com?project={project_id}'
        enable(bool): enable the API or disable the API, default is True, enable the API
    """
    if 'project_id' not in config:
        assert 'project_name' in config, "At least provide project name to enable/disable Google API Services."
        infos = gcp_info_via_webgui(page, **config)
        if infos is None:
            logger.error(f'[ERROR]: GCP (project_name={config["project_name"]}) not found, unable to manipulate Google API services!')
            return
        config['project_id'] = infos['project_id']

    project_id = config['project_id']
    apis = config.get('apis', ['serviceusage', 'servicemanagement', 'cloudresourcemanager', 'bigquery', 'cloudapis'])
    enable = config.get('enable', True) # two choices: enable or disable

    def confirm_disable_popups(page):
        try:
            button = page.locator('mat-dialog-container[role="alertdialog"] button').filter(has_text=re.compile(r'disable', flags=re.I))
            expect(button).to_be_visible(timeout=5000)
            button.click()
        except: pass
        try:
            button = page.locator('mat-dialog-container[role="alertdialog"] button').filter(has_text=re.compile(r'confirm', flags=re.I))
            expect(button).to_be_visible(timeout=5000)
            button.click()
        except: pass
        return

    def enable_or_disable_one_api(page, product, project_id):
        url_template = f'https://console.cloud.google.com/apis/library/{product}.googleapis.com?project={project_id}'
        page.goto(url_template)
        page.wait_for_load_state('load')
        enable_button = page.locator('button[aria-label="enable this API" i]')
        manage_button = page.locator('button[aria-label="manage this API" i]')
        expect(enable_button.last.or_(manage_button.last)).to_be_visible()

        if enable:
            if enable_button.count() == 0: # the API is already enabled
                assert manage_button.count() > 0
                logger.info(f'Google API Service {product} has been enabled for GCP: project_id={project_id}')
                return project_id

            enable_button.last.click()
            disable_button = page.locator('button[aria-label="Disable API" i]')
            expect(disable_button).to_be_visible(timeout=300000) # waiting for the web response, may take longer time
            logger.info(f'Google API Service {product} is enabled for GCP: project_id={project_id}')
        else: # disable the API
            if manage_button.count() == 0: # the API is not enabled yet, do nothing
                assert enable_button.count() > 0
                logger.info(f'Google API Service {product} is not enabled for GCP: project_id={project_id}')
                return project_id

            manage_button.last.click()
            disable_button = page.locator('button[aria-label="Disable API" i]')
            expect(disable_button).to_be_visible()
            disable_button.click()
            confirm_disable_popups(page)
            enable_button = page.locator('button[aria-label="enable this API" i]').last
            expect(enable_button).to_be_visible(timeout=300000)
            logger.info(f'Google API Service {product} is disabled for GCP: project_id={project_id}')
        return

    for product in apis:
        enable_or_disable_one_api(page, product, project_id)

    return project_id


def gcp_login_via_webgui(page, **config):
    """ Login to the GCP via web GUI. By default, the google account is logined in.
    @args:
        url(str): the url to open, if not provided, use project_id and product to generate the url
        project_id(str): the project id, if unknown, use gcp_info_via_webgui to get it from project name
        project_name(str): the project name, easier to remember than project id
        product(str): the product to open, default is 'bigquery'
    """
    if 'url' in config:
        page.goto(config['url'])
        page.wait_for_load_state('load')
        return

    if 'project_id' not in config:
        assert 'project_name' in config, "At least provide project name to login in if both url and project_id are not provided."
        infos = gcp_info_via_webgui(page, **config)
        if infos is None:
            logger.error(f'[ERROR]: GCP (project_name={config["project_name"]}) not found, unable to login in to the project related page!')
            return
        config['project_id'] = infos['project_id']

    project_id = config['project_id']
    product = config.get('product', 'bigquery')
    url_template = f'https://console.cloud.google.com/{product}?project={project_id}'
    page.goto(url_template)
    page.wait_for_load_state('load')
    return


def gcp_service_account_via_webgui(page, **config):
    """ Given a GCP, create a new service account and obtain the .json key file via web GUI. By default, each GCP can have at most 100 service accounts.
    @args:
        project_id(str): the project id, if unknown, use gcp_info_via_webgui to get it from project name
        project_name(str): the project name, easier to remember than project id
        email(str): google account email to access the service account, default is the current logined in account
        role(str): the role of the service account, default is 'Owner'
    @return:
        x, y: the position of the download button, used to simulate the click action
    """
    if 'project_id' not in config:
        assert 'project_name' in config, "At least provide project name to create a service account and the keyfile."
        infos = gcp_info_via_webgui(page, **config)
        if infos is None:
            logger.error(f'[ERROR]: GCP (project_name={config["project_name"]}) not found, unable to create a service account!')
            return
        config['project_id'] = infos['project_id']

    project_id = config['project_id']
    page.goto(f"https://console.cloud.google.com/iam-admin/serviceaccounts?project={project_id}")
    page.wait_for_load_state('load')

    create_button = page.locator('button[aria-label="Create service account" i]')
    expect(create_button).to_be_enabled()
    create_button.click()

    # 1. first, create serivice account id (use default generator)
    id_input = page.locator('input[formcontrolname="accountId"][aria-required="true"]')
    expect(id_input).to_be_editable(timeout=20000)
    auto_button = page.locator('button[cfctooltip="Generate ID" i]')
    expect(auto_button).to_be_enabled()
    auto_button.click()
    expect(id_input).to_have_attribute('aria-invalid', 'false')
    account = id_input.input_value() + f'@{project_id}.iam.gserviceaccount.com'
    continue_button = page.locator('button').filter(has_text=re.compile(r'create and continue', flags=re.I))
    expect(continue_button).to_be_enabled()
    continue_button.click()

    # 2. second, assign the role to the service account
    selector = page.locator('cfc-select-dual-column')
    expect(selector).to_be_visible(timeout=20000)
    selector.click()
    filter_input = page.locator('cfc-select-filter input[role="combobox"][aria-expanded="true"]')
    expect(filter_input).to_be_editable()
    role = config.get("role", "Owner")
    filter_input.fill(role)
    first_option = page.locator('div.cfc-select-body > div[role="listbox"] > div.cfc-select-filter-view > mat-option').first
    expect(first_option).to_be_visible()
    first_option.click()
    continue_button = page.locator('button.cfc-stepper-step-continue-button').filter(has_text=re.compile(r'continue', flags=re.I))
    expect(continue_button).to_be_enabled()
    continue_button.click()

    # 3. third, grant users access to this service account    
    input_box = page.locator('cfc-iam-member-bar[formcontrolname="users"] input')
    expect(input_box).to_be_editable(timeout=20000)
    input_box.fill(config['email'])
    
    input_box = page.locator('cfc-iam-member-bar[formcontrolname="admins"] input')
    expect(input_box).to_be_editable()
    input_box.fill(config['email'])

    # 4. third, create the service account
    done_button = page.locator('button[type="submit" i]').filter(has_text=re.compile(r'done', flags=re.I))
    expect(done_button).to_be_enabled()
    done_button.click()

    def search_account_row(page, account):
        table = page.locator('table[aria-busy="false"]')
        expect(table).to_be_visible()
        for row in table.locator('tbody tr').all():
            current_email = row.evaluate('el => el.children[1].innerText').strip()
            if current_email == account:
                return row
        return None
    
    row = search_account_row(page, account)
    if row is None:
        logger.error(f'[ERROR]: The service account {account} is not found, no keyfile is downloaded!')
        return

    action_button = row.locator('button[aria-label="Service account actions menu" i]')
    expect(action_button).to_be_enabled()
    action_button.click()
    key_button = page.locator('cfc-menu-section cfc-menu-item[label="Manage keys" i] a')
    expect(key_button).to_be_visible()
    key_button.click()

    add_button = page.locator('cfc-service-account-key-list > div > button').filter(has_text=re.compile('add key', flags=re.I))
    expect(add_button).to_be_visible()
    add_button.click()
    create_key = page.locator('cfc-menu-section cfc-menu-item[label="Create new key" i] a')
    expect(create_key).to_be_visible()
    create_key.click()
    create_button = page.locator('mat-dialog-container cfc-progress-button button').filter(has_text=re.compile('create', flags=re.I))
    expect(create_button).to_be_visible()

    position = get_element_desktop_position(page, create_button)
    x, y = (position[0][0] + position[1][0]) / 2, (position[0][1] + position[1][1]) / 2
    return {'x': x, 'y': y, 'account': account}


def gcp_config_webgui_setup(controller, **config):
    """ Create a new service account and obtain the .json key file via web GUI.
    @args: for config
        host(str): the host ip address, default to the ip address of the running virtual machine
        port(str): debugging port of web browser, default to 9222
        settings_file(str): .json settings file of the Google Account, containing `email` and `password` fields
        projects([List[Dict[str, Any]]]): project dict to create service accounts, each dict contains 'project_name' and 'role' fields (default to 'Owner')
    """
    host = config.get('host', controller.vm_ip)
    port = config.get('port', 9222)
    remote_debugging_url = f"http://{host}:{port}"
    settings_file = config.get('settings_file', "evaluation_examples/settings/google/settings.json")
    if platform.system() == 'Windows':
        settings_file = settings_file.replace('/', '\\')
    settings = json.load(open(settings_file))
    email, password = settings['email'], settings['password']
    
    def sync_playwright_browser(project):
        with sync_playwright() as p:
            browser = get_browser(p, remote_debugging_url)
            if not browser:
                logger.error(f'[ERROR]: Nothing done. Failed to obtain the browser instance from {remote_debugging_url} .')
                return
            context = browser.contexts[0]
            page = context.new_page()
            page.set_default_timeout(timeout=10000) # defaults to 10s
            page.set_default_navigation_timeout(timeout=100000) # affects the page.goto() method, 100s

            if idx == 0:
                page.goto("https://console.cloud.google.com/cloud-resource-manager")
                google_account_login_in(page, email, password) # needs to login in Google Account for the first time
                google_account_login_in_alert(page)
                gcp_first_login_popup_webgui(page) # handle the first login popup if it appears, o.w. just skip

            # 1. create project if the target project name not exists
            prj_id = gcp_create_via_webgui(page, **project)
            project['project_id'] = prj_id

            # 2. enable some APIs by default
            gcp_api_via_webgui(page, **project)

            # 3. create service account and obtain keyfile
            project['email'], project['role'] = email, project.get('role', 'Owner')
            output = gcp_service_account_via_webgui(page, **project)
            project['service_account'] = output['account']
        return output, project

    for idx, project in enumerate(config.get('projects', [])):
        output, project = sync_playwright_browser(project)
        # we found that in the playwright environment, the click action to download the keyfile will fail
        # leave some time to exit the playwright environment and then simulate the human click action
        time.sleep(3)
        simulate_human_click(controller, (output['x'], output['y']))
        time.sleep(5) # leave some time for downloading
        vm_path = resolve_keyfile_path(controller, output['account'])
        if not vm_path: continue

        local_path = os.path.join(os.path.dirname(settings_file), f'{project["project_id"]}.json')
        copyfile_from_guest_to_host_setup(controller, vm_path, local_path)
        project['keyfile_path'] = local_path

    return config.get('projects', [])


def resolve_keyfile_path(controller, account: str):
    """ Given the service account email, return the path of the keyfile in the virtual machine. By default, the keyfile is saved in the ~/Downloads directory.
    """
    command_list = ["python3", "-c", f"import os, json; keydir = '/home/user/Downloads'; paths = [os.path.join(keydir, f) for f in os.listdir(keydir) if json.load(open(os.path.join(keydir, f)))['client_email'] == '{account}']; print(paths[0])"]
    payload = json.dumps({"command": command_list, "shell": False})
    headers = {
        'Content-Type': 'application/json'
    }

    try:
        http_server = f'http://{controller.vm_ip}:5000'
        response = requests.post(http_server + "/execute", headers=headers, data=payload)
        if response.status_code == 200:
            return response.json()['output'].strip()
    except: pass
    logger.error(f"[ERROR]: Failed to obtain the keyfile path for service account={account}!")
    return


def gcp_webgui_setup(controller, **config):
    """ By default, all Google Cloud Projects (GCPs) belong to the organization 'No organization'. The user needs to provide the Google Account in settings_file (evaluation_examples/settings/google/settings.json).
    @args: for config
        host(str): the host ip address, default to the ip address of the running virtual machine
        port(str): debugging port of web browser, default to 9222
        url(str): goto the url to manage GCPs, usually starts with Google Account login in page,
            default is 'https://console.cloud.google.com/cloud-resource-manager'
        settings_file(str): .json settings file of the Google Account, containing `email` and `password` fields
        consistent(bool): whether use consistent GCP name->id mappings, default is True. This parameter is useful to record and reuse the project name -> project id mappings without invoking gcp_info_via_webgui() repeatedly.
        actions(List[Dict[str, Any]]): a list of actions to perform, each action is a dictionary containing `type` and `parameters` fields, supported action types include: ['delete', 'create', 'login', 'api']
            create: create a new GCP by project name or project id (if already exists, do nothing)
            delete: delete the GCP by project name or project id
            rename: rename the name of a specific GCP
            restore: restore a pending deletion GCP
            api: enable or disable the specific API service for one GCP via web GUI
            login: login to one url using a specific GCP id
    """
    host = config.get('host', controller.vm_ip)
    port = config.get('port', 9222)
    remote_debugging_url = f"http://{host}:{port}"

    with sync_playwright() as p:
        browser = get_browser(p, remote_debugging_url)
        if not browser:
            logger.error(f'[ERROR]: Nothing done. Failed to obtain the browser instance from {remote_debugging_url} .')
            return

        context = browser.contexts[0]
        page = context.new_page()  # Create a new page (tab) within the existing browser context
        page.set_default_timeout(timeout=10000) # defaults to 10s
        page.set_default_navigation_timeout(timeout=100000) # affects the page.goto() method, 100s

        page.goto(config.get('url', "https://console.cloud.google.com/cloud-resource-manager"))
        settings_file = config.pop('settings_file', "evaluation_examples/settings/google/settings.json")
        if platform.system() == 'Windows':
            settings_file = settings_file.replace('/', '\\')
        settings = json.load(open(settings_file))
        email, password = settings['email'], settings['password']
        google_account_login_in(page, email, password) # needs to login in Google Account for the first time
        google_account_login_in_alert(page)
        gcp_first_login_popup_webgui(page) # handle the first login popup if it appears, o.w. just skip

        registered_functions = {
            'info': gcp_info_via_webgui,
            'create': gcp_create_via_webgui,
            'delete': gcp_delete_via_webgui,
            'rename': gcp_rename_via_webgui,
            'restore': gcp_restore_via_webgui,
            'api': gcp_api_via_webgui,
            'login': gcp_login_via_webgui,
        }
        consistent, name2id_mappings = config.get('consistent', True), {}
        for action in config['actions']:
            if consistent and 'project_name' in action['parameters'] and 'project_id' not in action['parameters'] \
                    and action['parameters']['project_name'] in name2id_mappings:
                action['parameters']['project_id'] = name2id_mappings[action['parameters']['project_name']]

            output = registered_functions[action['type']](page, **action['parameters'])

            if consistent and isinstance(output, str):
                if 'new_name' in action['parameters']:
                    name2id_mappings[action['parameters']['new_name']] = output
                elif 'project_name' in action['parameters']:
                    name2id_mappings[action['parameters']['project_name']] = output
            time.sleep(3)

        return browser, context


if __name__ == '__main__':

    from ..controllers.setup import SetupController
    import argparse, sys, subprocess

    parser = argparse.ArgumentParser(description="Google Cloud Project Setup")
    parser.add_argument('-p', '--path', type=str, required=True, help='Path to the virtual machine .vmx file')
    parser.add_argument('-s', '--snapshot', type=str, required=True, help='Name of the snapshot to restore')
    parser.add_argument('-c', '--config', type=str, help='Path to the configuration file to init GCPs')
    args = parser.parse_args(sys.argv[1:])
    stdout_handler = logging.StreamHandler(sys.stdout)
    logger.addHandler(stdout_handler)
    logger.setLevel(logging.INFO)

    p = subprocess.Popen(["vmrun", "-T", "ws", "revertToSnapshot", args.path, args.snapshot])
    p.wait()
    p = subprocess.Popen(["vmrun", "-T", "ws", "start", args.path])
    p.wait()
    vm_ip = subprocess.run(["vmrun", "-T", "ws", "getGuestIPAddress", args.path, "-wait"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=60, text=True, encoding="utf-8").stdout.strip()
    print('VM IP: %s' % vm_ip)

    setup_controller = SetupController(vm_ip=vm_ip, cache_dir='tmp')
    setup_controller._launch_setup(command=["google-chrome", "--remote-debugging-port=1337"])
    setup_controller._launch_setup(command=["socat", "tcp-listen:9222,fork", "tcp:localhost:1337"])
    settings_file = "evaluation_examples/settings/google/settings.json"

    # test each action by modifying the config, this will overwrite the args.config filepath
    # config = {
    #     "consistent": True,
    #     "settings_file": settings_file,
    #     "actions": [
    #         {
    #             "type": "api",
    #             "parameters": {
    #                 "project_name": "My 1st Project",
    #                 "apis": ["bigquery"],
    #                 "enable": True
    #             }
    #         }
    #     ]
    # }
    # gcp_webgui_setup(setup_controller, **config)

    projects = json.load(open(args.config, 'r'))
    config = {"settings_file": settings_file, "projects": projects}
    projects = gcp_config_webgui_setup(setup_controller, **config)
    json.dump(projects, open(args.config, 'w'), indent=4)