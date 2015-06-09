# Copyright 2010 United States Government as represented by the
# Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""Super simple fake memcache client."""

from app import config

import redis

conf = config.app_config()

class Client(object):

    def __init__(self, *args, **kwargs):
        """Ignores the passed in args."""
        self.host = conf.get('host')
        self.port = conf.get('port')
        self.password = conf.get('password')
        self.db = int(conf.get('db', 1))
        print self.host
        print type(self.host)
        print self.port
        print type(self.port)
        print self.password
        print type(self.password)
        print self.db
        print type(self.db)
        try:
            self.client = redis.Redis(host=self.host,
                                      port=self.port,
                                      password=self.password,
                                      db=self.db)
        # FIXME need to catch specify exception
        except Exception as e:
            print e
            raise

    def get(self, key):
        """Retrieves the value for a key or None.

        This expunges expired keys during each get.
        """

        return self.client.get(key)

    def set(self, key, value, time=0, min_compress_len=0):
        """Sets the value for a key."""
        try:
            self.client[key] = value
            self.client.expire(key, time)
        except Exception as e:
            print e
            raise
        return key

    def add(self, key, value, time=0, min_compress_len=0):
        """Sets the value for a key if it doesn't exist."""
        if self.get(key) is not None:
            return False
        return self.set(key, value, time, min_compress_len)

    def incr(self, key, delta=1):
        """Increments the value for a key."""
        pass

    def delete(self, key, time=0):
        """Deletes the value associated with a key."""
        self.client.delete(key)

