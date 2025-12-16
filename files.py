#data_file = open("SnumData.txt","r")

#content = data_file.read()
#print(content)

#data_file.close()

with open("SnumData.txt", "r") as data_file:
    content = data_file.read().splitlines()
    for line in content:
        print("Line: " + line)
