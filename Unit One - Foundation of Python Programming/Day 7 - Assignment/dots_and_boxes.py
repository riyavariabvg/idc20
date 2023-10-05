# This is a dots and boxes score tracker that allows you to keep track of your results while playing the game "Dots and Boxes".
# You will play against five different opponents in your class
# The grid is 7x7 (36 boxes in total)
# The program will calculate various statistics, including the percentage of boxes created and the percentage of points received.

name = input("Enter your name: ")

# User inputs data for all 5 dots and boxes games 
print()
print("Game #1:")
opponent1_name = input("Opponent's Name: ")
game1_my_pts = int(input("Your Points: "))
game1_opponent_pts = int(input("Opponent's Points: "))

print()
print("Game #2:")
opponent2_name = input("Opponent's Name: ")
game2_my_pts = int(input("Your Points: "))
game2_opponent_pts = int(input("Opponent's Points: "))

print()
print("Game #3:")
opponent3_name = input("Opponent's Name: ")
game3_my_pts = int(input("Your Points: "))
game3_opponent_pts = int(input("Opponent's Points: "))

print()
print("Game #4:")
opponent4_name = input("Opponent's Name: ")
game4_my_pts = int(input("Your Points: "))
game4_opponent_pts = int(input("Opponent's Points: "))

print()
print("Game #5:")
opponent5_name = input("Opponent's Name: ")
game5_my_pts = int(input("Your Points: "))
game5_opponent_pts = int(input("Opponent's Points: "))

# Calculates the total number of points you recieved across all 5 games 
my_pts_total = game1_my_pts + game2_my_pts + game3_my_pts + game4_my_pts + game5_my_pts

# Calculates the total number of points opponent recieved across all 5 games
opponent_pts_total = game1_opponent_pts + game2_opponent_pts + game3_opponent_pts + game4_opponent_pts + game5_opponent_pts

# Calculates the percentage of boxes you created out of the maximum possible boxes across all 5 games
# There are 180 boxes in total (36*5)
# The percentage will be in decimal form 
my_percentage_of_total_pts = my_pts_total/(36*5)


print()
print()
print("Dots and Boxes Score Tracker")
print()
print(f"Player's Name: {name}")
print()

# Creating a table to collect all of the information
print(f"{'Opponent':<14}{'Your Points':>11}{'Opponent Points':>20}{'Box %':>12}")
print("=========================================================")
print(f"{opponent1_name:<14.14}{game1_my_pts:>11}{game1_opponent_pts:>20}{(game1_my_pts/36):>12.2%}")
print(f"{opponent2_name:<14.14}{game2_my_pts:>11}{game2_opponent_pts:>20}{(game2_my_pts/36):>12.2%}")
print(f"{opponent3_name:<14.14}{game3_my_pts:>11}{game3_opponent_pts:>20}{(game3_my_pts/36):>12.2%}")
print(f"{opponent4_name:<14.14}{game4_my_pts:>11}{game4_opponent_pts:>20}{(game4_my_pts/36):>12.2%}")
print(f"{opponent5_name:<14.14}{game5_my_pts:>11}{game5_opponent_pts:>20}{(game5_my_pts/36):>12.2%}")
print("=========================================================")

# Summary
print()
print("Summary:")
print(f"Total Points: {my_pts_total}")
print(f"Total Opponent Points: {opponent_pts_total}")
print(f"Percentage Points Recieved: {my_percentage_of_total_pts:.2%}")


