#coding=utf8
import os, tempfile, requests, logging, time, json, platform
from typing import List, Dict, Any
from .general import get_browser
from .google_cloud import google_account_login_in
from playwright.sync_api import sync_playwright, expect
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive, GoogleDriveFile, GoogleDriveFileList


logger = logging.getLogger("desktopenv.setup")


def googledrive_delete(drive: GoogleDrive, **config):
    """ Delete files or folders in google drive.
    @config(Dict[str, Any]): contain keys
        path(List[str]): the folder or file path in the google drive to delete, e.g., ['folder1'] and ['folder1', 'file1']. By default, `path=[]`, which means deleting all files and folders in the root directory
        trash(bool): whether to delete files permanently or just move to trash (can be recovered). By default, `trash=false`, delete permanently
    @return: None
    Usage:
        {"type": "delete", "path": [], "trash": False}: delete all files and folders in google drive permanently
        {"type": "delete", "path": ["folder1", "file1"], "trash": True}: move folder1/file1 to trash
        {"type": "delete", "path": ["folder1"], "trash": False}: delete folder1 permanently
    """
    file_path = config.get('path', [])
    file_path = [file_path] if type(file_path) != list else file_path
    trash = config.get('trash', False)

    def delete_files(query: str):
        query_file = query + " and mimeType != 'application/vnd.google-apps.folder'" if query.strip() != '' else "mimeType != 'application/vnd.google-apps.folder'"
        query_folder = query + " and mimeType = 'application/vnd.google-apps.folder'" if query.strip() != '' else "mimeType = 'application/vnd.google-apps.folder'"
        filelist: GoogleDriveFileList = drive.ListFile({'q': query_file}).GetList()
        folderlist: GoogleDriveFileList = drive.ListFile({'q': query_folder}).GetList()
        for file in filelist + folderlist:
            file: GoogleDriveFile
            try: # some files may be shared and cannot be deleted
                if trash:
                    file.Trash()
                else:
                    file.Delete()
            except: pass
        return

    if file_path == []: # special case: delete all files and folders in the root directory
        q_string = 'and trashed = false' if trash else ''
        delete_files(query=q_string)
        return

    parent_id = 'root'
    for idx, p in enumerate(file_path):
        q_string = f'"{parent_id}" in parents and title = "{p}"'
        if trash: # if already send to trash (trashed = true), it is ok
            q_string += ' and trashed = false'
        if idx == len(file_path) - 1: # folder or file to delete
            delete_files(q_string)
        else: # folder in the sub-path, just extract parent_id
            q_string += " and mimeType = 'application/vnd.google-apps.folder'"
            folder = drive.ListFile({'q': q_string}).GetList()
            if len(folder) == 0: # not found, just return
                return
            if len(folder) > 1:
                raise ValueError(f'[ERROR]: multiple folders with the same path {"/".join(file_path[:idx + 1])} exist in google drive!')
            parent_id = folder[0]['id']
    return


def googledrive_mkdirs(drive: GoogleDrive, **config) -> str:
    """ Create a folder in google drive.
    @config(Dict[str, Any]): contain keys
        path(List[str]): folder path in google drive to create, e.g., ['folder1', 'folder2'] means /folder1/folder2, if folder1 not exists, create it first
        exist_ok(bool): if True, do not raise Error if already exists. By default, `exist_ok=True`.
    @return(str):
        the unique id of the last folder created
    Usage:
        {"type": "mkdirs", "path": ["folder1", "folder2"], "exist_ok": True}: create folder1/folder2 in google drive
        {"type": "mkdirs", "path": ["folder1"], "exist_ok": False}: create folder1 in google drive, raise error if already exists
    """
    folder_path = config['path']
    exist_ok = config.get('exist_ok', True)
    folder_path = [folder_path] if type(folder_path) != list else folder_path
    parent_id = 'root'
    for idx, p in enumerate(folder_path):
        q = f'"{parent_id}" in parents and title = "{p}" and mimeType = "application/vnd.google-apps.folder" and trashed = false'
        folder = drive.ListFile({'q': q}).GetList()
        if len(folder) == 0:  # not exists, create it
            parents = {} if parent_id == 'root' else {'parents': [{'id': parent_id}]}
            file = drive.CreateFile({'title': p, 'mimeType': 'application/vnd.google-apps.folder', **parents})
            file.Upload()
            parent_id = file['id']
        else:
            if len(folder) > 1:
                raise ValueError(f'[ERROR]: multiple folders with the same path {"/".join(folder_path[:idx + 1])} exist in google drive!')
            if not exist_ok and idx == len(folder_path) - 1:
                raise ValueError(f'[ERROR]: folder {"/".join(folder_path)} already exists in google drive!')
            parent_id = folder[0]['id']
    return parent_id


