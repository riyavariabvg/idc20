average = 12.6584930

print(f"{average:.2f}") # rounds to 2 decimal places

print(f"{average:.3f}")

number = 6.1
print(f"{number:.2f}")

integer = 6
print(f"{integer:.2f}")


math_test_mark = 34
math_test_total = 45

math_average = math_test_mark/math_test_total

print(f"{math_average}") #0.755555555
print(f"{math_average:.1%}") # automatically multiplies by 100 and rounds to 1 decimal place - adds the percent symbol as well

x= 54.5894303849
print(f"{x:.2f}")
print(f"{x:.5}")
print(f"{x:.1}") # 5e+01 -> scientific notation 5 x 10^1

# when we don't put the f, it includes how many spots that we are including for the whole number

y = 5.5859238093840
print(f"{y:.2}")     # 6e+00 -> scientific notation 6 x 10^0