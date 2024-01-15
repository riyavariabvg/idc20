num_of_lines = int(input())
line_list = []

for i in range(num_of_lines):
    line = input()
    line = line.split(" ")
    line_list.append(line[1]*int(line[0]))

for i in line_list:
    print(i)

