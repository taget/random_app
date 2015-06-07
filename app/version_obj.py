###################
###################

from app import exceptions

class version_obj(object):

    def __init__(self, req, version=None):
        self._get_version(version)
        self.req = req

    def __eq__(self, obj):
        return self.min == obj.min and self.max == obj.max

    def __gt__(self, obj):
        if self.max > obj.max:
            return True
        elif self.max == obj.max:
            return self.min > obj.min
        else:
            return False
    def __lt__(self, obj):
        if self.max < obj.max:
            return True
        elif self.max == obj.max:
            return self.min < obj.min
        else:
            return False

    def _get_version(self, ver=None):
        #ver is a str
        if ver is not None:
            tmp =  float(ver)
            self.max = int(tmp)
            self.min = tmp - self.max
        else:
            self.min = 0
            self.max = 1

    def __str__(self):
        return "%f" % (self.max + self.min)

