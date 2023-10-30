def middleThree(str):
    len_str = int((len(str) - 3)/2)
    return str[len_str:len_str + 3]


def lastChars(str1, str2):
    str1_letter = str1[0]
    str2_letter = str2[len(str2) -1]
    return str1_letter + str2_letter

def lastTwo(str):
    last_letter = str[len(str)-1]
    second_last = str[len(str) -2]
    first_part = str[0:len(str)-2]
    return first_part + last_letter + second_last

def hollow_square(length, width):
    pass
    

