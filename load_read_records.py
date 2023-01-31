# Load in and display records from RedCap into a readable format
# CREATES TEXT FILE

import export_records
import json

recordus = json.loads(export_records.r.text) # LIST OF CURRENT RECORDS
records = []

# FOR EACH RECORD (DICT) IN LIST:
for rec in recordus:
    sortRec = sorted(rec.items())
    records.append(sortRec)
'''
for i in records:
    print(i)
'''

recFileOut = open("exportedRecords.txt", "w")

for r in records:
    for t in r:
        recFileOut.write("Variable: " + t[0] + ", Value: " + t[1] + '\n')
    recFileOut.write('\n')

recFileOut.close()
