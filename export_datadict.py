# EXPORT METADATA (VARIABLE/FIELD NAMES) -- FROM REDCAP API
from config import config
import requests

fields = {
    'token': config['API_TOKEN'],
    'content': 'exportFieldNames',
    'format': 'json',
    'returnFormat': 'json'
}

r = requests.post(config['API_URL'], data = fields)
#print('HTTP Status: ' + str(r.status_code))
#print(r.text)