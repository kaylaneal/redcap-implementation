# RETRIEVE PROJECT INFORMATION -- INCLUDED REDCAP API
from config import config
import requests
import pandas as pd

data = {
    'token': config['API_TOKEN'],
    'content': 'project',
    'format': 'json',
    'returnFormat': 'json'
}

r = requests.post(config['API_URL'], data = data)

pinfo = r.json()

df = pd.json_normalize(pinfo)
df.to_csv('project-info.csv')