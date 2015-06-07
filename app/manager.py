from app import random_code
from app import memorycache
from app import exceptions

import json
import uuid

# FixME(eliqiao): this is too urgly
MAX_RETRY = 1000000


class Manager(object):

    def __init__(self):
        self.mc = memorycache.get_client()

    def create_random(self, length, timeout=10):

        for i in range(MAX_RETRY):
            code = random_code.get_random_str(length)
            code_exist = self.mc.get(code)
            if not code_exist:
                val = int(uuid.uuid4()) % 100000000000000
                data_dict = {'uuid': str(val)}
                data = json.dumps(data_dict)
                break
        else:
            # TODO(eliqiao): we may need to avoid this by adding uuid
            raise exceptions.CodeCreateFailed("no enough code can be created!")

        self.mc.set(code, data, timeout)
        return {"code": code, "time_out": timeout, "uuid": str(val)}

    def get_random(self, code):
        code_find = self.mc.get(code)
        if code_find is None:
            raise exceptions.CodeNotFound("%s not found" % code)
        json_ret = json.loads(code_find)
        json_ret.update({"code": code})
        return json_ret

    def delete_random(self, code):
        self.mc.delete(code)

    def list_random(self):
        pass
