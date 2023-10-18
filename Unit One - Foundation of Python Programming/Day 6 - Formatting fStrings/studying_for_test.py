product1 = "Apple"
price1 = 0.99
discount1 = 0.1

product2 = "Orange"
price2 = 1.29
discount2 = 0.15

product3 = "Banana"
price3 = 0.49
discount3 = 0.05

discounted_price1 = (1 - discount1) * price1
discounted_price2 = (1 - discount2) * price2
discounted_price3 = (1 - discount3) * price3

#Creating table
print(f"{'Product':<15}{'Price($)':>10}{'Discount':>15}")
print(f"{product1:<15}{'$' + str(price1):>10}{discount1:>15}")

number = 42
formatted_str = f"Number: {number:06}"  # Outputs "Number: 00042"
print(formatted_str)

num1 = 5
num2 = 7
print("The sum of" +str(num1)+ "and")

print(3*7)




