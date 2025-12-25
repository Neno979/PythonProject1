
country_capital = {"Croatia" : "Zagreb" , "Colombia" : "Bogota" , "Morocco" : "Marrakesh" , "Laos" : "Vientiane" , "Mexico" : "Mexico City" , "Australia" : "Canberra"}
result = 0
for country, capital in country_capital.items():
    city = input("What is the capital city of " + country + "? ")
    if city == capital:
        result += 1
        print("answer is correct")
    else:
        print("answer is incorrect")
print("Congratulations! your score is: " + str(result))

