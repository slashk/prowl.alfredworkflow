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

import ConfigParser
import os
import plistlib

def get_bundle_id():
    info_path = os.path.abspath("./info.plist")
    if os.path.exists(info_path):
        info = plistlib.readPlist(info_path)
        try:
            this_bundle_id = info["bundleid"]
        except KeyError:
            raise Exception("Bundle ID not defined")
    else:
        raise Exception("Error reading info.plist!")
    return this_bundle_id

def get_config_path(config_file=None):
    bundle_id = get_bundle_id()
    this_config_path = os.path.expanduser(os.path.join("~/Library/Application Support/Alfred 2/Workflow Data/", bundle_id))
    if not os.path.exists(this_config_path):
        try:
            os.makedirs(this_config_path)
        except:
            raise Exception("Cannot create configuration file")
    if config_file:
        this_config_path = os.path.join(this_config_path, config_file)
    return this_config_path

def get_config(config_key, section="defaults", config_file="config.ini"):
    config = ConfigParser.RawConfigParser()
    try:
        config.read(get_config_path(config_file))
        config_value = config.get(section, config_key)
    except:
        raise Exception("Cannot read configuration file or key")
    return config_value

def save_config(config_key, config_value, config_file="config.ini"):
    config = ConfigParser.RawConfigParser()
    config.add_section('defaults')
    config.set('defaults', config_key, config_value)
    with open(get_config_path(config_file), 'wb') as configfile:
        config.write(configfile)

