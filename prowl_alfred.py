# Copyright 2013 Ken Pepple <ken@pepple.info>
#
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

import alfred_utils as utils
import requests

PROWL_URL = "https://api.prowlapp.com/publicapi/"


def get_api_key():
    return utils.get_config('apikey')

def get_priority_key():
    return utils.get_config('priority')

def verify_apikey(apikey):
    parameters = {'apikey': apikey}
    r = requests.post(PROWL_URL + "verify", params=parameters)
    return r.ok

def save_api_key(apikey):
    utils.save_config('apikey',apikey)

def send_prowl(description, application="Alfred", event="event", priority=0):
    try:
        apikey = get_api_key()
    except:
        raise.Exception "No APIKEY. Please configure by holding down the cmd key and pasting in prowl APIKEY."
    parameters = {'apikey': apikey, 'event': event, 'application': application,
                  'priority': priority, 'description': description}
    r = requests.post(PROWL_URL + "add", params=parameters)
    return r.ok
