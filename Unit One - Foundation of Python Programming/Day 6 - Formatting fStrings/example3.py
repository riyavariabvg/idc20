import math

average = 67.4465456

print(f"{average}")
print(f"{average:.2f}")
print(f"{average:>20}")
print(f"{average:>20.2f}") # need to do the width/allignment first and deciaml places after
#print(f"{average:.2f>20}") # DOES NOT WORK


# print PI with 2 decimal places alliged right with a width of 10
print(math.pi)
print(f"{math.pi:>10.2f}")


