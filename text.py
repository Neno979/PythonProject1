with open("data.csv","r") as csv_file:
    for line in csv_file:
        l=line.split(",")
        print(l[0] + " is " + l[1] +" years old and " + l[2])
