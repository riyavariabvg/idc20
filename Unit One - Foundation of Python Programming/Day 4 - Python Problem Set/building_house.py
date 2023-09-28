import math

wall_length = float(input("Enter the length of one wall (in metres): "))
wall_width = float(input("Enter the width of one wall (in metres): "))
house_height = float(input("Enter the height of the house (in metres): "))
cost_per_brick = float(input("Enter the cost per brick (in dollars): "))
brick_length = float(input("Enter the length of a standard brick (in metres): "))
brick_width = float(input("Enter the width of a standard brick (in metres): "))
brick_height = float(input("Enter the height of a standard brick (in metres): "))
house_surface_area = house_height * 2 * (wall_width + wall_length)
brick_area = brick_length * brick_width
num_of_bricks = math.ceil(house_surface_area/brick_area)
total_cost = num_of_bricks * cost_per_brick

print("House Details: ")
print(f"- Wall Surface Area: {house_surface_area} square metres")
print(f"- Bricks Required: {num_of_bricks} bricks")
print(f"- Total Cost of Bricks: ${total_cost}")


