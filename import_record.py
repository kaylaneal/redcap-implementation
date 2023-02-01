# ADD A RECORD TO THE DATABASE -- REDCAP API
from config import config
import requests

'''
import_record (
    token: API_TOKEN
    content: record
    format: json, csv, xml (default), odm
    type: flat (output as one record/row), eav (input as one data point per row)
    overwriteBehavior: normal (ignore empty - default), overwrite (overwrite with empty value)
    forceAutoNumber: true (new record names auto determined), false (provided record name used -- default)
    data: data
)
'''