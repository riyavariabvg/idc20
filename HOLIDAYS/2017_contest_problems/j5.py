N = int(input())
wood_pieces_strings = input()
wood_pieces_strings = wood_pieces_strings.split(" ")
wood_pieces = []
for i in wood_pieces_strings:
    wood_pieces.append(int(i))

wood_pieces.sort()
previous_num = None 
inner_num = None 
board_list = []

for i in range(len(wood_pieces)):
    previous_num = None
    inner_num = None
    for j in range(i + 1, len(wood_pieces)):
        inner_num = wood_pieces[j]
        if inner_num != previous_num:
            board_list.append(wood_pieces[i] + wood_pieces[j])
        
        previous_num = inner_num

board_list.sort()
count = 0
max_length_list = []
previous_num = -1

count = 1
for i in range(len(board_list)):
    if board_list[i] == previous_num:
        count = count + 1
    else:
        max_length_list.append(count)
        count = 1
        previous_num = board_list[i]

max_length = 1

for i in max_length_list:
    if i > max_length:
        max_length = i

different_heights = 0

for j in max_length_list:
    if j == max_length:
        different_heights += 1

         
print(f"{max_length} {different_heights}")

    



