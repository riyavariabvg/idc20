def my_first_function():
    print("Hello ICD20 Class")
    print("Goodbye ICD20")

my_first_function()

def useless():
    print(1)
    print(2)
    print(3)


print(4)

useless()

print(useless)

# factorial recursion
def factorial(n):
    if n == 0:
        return 1
    
    elif n == 1:
        return 1
    
    elif n > 1:
        current_product = n*factorial(n-1)
        return current_product
    
print(factorial(3))
        
        






