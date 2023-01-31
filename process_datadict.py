# READ FIELD NAMES FROM DD INTO VARIABLES
import export_datadict
import json

fields = json.loads( export_datadict.r.text ) # LIST OF DICTIONARIES
fNames = set()

# for each list element (dict)
for f in fields:
    # for each dict key (str)
    for key, val in f.items():
        fNames.add(val)

vari_names = list(fNames)
vari_names.sort()

for i in vari_names:
    if i == (''):
        vari_names.remove(i)