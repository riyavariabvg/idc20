import math

def multiply(num1, num2): 
    print(f"The product is {num1*num2}.")


def calculate_cylinder_volume(radius, height):
    volume = math.pi*(radius**2)*height
    print(f"The volume is {volume} cubic units.")

def print_triangle(character):
    print(f"{character:^24}")
    print(f"{character:^12}{character:^12}")
    print(f"{character:^8}{character:^8}{character:^8}")

def say_hello(name):
    print(f"Hello, {name}! Nice to meet you.")

def calculate_circle_area(radius):
    print(f"The area of the cirlce is {math.pi*(radius**2)}")

def print_square(character):
    print(f"{character}{character}{character}{character}")
    print(f"{character}{character}{character}{character}")
    print(f"{character}{character}{character}{character}")
    print(f"{character}{character}{character}{character}")

def calculate_power(num, power):
    print(f"{num} to the power of {power} is {num**power}.")

def calculate_triangle_area(base, height):
    print(f"The area of the triangle is {base*height/2}")






