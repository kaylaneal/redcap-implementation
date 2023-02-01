# RETRIEVE PROJECT INFORMATION -- INCLUDED REDCAP API
from config import config
import requests

data = {
    'token': config['API_TOKEN'],
    'content': 'project',
    'format': 'json',
    'returnFormat': 'json'
}

r = requests.post(config['API_URL'], data = data)

print(r.json())