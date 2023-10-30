def my_first_function():
    print("Hello ICD20 Class")
    print("Goodbye ICD20")

def hello(times):
    return None

print(hello(3))

import math
def calculate_circle_area(radius):
    area = math.pi*radius**2
    return abs(area)



print(calculate_circle_area(1))


def format_sales(name, amount, price):
    return f"You purchased {amount} {name} for a total of ${price:.2f}."

print(format_sales('Apples', 67, 390))

print(5**3.4)


def front_back(str):
  front = str[0]
  return front

print(front_back("hi"))

def calculate_rec_area(length, width):
    area = length*width
    return f"{area:.2f}"

print(calculate_rec_area(5, 7))

