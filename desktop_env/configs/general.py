#coding=utf8

def download_and_execute_setup(controller, url: str, path: str = '/home/user/init.sh'):
    """ Download a script from a remote url and execute it to setup the environment.
    @args:
        controller(desktop_env.controllers.SetupController): the controller object
        url(str): remote url to download the script
        path(str): the path to save the script on VM (default: '~/init.sh')
    """
    # download the script
    controller._download_setup([{'url': url, 'path': path}])
    # execute the script
    controller._execute_setup(command=["chmod", "a+x", path])
    controller._execute_setup(command=["/bin/bash", path])
    controller._execute_setup(command=["rm", "-f", path])
    return


def clear_terminal_history_setup(controller, **kwargs):
    pass