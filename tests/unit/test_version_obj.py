import sys

sys.path.append("../..")


from app import version_obj

import unittest



class TestVersionObj(unittest.TestCase):

    def setUp(self):

        self.ver_obj = version_obj.version_obj('', '1.0')
        self.ver_obj1 = version_obj.version_obj('', '1.00')
        self.ver_obj2 = version_obj.version_obj('', '1.2')
        self.ver_obj3 = version_obj.version_obj('', '0.9')

    def test_version_equal(self):
        self.assertTrue(self.ver_obj == self.ver_obj1)

    def test_version_high(self):
        self.assertTrue(self.ver_obj2 > self.ver_obj1)

    def test_version_low(self):
        self.assertTrue(self.ver_obj3 < self.ver_obj1)


if __name__ == '__main__':
    unittest.main()
