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
            raise Exception("Bundle ID not defined or readable from info.plist.")
    else:
        raise Exception("info.plist missing.")
    return this_bundle_id

def get_config_path(config_file=None):
    bundle_id = get_bundle_id()
    nvPath = os.path.expanduser(os.path.join("~/Library/Application Support/Alfred 2/Workflow Data/", bundle_id))
    if not os.path.exists(nvPath):
        os.makedirs(nvPath)
    if config_file:
        nvPath = os.path.join(nvPath, config_file)
    return nvPath

def get_config(config_key, section="defaults", config_file="config.ini"):
    config = ConfigParser.RawConfigParser()
    config.read(get_config_path(config_file))
    return config.get(section, config_key)

def save_config(config_key, config_value, config_file="config.ini"):
    config = ConfigParser.RawConfigParser()
    config.add_section('defaults')
    config.set('defaults', config_key, config_value)
    with open(get_config_path(config_file), 'wb') as configfile:
        config.write(configfile)

