# print("="*10)

# print("Hello"*9)

# print("-"*45)

def sample_function():
    return 7, 8, 9


a,b,c = sample_function()
print(a)
print(c)

print(sample_function()) # (7, 8, 9)

d = sample_function()

n = d * 5
print(n)
