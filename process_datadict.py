# READ FIELD NAMES FROM DD INTO VARIABLES
import export_datadict
import json

fields = json.loads( export_datadict.r.text ) # LIST OF DICTIONARIES
fieldNames = set()

# for each list element (dict)
for f in fields:
    # for each dict key (str)
    for key, val in f.items():
        fieldNames.add(val)

fieldNames = list(fieldNames)
fieldNames.sort()

for i in fieldNames:
    if i == (''):
        fieldNames.remove(i)

print ("Variables Being Collected: ")
print(fieldNames)