def caught_speeding(speed, is_birthday):
    if is_birthday:
        if speed <=65:
            return "No Ticket"
        elif 66 <= speed <= 85:
            return "Small Ticket"
        else:
            return "Big Ticket"
    
    else:
        if speed <= 60:
            return "No Ticket"
        
        elif 61 <= speed <=80:
            return "Small Ticket"
        
        else:
            return "Big Ticket"

def not_string(s):
    lower_s = s.lower()
    if lower_s[0:3] == "not":
        return s
    else:
        return "not" + s

def squirrel_play(temp, is_summer):
	if is_summer:
		if 60<= temp <= 100:
			return True
	else:
		if 60 <=temp <= 90:
			return True
	
	return False

def in2020(a,b):
    if 10<=a<=20 or 10<=b<=20:
        return True
    else:
        return False

def theEnd(string, front: bool):
     if len(string) > 0:
          if front:
               return string[0]
          else:
               return string[len(string)-1]
     else:
          return "Empty"
    
print(theEnd("", False))

