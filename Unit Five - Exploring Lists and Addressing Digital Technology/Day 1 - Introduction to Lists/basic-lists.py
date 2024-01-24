# Var = ["Geeks", "for", "Geeks"]
# print(Var)

# Python program to demonstrate
# Creation of List

# Creating a List
# List = []
# print("Blank List: ")
# print(List)

# # Creating a List of numbers
# List = [10, 20, 14]
# print("\nList of numbers: ")
# print(List)

# # Creating a List of strings and accessing
# # using index
# List = ["Geeks", "For", "Geeks"]
# print("\nList Items: ")
# print(List[0])
# print(List[2])

list = []
list.append("hello")
list.append("kamea")
list.append("riya")
list.append("fries")
 
print(list)
list.append(7)
print(list)
 
list.insert(2, "dev")
print(list)
list.remove("fries")
 
list.pop(1)
print(list)

def reverse3(nums):
  list = [nums[2],nums[1],nums[0]]
  return list


