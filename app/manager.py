from app import random_code
from app import exceptions
from app import config

import json
import uuid

# FixME(eliqiao): this is too urgly
MAX_RETRY = 1000000

conf = config.app_config()

class Manager(object):

    def __init__(self):
        if conf.get('db') == 'mc':
            from app import memorycache
            self.driver = memorycache.get_client()
        elif conf.get('db') == 'redis':
            from app import redis_client
            self.driver = redis_client.Client()

    def create_random(self, length, timeout=10):

        for i in range(MAX_RETRY):
            code = random_code.get_random_str(length)
            val = int(uuid.uuid4()) % 100000000000000
            data_dict = {'uuid': str(val)}
            data = json.dumps(data_dict)
            if self.driver.add(code, data, timeout):
                break
        else:
            # TODO(eliqiao): we may need to avoid this by adding uuid
            raise exceptions.CodeCreateFailed("no enough code can be created!")

        return {"code": code, "time_out": timeout, "uuid": str(val)}

    def get_random(self, code):
        code_find = self.driver.get(code)
        if code_find is None:
            raise exceptions.CodeNotFound("%s not found" % code)
        json_ret = json.loads(code_find)
        json_ret.update({"code": code})
        return json_ret

    def delete_random(self, code):
        self.driver.delete(code)

    def list_random(self):
        pass
