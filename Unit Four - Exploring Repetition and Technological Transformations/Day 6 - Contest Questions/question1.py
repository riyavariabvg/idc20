wins = 0 

for i in range(6):
    stat = input()
    if stat == "W":
        wins +=1
    
if wins == 5 or wins == 6:
    print(1)

elif wins == 3 or wins == 4:
    print(2)

elif wins == 1 or wins == 2:
    print(3)

else:
    print(-1)