#coding=utf8
from .general import (
    script_and_execute_setup,
    copyfile_from_guest_to_host_setup,
    copyfile_from_host_to_guest_setup,
    google_chrome_browser_setup
)

from .bigquery import (
    bigquery_init_setup,
    bigquery_login_setup
)

from .dagster import (
    dagster_webui_init_setup
)

from .airbyte import (
    airbyte_webui_init_setup
)

from .google_cloud import (
    gcp_upload_keyfile_setup,
    gcp_webgui_setup,
    gcp_config_webgui_setup
)

from .googledrive import (
    googledrive_init_setup,
    googledrive_login_setup
)