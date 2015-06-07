# Copyright 2015 Eli Qiao
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


from app import app
from app import manager
from app import validation
from app import exceptions

from flask import abort
from flask import jsonify
from flask import request
from flask import make_response

random_manager = manager.Manager()

@app.route('/')
@app.route('/index')
def index():
    print app.app_context()
    return "hello world!"

#create a random code with a timeout window
@app.route('/random', methods=['POST'])
def create_random():
    print request.json
    req = request.json
    try:
        validation.validate(req, validation.create_random)

        length = req.get('length')
        timeout = req.get('time_out', 10)

        ret = random_manager.create_random(length, timeout=timeout)
    except exceptions.inValidateInput as e:
        return error_json_out(404, e.message)
    except exceptions.CodeCreateFailed as e:
        return error_json_out(403, e.message)
    return jsonify(ret), 201

#verify random code exist
@app.route('/random/<string:code>', methods=['GET'])
def get_random(code):
    try:
        ret = random_manager.get_random(code)
    except exceptions.CodeNotFound as e:
        return error_json_out(404, e.message)
    return jsonify(ret)

@app.route('/random/<string:code>', methods=['DELETE'])
def delete_random(code):
    try:
        ret = random_manager.get_random(code)
    except exceptions.CodeNotFound as e:
        return error_json_out(404, e.message)
    random_manager.delete_random(code)
    return jsonify({}), 200

@app.errorhandler(404)
def not_found(error):
    return make_response("error, not found", 404)

def error_json_out(code, msg):
    return jsonify({'error': msg}), code
