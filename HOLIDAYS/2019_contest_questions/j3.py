number_of_lines = int(input())
output_lines = []

for i in range(number_of_lines):
    output_line = ""
    sequence = input()
    sequence = sequence + " "
    previous_symbol = sequence[0]
    count = 0
    for i in sequence:
        if i == previous_symbol:
            count += 1
        else:
            output_line = output_line + str(count) + " " + previous_symbol + " "
            count = 1
        
        previous_symbol = i

    output_lines.append(output_line)

for i in output_lines:
    print(i.rstrip())

            
