drink = float(input("Enter the cost of your drink: "))
appetizer = float(input("Enter the cost of your appetizer: "))
entrée = float(input("Enter the cost of your entrée: "))
dessert = float(input("Enter the cost of your dessert: "))
tip_rate = float(input("Enter the tip rate (as a percentage, e.g., 15%): "))
subtotal = drink + appetizer + entrée + dessert
tip = subtotal * tip_rate/100
total = subtotal + tip

print("Bill Summary:")
print(f"Subtotal: ${round(subtotal,2)}")
print(f"Tip ({tip_rate}%): {tip}")
print(f"Total Cost: ${round(total,2)}")
