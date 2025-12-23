def search(arr):
    for key, val in arr.items():
        if dna_string.count(val) == 1:
            print(key)
            return key
    return()

Eva = {"gender" : "female", "race" : "white", "hair color" : "blonde", "eye color" : "blue", "face shape" : "oval"}
Larisa = { "gender" : "female", "race" : "white", "hair color" : "brown", "eye color" : "brown", "face shape" : "oval"}
Matej = { "gender" : "male", "race" : "white", "hair color" : "black", "eye color" : "brown", "face shape" : "oval"}
Miha = { "gender" : "male", "race" : "white", "hair color" : "brown", "eye color" : "green", "face shape" : "square"}
people_list = [Eva, Larisa, Matej, Miha]
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

