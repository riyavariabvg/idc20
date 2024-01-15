time = input()
time_in_integers = [int(time_int) for time_int in time.split(':')]

hour = time_in_integers[0]
min = time_in_integers[1]
current_time = hour*60 + min
end_time = 0
remaining_time = 0
rush_hour_next = None
day_next = False
period = None

if 0 <= current_time < 420:
    if 420 - current_time < 120:
        remaining_time = 120 - (420 - current_time)
        period = 420
        rush_hour_next = True
    else:
        end_time = current_time + 120

elif 420 <= current_time < 600:
    remaining_time = 120 - ((600-current_time)/2)
    period = 600
    rush_hour_next = False
        
elif 600 <= current_time < 900:
    if 900 - current_time < 120:
        remaining_time = 120 - (900 - current_time)
        period = 900
        rush_hour_next = True
    else:
        end_time = current_time + 120

elif 900 <= current_time < 1140:
    remaining_time = 120 - ((1140-current_time)/2)
    period = 1140
    rush_hour_next = False

elif 1140 <= current_time < 1440:
    if 1440 - current_time < 120:
        remaining_time = 120 - (1440 - current_time)
        period = 1440
        day_next = True
    else:
        end_time = current_time + 120

if end_time == 0:
    if day_next:
        end_time = remaining_time
    
    else:
        if rush_hour_next:
            end_time = period + (remaining_time*2)

        else:
            end_time = period + remaining_time


end_hour = int(end_time/60)
end_min = int(end_time % 60)

end_hour = str(end_hour)
end_min = str(end_min)
if len(str(end_hour)) == 1:
    end_hour = "0" + str(end_hour)


if len(str(end_min)) == 1:
    end_min = "0" + str(min)


print(end_hour + ":" + end_min)


    






