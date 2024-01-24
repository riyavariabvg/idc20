# # create a list
# mylist = [1, -7, 9, 2, 5, 204, 15, -87, 45, 3]


# # iterate and print the list
# # for element in mylist: # element is the next element in the list 
# #     print(element)     # works very similar to the range 

# # for i in range (len(mylist)):
# #     print(mylist[i])


# # # get the sum of all of the numbers in the list (2 different ways)
# # total = 0
# # for element in mylist:
# #     total += element
# # print(total)


# print(sum(mylist)) # sum returns the sum of all the elements 

# # print only the positive even numbers in the list
# mylist = [1, -7, 9, 2, 5, 204, 15, -87, 45, 3]
# for el in mylist:
#     if el > 0 and el % 2 == 0:
#         print(el)

# # get the largest and smallest number in the list
# smallest = mylist[0] # assume the first element is the smallest 
# biggest = mylist[0]
# for el in mylist:    # go through the list
#     if el < smallest:   # check if this element is the nw smallest
#         smallest = el   # if it is make it the smallest 
#     if el > biggest:
#         biggest = el

# # another way
# print(min(mylist))
# print(max(mylist))


# # in a list of Strings, get the string that would be considered largest in term of "alphabetical order"
# name_list = ["dev", "riya", "joshua", "arees", "alexander", "abraham", "daniel", "zaafir", "ishaan"]
# biggest_name = name_list[0]
# for el in name_list:
#     if el > biggest_name:
#         biggest_name = el

# print(biggest_name)
    
# print(max(name_list)) # zaafir
# print(min(name_list)) # abraham

# check = ["z", "a"]
# print(max(check))

# # work with min and max with strings, upper and lower are different
# check = ["A", "a"]
# print(max(check))



# # in a list of String, print the string with the longest length
# longest_length = len(name_list[0])
# word = None
# for el in name_list:
#     if len(el) > longest_length:
#         longest_length = len(el)
#         word = el
# print(word)

# print(max(name_list, key=len))
# print(max(name_list))

name_list = ["dev", "riya", "joshua", "arees", "alexander", "abraham", "daniel", "zaafir", "ishaan"]
longest = name_list[0]

for el in name_list:
    if len(longest) < len(el):
        longest = el

print(longest) # length
print(max(name_list, key=len)) # length
print(max(name_list)) # alpha

print(ord("A")) # ord returns the ASCII value for the character










