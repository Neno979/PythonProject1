def search(arr):
    for key, val in arr.items():
        if dna_string.count(val) == 1:
            return key
    return ()



Eva = ["female", "white", "blonde", "blue", "oval"]
Larisa = ["female", "white", "brown", "brown", "oval"]
Matej = ["male", "white", "black", "brown", "oval"]
Miha = ["male", "white", "brown", "green", "square"]
people_list = [Eva, Larisa, Matej, Miha]
suspect_name = ["Eva" , "Larisa" , "Matej" , "Miha" ]
hair_color = {"black" : "CCAGCAATCGC" , "brown" : "GCCAGTGCCG" , "blonde" : "TTAGCTATCGC"}
facial_shape = {"square" : "GCCACGG" , "round" : "ACCACAA" , "oval" : "AGGCCTCA"}
eye_color = {"blue" : "TTGTGGTGGC" , "green" : "GGGAGGTGGC" , "brown" : "AAGTAGTGAC"}
gender = {"female" : "TGAAGGACCTTC" , "male" : "TGCAGGAACTTC" }
race = {"white" : "AAAACCTCA" , "black" : "CGACTACAG" , "asian" : "CGCGGGCCG"}
att_list = [gender, race, hair_color, eye_color, facial_shape ]
suspect_data = []
with open("dna.txt", "r") as dna_file:
    dna_string = dna_file.read()
for att in att_list:
    suspect_data.append (search(att))

print(suspect_data)
p = 0
for person in people_list:
    if person == suspect_data:
        print("The main suspect is " + suspect_name[p])
    p += 1



