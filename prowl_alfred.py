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
    prowl_url = "http://api.prowlapp.com/publicapi/add"
    try:
    	apikey = get_api_key()
    except:
    	print "No APIKEY. Please configure by holding down the cmd key"\
              "and pasting in prowl APIKEY."
    parameters = {'apikey': apikey, 'event': event, 'application': application,
                  'priority': priority, 'description': description}
    r = requests.post(PROWL_URL + "add", params=parameters)
    return r.ok
