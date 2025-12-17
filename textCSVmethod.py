import csv
with open("data.csv","r") as csv_file:
    data = csv.reader(csv_file)
    for row in data:
        print(row[0] + " is " + row[1] + " years old and " + row[2])