def googledrive_upload(drive: GoogleDrive, **config):
    """ Upload a file or a complete folder to google drive. If src is a folder, upload the folder tree recursively.
    @config(Dict[str, Any]): contain keys
        src(str): required, source file path in the local machine or remote url. For local machine, it can be a folder or a file. But for remote url, must be a single file.
        path(List[str]): required, target folder/file path to store the uploaded folder/file.
    @return:
        id(str): folder_id/file_id of the uploaded file/folder
    Usage:
        {"type": "upload", "src": "https://example.com/hello.txt", "path": ["hello.yaml"]}: upload a remote file to google drive file hello.yaml
        {"type": "upload", "src": "files/hello.txt", "path": ["folder1", "folder2", "hello.txt"]}: upload a local file to google drive file folder1/folder2/hello.txt
        {"type": "upload", "src": "files/", "path": ["folder1"]}: upload the entire local folder files/ to google drive folder1/ (`files` is renamed to `folder1`). If `folder1/` already exists on google drive, raise Error
    """
    src_path = config['src']
    target_path = config.get('path', [])
    target_path = [target_path] if type(target_path) != list else target_path

    if src_path.startswith('http'): # remote url, only support uploading a single file
        with tempfile.NamedTemporaryFile(mode='wb', delete=True) as tmpf:
            response = requests.get(src_path, stream=True)
            response.raise_for_status()
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    tmpf.write(chunk)
            tmpf.close()
            parents = {'parents': [{'id': googledrive_mkdirs(drive, path=target_path[:-1], exist_ok=True)}]} if len(target_path) > 1 else {}
            file = drive.CreateFile({'title': target_path[-1], **parents})
            file.SetContentFile(tmpf.name)
            file.Upload()
        return file['id']
    else: # local file or folder
        if platform.system() == 'Windows':
            src_path = src_path.replace('/', '\\')
        if not os.path.exists(src_path):
            raise FileNotFoundError(f'[ERROR]: local file/folder {src_path} not found!')

        if os.path.isfile(src_path): # upload a single file
            parents = {'parents': [{'id': googledrive_mkdirs(drive, path=target_path[:-1], exist_ok=True)}]} if len(target_path) > 1 else {}
            file = drive.CreateFile({'title': target_path[-1], **parents})
            file.SetContentFile(src_path)
            file.Upload()
            return file['id']
        else: # upload a local folder and the subtree in it recursivel. 
            assert os.path.isdir(src_path)
            # exist_ok=False: If the target folder exists on google drive, raise Error. Because, for a single file, it can be simply overwritten, but for a folder, not used files already existed may not be updated.
            parent_id = googledrive_mkdirs(drive, path=target_path, exist_ok=False)
            for file in os.listdir(src_path):
                file_path = os.path.join(src_path, file)
                if os.path.isfile(file_path):
                    parents = {'parents': [{'id': parent_id}]}
                    file = drive.CreateFile({'title': file, **parents})
                    file.SetContentFile(file_path)
                    file.Upload()
                else: # upload the subfolder recursively by automatically appending the subfolder name to the target_path
                    googledrive_upload(drive, src=file_path, path=target_path + [file])
            # just return the folder id
            return parent_id


GOOGLEDRIVE_INIT_FUNCTIONS = {
    "delete": googledrive_delete,
    "mkdirs": googledrive_mkdirs,
    "upload": googledrive_upload
}


def googledrive_init_setup(controller, **config):
    """ Clean google drive space (eliminate the impact of previous experiments to reset the environment)
    @config(Dict[str, Any]): contain keys
        settings_file(str): path to google drive settings file, which will be loaded by pydrive.auth.GoogleAuth(), by default,
            `evaluation_examples/settings/google/settings.yml` (which defines the filepath to client_secrets.json and credentials.json)
        actions(List[Dict[str, Any]]): each action is a dict with type chosen from ['delete', 'upload']
            - delete: delete files or folders in google drive
                query(str): [difficult, deprecated, removed] query pattern string to search files or folder in google drive to delete, please refer to
                    https://developers.google.com/drive/api/guides/search-files?hl=en about how to write query string
                path(List[str]): the folder or file path in the google drive to delete, e.g., ['folder1'] and ['folder1', 'file1']. By default, `path=[]`, which means deleting all files and folders in the root directory
                trash(bool): whether to delete files permanently or just move to trash (can be recovered). By default, `trash=false`, delete permanently
            - mkdirs: create folders in google drive
                path(List[str]): folder path in google drive to create, e.g., ['folder1', 'folder2'] means /folder1/folder2, if folder1 not exists, create it first
                exist_ok(bool): if True, do not raise Error if already exists. By default, `exist_ok=True`.
            - upload: upload a file or folder to google drive. If src is a folder, upload folder tree recursively.
                path(List[str]): target folder/file path to store the uploaded folder/file.
                src(str): source file path in the local machine or remote url
    """
    settings_file = config.get('settings_file', 'evaluation_examples/settings/google/settings.yml')
    gauth = GoogleAuth(settings_file=settings_file)
    drive = GoogleDrive(gauth)

    action_list: List[Dict[str, Any]] = config.get('actions', [])
    for action in action_list:
        action_type = action.pop('type', None)
        if action_type not in GOOGLEDRIVE_INIT_FUNCTIONS:
            raise ValueError(f'[ERROR]: action_type={action_type} not implemented in googledrive init function!')
        GOOGLEDRIVE_INIT_FUNCTIONS[action_type](drive, **action)
    return


def googledrive_login_setup(controller, **config):
    """ Login to a website with account and password information.
    @config(Dict[str, Any]): contain keys
        settings_file(str): path to the settings file, by default, 'evaluation_examples/settings/google/settings.json'
        listening_port(int): the port to listen to the remote debugging, by default, 9222
        url(str): the url to login, by default, 'https://drive.google.com/drive/my-drive'
        need_login(bool): default to True, whether need to login in to Google Account
    """
    host = controller.vm_ip
    port = config.get('listening_port', 9222)
    remote_debugging_url = f"http://{host}:{port}"

    with sync_playwright() as p:
        browser = get_browser(p, remote_debugging_url)
        if not browser:
            return

        context = browser.contexts[0]
        page = context.new_page()  # Create a new page (tab) within the existing context

        url = 'https://drive.google.com/drive/my-drive'
        settings = json.load(open(config['settings_file']))
        email, password = settings['email'], settings['password']

        try:
            page.goto(url)
            if config.get('need_login', True):
                google_account_login_in(page, email, password, timeout=60000) # wait for one minute to consider delay
            
        except Exception as e:
            logger.info('[ERROR]: unexpected error occurred when trying to login to the google drive!')
            return

        return browser, context