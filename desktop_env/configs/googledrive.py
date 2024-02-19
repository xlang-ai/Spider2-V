#coding=utf8
import tempfile, requests, logging, time, json
from typing import List
from playwright.sync_api import sync_playwright, TimeoutError
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive, GoogleDriveFile, GoogleDriveFileList


logger = logging.getLogger("desktopenv.setup")


def googledrive_init_setup(controller, **config):
    """ Clean google drive space (eliminate the impact of previous experiments to reset the environment)
    @args:
        config(Dict[str, Any]): contain keys
            settings_file(str): path to google drive settings file, which will be loaded by pydrive.auth.GoogleAuth()
            operation(List[str]): each operation is chosen from ['delete', 'upload']
            args(List[Dict[str, Any]]): parameters for each operation
        different args dict for different operations:
            for delete:
                query(str): query pattern string to search files or folder in google drive to delete, please refer to
                    https://developers.google.com/drive/api/guides/search-files?hl=en about how to write query string.
                trash(bool): whether to delete files permanently or move to trash. By default, trash=false, completely delete it.
            for upload:
                path(str): remote url to download file
                dest(List[str]): the path in the google drive to store the downloaded file
    """
    settings_file = config.get('settings_file', 'evaluation_examples/settings/googledrive/settings.yml')
    gauth = GoogleAuth(settings_file=settings_file)
    drive = GoogleDrive(gauth)

    def mkdir_in_googledrive(paths: List[str]):
        paths = [paths] if type(paths) != list else paths
        parent_id = 'root'
        for p in paths:
            q = f'"{parent_id}" in parents and title = "{p}" and mimeType = "application/vnd.google-apps.folder" and trashed = false'
            folder = drive.ListFile({'q': q}).GetList()
            if len(folder) == 0:  # not exists, create it
                parents = {} if parent_id == 'root' else {'parents': [{'id': parent_id}]}
                file = drive.CreateFile({'title': p, 'mimeType': 'application/vnd.google-apps.folder', **parents})
                file.Upload()
                parent_id = file['id']
            else:
                parent_id = folder[0]['id']
        return parent_id

    for oid, operation in enumerate(config['operation']):
        if operation == 'delete':  # delete a specific file
            # query pattern string, by default, remove all files/folders not in the trash to the trash
            params = config['args'][oid]
            q = params.get('query', '')
            trash = params.get('trash', False)
            q_file = f"( {q} ) and mimeType != 'application/vnd.google-apps.folder'" if q.strip() else "mimeType != 'application/vnd.google-apps.folder'"
            filelist: GoogleDriveFileList = drive.ListFile({'q': q_file}).GetList()
            q_folder = f"( {q} ) and mimeType = 'application/vnd.google-apps.folder'" if q.strip() else "mimeType = 'application/vnd.google-apps.folder'"
            folderlist: GoogleDriveFileList = drive.ListFile({'q': q_folder}).GetList()
            for file in filelist:  # first delete file, then folder
                file: GoogleDriveFile
                if trash:
                    file.Trash()
                else:
                    file.Delete()
            for folder in folderlist:
                folder: GoogleDriveFile
                # note that, if a folder is trashed/deleted, all files and folders in it will be trashed/deleted
                if trash:
                    folder.Trash()
                else:
                    folder.Delete()
        elif operation == 'mkdirs':
            params = config['args'][oid]
            mkdir_in_googledrive(params['path'])
        elif operation == 'upload':
            params = config['args'][oid]
            url = params['url']
            with tempfile.NamedTemporaryFile(mode='wb', delete=False) as tmpf:
                response = requests.get(url, stream=True)
                response.raise_for_status()
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        tmpf.write(chunk)
                tmpf.close()
                paths = [params['path']] if params['path'] != list else params['path']
                parent_id = mkdir_in_googledrive(paths[:-1])
                parents = {} if parent_id == 'root' else {'parents': [{'id': parent_id}]}
                file = drive.CreateFile({'title': paths[-1], **parents})
                file.SetContentFile(tmpf.name)
                file.Upload()
            return
        else:
            raise ValueError('[ERROR]: not implemented clean type!')


def googledrive_login_setup(controller, **config):
    """ Login to a website with account and password information.
    @args:
        config(Dict[str, Any]): contain keys
            settings_file(str): path to the settings file
    """
    host = controller.vm_ip
    port = 9222  # fixme: this port is hard-coded, need to be changed from config file
    remote_debugging_url = f"http://{host}:{port}"

    with sync_playwright() as p:
        browser = None
        for attempt in range(15):
            try:
                browser = p.chromium.connect_over_cdp(remote_debugging_url)
                break
            except Exception as e:
                if attempt < 14:
                    logger.error(f"Attempt {attempt + 1}: Failed to connect, retrying. Error: {e}")
                    time.sleep(1)
                else:
                    logger.error(f"Failed to connect after multiple attempts: {e}")
                    raise e
        if not browser:
            return

        context = browser.contexts[0]

        url = 'https://drive.google.com/drive/my-drive'
        page = context.new_page()  # Create a new page (tab) within the existing context
        page.goto(url)
        logger.info(f"Opened new page: {url}")
        settings = json.load(open(config['settings_file']))
        email, password = settings['email'], settings['password']

        try:
            page.wait_for_selector('input[type="email"]', state="visible", timeout=3000)
            page.fill('input[type="email"]', email)
            page.click('#identifierNext > div > button')
            page.wait_for_selector('input[type="password"]', state="visible", timeout=5000)
            page.fill('input[type="password"]', password)
            page.click('#passwordNext > div > button')
            page.wait_for_load_state('load', timeout=5000)
        except TimeoutError:
            logger.info('[ERROR]: timeout when waiting for google drive login page to load!')
            return

        return browser, context