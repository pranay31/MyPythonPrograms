import csv
f = open('sample.csv')
dt = csv.reader(f)

for r in dt:
    print r[1]
