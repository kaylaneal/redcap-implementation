# EXPORT RECORDS FROM REDCAP -- FROM REDCAP API
from config import config
import requests

fields = {
    'token': config['API_TOKEN'],
    'content': 'record',
    'format': 'json',
    'type': 'flat'
}

r = requests.post(config['API_URL'], data = fields)
#print('HTTP Status: ' + str(r.status_code))
#print(r.text)