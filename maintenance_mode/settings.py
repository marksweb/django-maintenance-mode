# -*- coding: utf-8 -*-
from django.conf import settings


class Settings(object):
    """Lazy settings wrapper, for use in app-specific conf.py files"""

    def __init__(self, defaults):
        """
        Constructor

        :param defaults: default values for settings, will be return if
                         not overridden in the project settings
        :type defaults: dict
        """
        self.defaults = defaults

    def __getattr__(self, name):
        """
        Return the setting with the specified name, from the project settings
        (if overridden), else from the default values passed in during
        construction.

        :param name: name of the setting to return
        :type name: str or unicode
        :return: the named setting
        :raises: AttributeError -- if the named setting is not found
        """
        if hasattr(settings, name):
            return getattr(settings, name)
        if name in self.defaults:
            return self.defaults[name]
        raise AttributeError("'{name}' setting not found".format(name=name))
