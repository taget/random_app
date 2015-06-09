# config.py
# helper class to load variable
#

# default db backend is mc
# plan to support redis
import os


class app_config(object):

    def __init__(self):
        self._default_var = {
        'db_backend': 'mc',
        }

    def get(self, var, val=None):
        """get variable
        """
        ret = os.getenv(var, self._default_var.get(var))
        if ret is None and val is not None:
            return val
        return ret
