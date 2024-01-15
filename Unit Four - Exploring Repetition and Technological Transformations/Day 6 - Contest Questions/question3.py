word = input()
max = 1
def palindrome(word):
    backwards = ""
    forwards = word
    for i in range(len(forwards)-1, -1, -1):
        backwards += forwards[i]
 
    if backwards == forwards:
        return True
    else:
        return False
 
for i in range(len(word)):
    for j in range(len(word)):
        if j < i:
            j = i 
        substring = word[i:j+1]
        if palindrome(substring) and len(substring) > max:
            max = len(substring)

print(max)

