Poblano = 1500
Mirasol = 6000
Serrano = 15500
Cayenne = 40000
Thai = 75000
Habanero = 125000

chili_sum = 0
number_of_peppers = int(input())

for x in range (number_of_peppers):
    i = input()
    if i == "Poblano":
        chili_sum = chili_sum + Poblano
    
    elif i == "Mirasol":
        chili_sum = chili_sum + Mirasol

    elif i == "Serrano":
        chili_sum = chili_sum + Serrano
    
    elif i == "Cayenne":
        chili_sum = chili_sum + Cayenne

    elif i == "Thai":
        chili_sum = chili_sum + Thai

    else:
        chili_sum = chili_sum + Habanero

print(chili_sum)

