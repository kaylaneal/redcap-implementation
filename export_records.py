# EXPORT RECORDS FROM REDCAP 
from config import config
import requests
import pandas as pd

fields = {
    'token': config['API_TOKEN'],
    'content': 'record',
    'format': 'json',
    'type': 'flat'
}

r = requests.post(config['API_URL'], data = fields)
#print('HTTP Status: ' + str(r.status_code))
#print(r.text)

recs = r.json()

df = pd.json_normalize(recs)
df.to_csv('current-records.csv')