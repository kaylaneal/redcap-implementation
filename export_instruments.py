# EXPORT INSTRUMENTS -- DATA ENTRY FORMS
import requests
from config import config
import pandas as pd

data = {
    'token': config['API_TOKEN'],
    'content': 'instrument',
    'format': 'json',
    'returnFormat': 'json'
}

r = requests.post(config['API_URL'], data = data)
print('HTTP Status: ' + str(r.status_code))

inst = r.json()
df = pd.json_normalize(inst)
df.to_csv("instruments.csv")