N = int(input())
k = int(input())

sum = N

for i in range (k):
    N = N*10
    sum = sum + N

print(sum)