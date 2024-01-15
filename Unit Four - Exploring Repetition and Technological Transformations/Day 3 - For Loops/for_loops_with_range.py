
# add the numbers from start to finish and return the total
def example_two(start, finish):
    total = 0
    for i in range(start,finish+1):
        total += i

    return total

#print numbers from 20 to 2 and go down by 2s
def example_three():
    for i in range(20, 0, -2):
        print(i)

#print a string backwards
def example_four(str):
    result = ""
    for i in range(len(str)-1, -1, -1):
        result += str[i]
    
    print(result)


#grab substrings of length n and print them to the screen.
def example_five(str, n):
    for i in range(0,len(str)-n+1):
        print(str[i:i+n])


#count how many times the second word appears in the first word
def example_six(str1, str2):
    if len(str2) > len(str1):
        return 0

    result = 0

    for i in range(len(str1)-len(str2)+1):
        if str1[i:i+len(str2)] == str2:
            result += 1
    
    return result



print(example_six("dogcargodogdog", "dog"))