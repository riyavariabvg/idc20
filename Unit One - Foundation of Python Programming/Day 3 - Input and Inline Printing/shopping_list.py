price1 = float(input("Enter the price of the first item: "))
price2 = float(input("Enter the price of the second item: "))
price3 = float(input("Enter the price of the third item: "))

# calculating total
total = round((price1 + price2 + price3) * 1.13, 2)
print(f"The total cost with tax is: {total}")