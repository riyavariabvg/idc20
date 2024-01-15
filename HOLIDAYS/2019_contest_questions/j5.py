sub1 = input().split(" ") #["AA", "AB"]
sub2 = input().split(" ") #["AB", "BB"]
sub3 = input().split(" ") #["B", "AA"]
pattern = input().split(" ") #["4", AB", "AAAB"]
num_of_steps = int(pattern[0]) # 4
initial_sequence = pattern[1] #AB
final_sequence = pattern[2] #AAAB

# def perform_substitution(current_sequence, sub):
#     current_sequence = current_sequence.replace(sub[0], sub[1],1)
#     return current_sequence

# current_sequence = initial_sequence
# # previous_list = [current_sequence]



# current_sequences = [current_sequence]

# for i in range(num_of_steps):
#     sequences = current_sequences
#     current_sequences = []
#     for i in sequences:
#         current_sequence = i
#         for idx in range(len(current_sequence)):
#             if current_sequence[idx: idx + len(sub1[0])] == sub1[0]:
#                 current_sequences.append(current_sequence[0: idx] + sub1[1] + current_sequence[idx+len(sub1[0]):len(current_sequence)])
            
#             if current_sequence[idx: idx + len(sub2[0])] == sub2[0]:
#                 current_sequences.append(current_sequence[0: idx] + sub2[1] + current_sequence[idx+len(sub2[0]):len(current_sequence)])

#             if current_sequence[idx: idx + len(sub3[0])] == sub3[0]:
#                 current_sequences.append(current_sequence[0: idx] + sub3[1] + current_sequence[idx+len(sub3[0]):len(current_sequence)])
    


sequences = []
# sequences = [[2,1,"BB"], [3, 2, "AAA"]]
# sequences = [[[2, 1, "BB"]]]

current_sequence = initial_sequence
for idx in range (len(current_sequence)):
    if current_sequence[idx: idx + len(sub1[0])] == sub1[0]:
        new_list = [1, idx + 1, current_sequence[0: idx] + sub1[1] + current_sequence[idx+len(sub1[0]):len(current_sequence)]]
        sequences.append(new_list)
            
    if current_sequence[idx: idx + len(sub2[0])] == sub2[0]:
        new_list = [2, idx + 1, current_sequence[0: idx] + sub2[1] + current_sequence[idx+len(sub2[0]):len(current_sequence)]]
        sequences.append(new_list)

    if current_sequence[idx: idx + len(sub3[0])] == sub3[0]:
        new_list = [3, idx + 1, current_sequence[0: idx] + sub3[1] + current_sequence[idx+len(sub3[0]):len(current_sequence)]]
        sequences.append(new_list)

previous_list = sequences
print(previous_list)

for i in range(1):
    final_list = []
    for sequence in previous_list:
        current_sequence = sequence[len(sequence)-1]
        for idx in range (len(current_sequence)):
            if current_sequence[idx: idx + len(sub1[0])] == sub1[0]:
                print(f"sequence {sequence}")
                new_list = []
                new_list = sequence
                new_list.append(1)
                new_list.append(idx + 1)
                new_list.append(current_sequence[0: idx] + sub1[1] + current_sequence[idx+len(sub1[0]):len(current_sequence)])
                final_list.append(new_list)
                    
            if current_sequence[idx: idx + len(sub2[0])] == sub2[0]:
                print(f"sequence {sequence}")
                new_list.clear()
                new_list = sequence
                new_list.append(2)
                new_list.append(idx + 1)
                new_list.append(current_sequence[0: idx] + sub2[1] + current_sequence[idx+len(sub2[0]):len(current_sequence)])
                final_list.append(new_list)

            if current_sequence[idx: idx + len(sub3[0])] == sub3[0]:
                print(f"sequence {sequence}")
                new_list.clear()
                new_list = sequence
                new_list.append(3)
                new_list.append(idx + 1)
                new_list.append(current_sequence[0: idx] + sub3[1] + current_sequence[idx+len(sub3[0]):len(current_sequence)])
                final_list.append(new_list)
            
            print(final_list)
    previous_list = final_list

print(final_list)












# Algorithm:
        # 1. find instances of a substitution possibility in the list
        # 2. if by replacing the substring, the string gets closer to the final_sequence, then do it
        # 3. else, find a different substring to replace 
            

            



    

    






