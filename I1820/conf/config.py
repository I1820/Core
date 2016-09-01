# In The Name Of God
# ========================================
# [] File Name : config.py
#
# [] Creation Date : 01-09-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
import yaml
import os

from ..pykaa.rest.app import KaaRestApplication


class I1820Kaa:
    def __init__(self, name, kaa):
        # Application
        self.app = {}
        kra = KaaRestApplication('%s:%s' % (kaa['host'], kaa['port']),
                                 kaa['user_developer'],
                                 kaa['passwd_developer'])
        apps = kra.get_all_applications()
        for app in apps:
            if app.name == name:
                self.app['name'] = app.name
                self.app['token'] = app.application_token
                self.app['uid'] = app.id
        # Notification


class I1820Config:
    def __init__(self, path):
        with open(path, 'r') as ymlfile:
            cfg = yaml.load(ymlfile)
        self.cfg = cfg
        self.kaa = I1820Kaa(cfg['app']['name'], cfg['kaa'])

    def __getattr__(self, name):
        section, field = name.split('_', maxsplit=1)
        if section == 'kaa' or section == 'mongodb':
            return self.cfg[section][field]
        elif section == 'app':
            return self.kaa.app[field]
        elif section == 'notification':
            return None


I1820_CONFIG_PATH = os.path.join(os.path.dirname(__file__), "1820.yml")
cfg = I1820Config(I1820_CONFIG_PATH)
