# ADD A RECORD TO THE DATABASE
from config import config
import requests
import pandas as pd

nRecord = pd.read_csv('new-records.csv')

data = {
    'token': config['API_TOKEN'],
    'content': 'record',
    'action': 'import',
    'format': 'csv',
    'type': 'flat',
    'overwriteBehavior': 'normal',
    'forceAutoNumber': 'true',
    'data': nRecord,
    'returnContent': 'nothing',
    'returnFormat': 'json'
}

r = requests.post(config['API_URL'], data = data)
#print('HTTP Status: ' + str(r.status_code))
print(r.json())
