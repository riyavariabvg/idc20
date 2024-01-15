question_type = int(input())
N = int(input())
country1_speeds_strings = input()
country1_speeds_strings = country1_speeds_strings.split(" ")


country1_speeds = []
for i in country1_speeds_strings:
    i = int(i)
    country1_speeds.append(i)

country2_speeds_strings = input()
country2_speeds_strings = country2_speeds_strings.split(" ")
country2_speeds = []
for i in country2_speeds_strings:
    i = int(i)
    country2_speeds.append(i)

country1_speeds.sort()
country2_speeds.sort()
all_speeds = []
for i in country1_speeds:
    all_speeds.append(i)

for i in country2_speeds:
    all_speeds.append(i)

if question_type == 1:
    minimum = 0
    for i in range(N):
        minimum = minimum + max(country1_speeds[i], country2_speeds[i])
    
    print(minimum)

else:
    maximum = 0
    all_speeds.sort()
    counter = len(all_speeds)-1
    for i in range(N):
        maximum += all_speeds[counter]
        counter = counter -1
    
    print(maximum)
    





