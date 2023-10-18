length = len("Hello World") # len function that takes a string and returns the number of characters
# "Hello World" is the argument that len function took, it returned the value 9
print(length)               # print function that takes a string or any other type and prints it to the screen

mystery = print("Happy Cat")
print(mystery)      # the function print() returns nothing (None)


# In line 1, the argument is "Hello World"
# In line 3, the argument is length
# In line 5, the argument is "Happy Cat"
# In line 6, the argument is mystery

width = int(input("Please enter a width: "))
# 'Please enter a width: ' is the argument for the input function
# it returns what the user entered
# that will be the argument for the int function
# the int function will convert that into an int and return it which gets assigned to width
print(width)


def area(length, width):
    return length * width


print(area(5, 6))

# displaying in the console is what a function does. Ex. the print returns to the console. When it returns is when it is finished doing what it does.
# input will wait until the user enters data. 


print(round(4.35234, 2))
print(round(34.6766876, 0)) # this will be 35.0 (use the round() without the 0 instead)




