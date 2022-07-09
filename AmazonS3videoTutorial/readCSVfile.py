import csv
outputlist=[]
with open('empdata.csv',newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
        outputlist.append(row.values())

print(outputlist)
