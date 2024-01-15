duration = int(input())
hour = "12"
min = "00"
count = 0



def get_next_time_sequence():
    global min, hour
    sequence = []
    if int(min) == 59:
        if int(hour) == 12:
            hour = str(1)
            min = "00"
        else:
            hour = str(int(hour) + 1)
            min = "00"
    
    else:
        min = str(int(min) + 1)
    
    if len(min) == 1:
        min = "0" + min
    
    for i in hour:
        sequence.append(int(i))
    
    for i in min:
        sequence.append(int(i))
    
    return sequence


def is_arithmatic(sequence):
    value = sequence[1] - sequence[0]
    next = sequence[0]
    arithmatic = None
    for i in sequence:
        if next == i:
            arithmatic = True
            next = i + value
        else:
            return False
    
    if arithmatic:
        return True


for i in range(duration):
    sequence = get_next_time_sequence()
    check_arithmatic = is_arithmatic(sequence)
    if check_arithmatic:
        count = count + 1


print(count)

    
            




