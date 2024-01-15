coordinate1_strings = input()
coordinate2_strings = input()
charge = int(input())


coordinate1_strings = coordinate1_strings.split(" ")
coordinate2_strings = coordinate2_strings.split(" ")
coordinate1 = []
coordinate2 = []

for i in coordinate1_strings:
    coordinate1.append(int(i))

for i in coordinate2_strings:
    coordinate2.append(int(i))


x_difference = abs(coordinate1[0] - coordinate2[0])
y_difference = abs(coordinate1[1] - coordinate2[1])

path_sums = x_difference + y_difference

if path_sums > charge:
    print("N")

elif path_sums == charge:
    print("Y")

else:
    charge_to_cover = charge - path_sums
    if charge_to_cover % 2 == 0:
        print("Y")
    else:
        print("N")