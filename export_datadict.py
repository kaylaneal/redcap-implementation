# EXPORT METADATA (VARIABLE/FIELD NAMES) -- FROM REDCAP API
from config import config
import requests
import pandas as pd

fields = {
    'token': config['API_TOKEN'],
    'content': 'exportFieldNames',
    'format': 'json',
    'returnFormat': 'json'
}

r = requests.post(config['API_URL'], data = fields)
#print('HTTP Status: ' + str(r.status_code))

ddict = r.json()

df = pd.json_normalize(ddict)
df.to_csv('data-dictionary.csv')