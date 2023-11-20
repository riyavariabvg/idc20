number_grade = 76

# These are all SEPERATE if statements so they each run seperately
# if number_grade >= 80:
#     print("A")

# if number_grade >= 70:
#     print("B")

# if number_grade >= 60:
#     print("C")

# if number_grade >= 50:
#     print("D")

# if number_grade < 50:
#     print("F")


# The following code has 5 seperate if statements 
# if number_grade >= 80:
#     print("A")
# if 70 <= number_grade < 80: # does not include 80 
#     print("B")
# if 60 <= number_grade < 70:
#     print("C")
# if 50 <= number_grade < 60:
#     print("D")
# if number_grade < 50:
#     print("F")

# prints B (Works as intended)



# if number_grade >= 80:
#     print("A")
# elif number_grade >= 70:
#     print("B")
# elif number_grade >= 60:
#     print("C")
# elif number_grade >= 50:
#     print("D")
# elif number_grade < 50:
#     print("F")


# if number_grade >= 80:
#     print("A")
# elif number_grade >= 70:
#     print("B")
# elif number_grade >= 60:
#     print("C")
# elif number_grade >= 50:
#     print("D")
# else:
#     print("F")


def inspect_number(x):
    if x > 0:
        print("The number is positive")
    elif x < 0:
        print("The number is negative")
    else:
        print("The number is 0")

inspect_number(0)

