import sys
import os
import unittest

sys.path.append("../..")


from app import config


class TestConfig(unittest.TestCase):

    def setUp(self):
        self._config = config.app_config()

    def test_get(self):
        os.environ['xx'] = '1'
        self.assertEqual('1', self._config.get('xx'))

    def test_get_not_found(self):

        self.assertEqual(None, self._config.get('none-fake'))

    def test_get_has_default(self):
        #self.assertEqual('mc', self._config.get('db'))
        pass

