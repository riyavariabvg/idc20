translations = input()
num_list = [1,2,3,4]
for i in translations:
    new_list = []
    if i == "H":
        new_list.append(num_list[2])
        new_list.append(num_list[3])
        new_list.append(num_list[0])
        new_list.append(num_list[1])
    elif i == "V":
        new_list.append(num_list[1])
        new_list.append(num_list[0])
        new_list.append(num_list[3])
        new_list.append(num_list[2])

    num_list = new_list

print(str(num_list[0])+ " " + str(num_list[1]))
print(str(num_list[2])+ " " + str(num_list[3]))


