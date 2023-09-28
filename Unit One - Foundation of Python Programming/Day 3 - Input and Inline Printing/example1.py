age = 40
name = "Steve"

print("My name is " + name + " and I am " + str(age) + " years old.")

# Issues with this type of print:
# I have to wrap non-string variables in a str
# A lot of poeple have issues with all the opening and closing of "" and all the + variable
# It is messy

print(f"My name is {name} and I am {age} years old.")
# fstring are so much better (formatted strings)
# automatically changes variables to strings and no need to use + symbols 


