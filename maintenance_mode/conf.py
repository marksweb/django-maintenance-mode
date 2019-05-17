# -*- coding: utf-8 -*-
import os

from django.utils.module_loading import import_module

from maintenance_mode.settings import Settings


MODE_STATE_FILE_NAME = 'maintenance_mode_state.txt'


def get_state_file_path():
    settings_module = import_module(os.environ['DJANGO_SETTINGS_MODULE'])
    settings_path = settings_module.__file__
    settings_dir = os.path.dirname(settings_path)

    return os.path.abspath(
        os.path.join(os.sep, settings_dir, MODE_STATE_FILE_NAME)
    )


DEFAULTS = {
    'MAINTENANCE_MODE': None,
    'MAINTENANCE_MODE_GET_CLIENT_IP_ADDRESS': None,
    'MAINTENANCE_MODE_GET_TEMPLATE_CONTEXT': None,
    'MAINTENANCE_MODE_IGNORE_ADMIN_SITE': None,
    'MAINTENANCE_MODE_IGNORE_ANONYMOUS_USER': None,
    'MAINTENANCE_MODE_IGNORE_AUTHENTICATED_USER': None,
    'MAINTENANCE_MODE_IGNORE_IP_ADDRESSES': None,
    'MAINTENANCE_MODE_IGNORE_STAFF': False,
    'MAINTENANCE_MODE_IGNORE_SUPERUSER': None,
    'MAINTENANCE_MODE_IGNORE_TESTS': None,
    'MAINTENANCE_MODE_IGNORE_URLS': None,
    'MAINTENANCE_MODE_REDIRECT_URL': None,
    'MAINTENANCE_MODE_STATE_BACKEND': 'maintenance_mode.backends.LocalFileBackend',
    'MAINTENANCE_MODE_STATE_FILE_NAME': MODE_STATE_FILE_NAME,
    'MAINTENANCE_MODE_STATE_FILE_PATH': get_state_file_path(),
    'MAINTENANCE_MODE_TEMPLATE': '503.html',
    'MAINTENANCE_MODE_STATUS_CODE': 503,
    'MAINTENANCE_MODE_RETRY_AFTER': 3600
}


settings = Settings(DEFAULTS)
