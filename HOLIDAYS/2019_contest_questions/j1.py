apple_threes = int(input())
apple_twos = int(input())
apple_ones = int(input())

banana_threes = int(input())
banana_twos = int(input())
banana_ones = int(input())

apple_pts = (apple_threes*3) + (apple_twos*2) + apple_ones
banana_pts = (banana_threes*3) + (banana_twos*2) + banana_ones

if apple_pts > banana_pts:
    print("A")

elif banana_pts > apple_pts:
    print("B")

else:
    print("T")

