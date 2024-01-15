def count_characters(s1, s2):
    count = 0
    for i in s1:
        if i == s2:
            count += 1

    return count

def reverse_string(s):
    result = ""
    for i in range(len(s)-1, -1, -1):
        result += s[i]
    
    return result

def remove_vowels(s):
    result = ""
    for i in s:
        if i not in ["a", "e", "i", "o", "u"]:
            result += i
    return result
    
def character_repetition(s, n):
    result = ""
    for i in s:
        result += i*n
    
    return result

def title_case(s):
    previous_space = False
    first_letter = True
    result = ""
    for i in s:
        if first_letter:
            first_letter = False
            i = i.upper()
            result +=i
        elif previous_space:
            previous_space = False
            i = i.upper()
            result += i
        
        elif i == " ":
            previous_space = True
            result +=i
        
        else:
            result += i
    return result  

# print(count_characters("hello", "l"))
# print(reverse_string("hello"))
# print(remove_vowels("happiness"))
# print(character_repetition("coke", 7))
# print(title_case("once upon a time"))

def num_of_times(str1, str2):
    len_str2 = len(str2)
    count = 0
    #if len(str2) > len(str1):
     #   return 0
    
    
    for i in range (len(str1)):
        if str1[i: i+len_str2] == str2:

            count = count + 1

    return count 
                

print(num_of_times("hellohel", "hel"))


def title_case_2(s):
    new_str = ""
    for i in range (len(s)):
        if i == 0:
            new_str += s[i].upper()
        elif s[i-1] == " ":
            new_str += s[i].upper()
        else:
            new_str += s[i].lower()
    return new_str

print(title_case_2("hellO mY name is riya"))
print(num_of_times("hello", "hello"))