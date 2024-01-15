line1 = input().split(" ")
line2 = input().split(" ")
line3 = input().split(" ")
line4 = input().split(" ")
magic = True

line1_list = []
line2_list = []
line3_list = []
line4_list = []

for i in range(4):
    line1_list.append(int(line1[i]))
    line2_list.append(int(line2[i]))
    line3_list.append(int(line3[i]))
    line4_list.append(int(line4[i]))

sum1 = sum(line1_list)
sum2 = sum(line2_list)
sum3 = sum(line3_list)
sum4 = sum(line4_list)
main_sum = sum1
column_sums = []

for i in range(4):
    sum = line1_list[i] + line2_list[i] + line3_list[i] + line4_list[i]
    column_sums.append(sum)


column_sums.append(sum1)
column_sums.append(sum2)
column_sums.append(sum3)
column_sums.append(sum4)


for i in column_sums:
    if i == main_sum:
        magic = True
    else:
        magic = False
        break

if magic == True:
    print("magic")

else:
    print("not magic")


    

        

    

