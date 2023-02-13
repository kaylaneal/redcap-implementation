# EXPORT LOGGING INFORMATION
from config import config
import requests
import pandas as pd

data = {
    'token': config['API_TOKEN'],
    'content': 'log',
    'logtype': '',								# CAN BE FILTERED BY EVENT
    'user': '',									# CAN BE FILTERED BY USER
    'record': '',								# CAN BE FILTERED BY RECORD ID
    'beginTime': '2023-02-03 14:25',			# DATE PROJECT CREATED
    'endTime': '',
    'format': 'json',
    'returnFormat': 'json'
}

r = requests.post(config['API_URL'], data = data)
print('HTTP Status: ' + str(r.status_code))

logs = r.json()

df = pd.json_normalize(logs)
df.to_csv('logs.csv')