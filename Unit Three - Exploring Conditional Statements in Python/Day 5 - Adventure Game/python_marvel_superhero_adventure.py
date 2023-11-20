import random 

# This function allows the player to choose their Marvel superhero and returns the superhero's name and current health number 
def choose_superhero():
    print("Welcome to the Python Marvel Superhero Adventure! ")
    print("")
    print("First, pick your superhero.\n1. Iron Man\n2. Black Widow\n3. Black Panther.")
    superhero_name = input("Enter the number of your chosen superhero (1-3): ")
    # checks to make sure superhero_name is a valid number 
    while superhero_name not in ['1', '2', '3']:
        print("")
        print("Invalid choice. ")
        print("Pick your superhero.")
        print("1. Iron Man")
        print("2. Black Widow")
        print("3. Black Panther")
        superhero_name = input("Enter the number of your chosen superhero (1-3): ")
    
    current_health = random.randint(75, 100)
        
    return superhero_name, current_health

# Introduces the game and the chosen superhero 
def game_intro(superhero_name, current_health):
    print("")
    print("Welcome to the Marvel game!")
    if superhero_name == "1":
        print("You have chosen Iron Man as your superhero.")
    elif superhero_name == "2":
        print("You have chosen Black Widow as your superhero.")
    else:
        print("You have chosen Black Panther as your superhero.")
    
    print(f"Your current health is {current_health}.")
        
# Presents the player with a decision and returns the number of the decision they choose 
def make_decision():
    print("")
    print("A supervillain is causing trouble. Do you want to...")
    print("1. Confront the villain")
    print("2. Seek assistance from another hero")
    decision = input("Enter the number of your choice: ")
    while decision not in ["1", "2"]:
        print("")
        print("Invalid choice. Do you want to...")
        print("1. Confront the villain")
        print("2. Seek assistance from another hero")
        decision = input("Enter the number of your choice: ")
    return decision 

# Implements a superhero mission scenario and returns the damage and bonus pts
def superhero_mission(decision, current_health):
    # picks a random villain out of the three options
    random_villain = random.choice(["Ultron", "Thanos", "Loki"])
    print("")
    if decision == "1":
        print(f"You have chosen to confront the villain and you are in a face off against {random_villain}. Get ready to fight.")
        print("")
        if random_villain == "Ultron":
            damage_taken, bonus = confronting_ultron()

        elif random_villain == "Thanos":
            damage_taken, bonus = confronting_thanos()
        
        else:
            damage_taken, bonus = confronting_loki()
    
    else:
        random_hero = random.choice(["Captain America", "Thor", "Doctor Strange"])
        print(f"You have chosen to seek assistance.")
        if random_hero == "Captain America":
            damage_taken, bonus = captain_america_assistance(random_villain)

        elif random_hero == "Thor":
            damage_taken, bonus = thor_assistance(random_villain)

        else:
            damage_taken, bonus = doctor_strange_assitance(random_villain)

    return damage_taken, bonus

# This function is called from the superhero_mission() function if the random villain chosen is Ultron
# Presents the player with a decision and returns the damage_taken, bonus 
def confronting_ultron():
    print("Ultron has shown up with his army of robots. Do you choose to...")
    print("1. Try to beat them with all of your strength")
    print("2. Find a way to turn all of the robots off at once ")
    decision = input("Enter the number of your choice: ")
    while decision not in ["1", "2"]:
        print("")
        print("Invalid choice. Do you choose to...")
        print("1. Try to beat them with all of your strength")
        print("2. Find a way to turn all of the robots off at once ")
        decision = input("Enter the number of your choice: ")
    
    print("")
    if decision == "1":
        print("Uh oh. You could not conquer all of the robots. Ultron used his blasters to take you down. ")
        damage_taken = 110
        bonus = 0
        print(f"Damage taken: {damage_taken}")
        print(f"Bonus pts: {bonus}")
    
    else:
        print("Smart decision! You found the power source of the robot army to turn the robots off, defeating them with your brains.")
        damage_taken = 0
        bonus = 69
        print(f"Damage taken: {damage_taken}")
        print(f"Bonus pts: {bonus}")

    return damage_taken, bonus 

# This function is called from the superhero_mission() function if the random villain chosen is Thanos
# Presents the player with a decision and returns the damage_taken, bonus 
def confronting_thanos():
    print("Thanos has showed up with the infinity stones. Do you choose to...")
    print("1. Create a diversion and then take the infinity glove off his hand")
    print("2. Use your strength to beat him.")
    decision = input("Enter the number of your choice: ")

    while decision not in ["1", "2"]:
        print("")
        print("Invalid choice. Do you choose to... ")
        print("1. Create a diversion and then take the infinity glove off his hand")
        print("2. Use your strength to beat him.")
        decision = input("Enter the number of your choice: ")
    
    print("")
    if decision == "1":
        print("Great choice. He was heavily distracted by your diversion and you got the glove off of his hand just in time.")
        damage_taken = 10
        bonus = 79
        print(f"Damage taken: {damage_taken}")
        print(f"Bonus pts: {bonus}")
    
    else:
        print("Your strength could not beat the power of the infinity stones. Thanos captured you and took him to his ship.")
        damage_taken = 125
        bonus = 0
        print(f"Damage taken: {damage_taken}")
        print(f"Bonus pts: {bonus}")
    
    return damage_taken, bonus

# This function is called from the superhero_mission() function if the random villain chosen is Loki
# Presents the player with a decision and returns the damage_taken, bonus 
def confronting_loki():
    print("Loki has come from Asgard to New York City through a portal with an army of Frost Giants. Do you choose to...")
    print("1. Try to reason with him. ")
    print("2. Steal his magic staff which will let you close the portal.")
    decision = input("Enter the number of your choice: ")

    while decision not in ["1", "2"]:
        print("")
        print("Invalid choice. Do you choose to...")
        print("1. Try to reason with him. ")
        print("2. Steal his magic staff which will let you close the portal.")
        decision = input("Enter the number of your choice: ")
    
    print("")
    if decision == "1":
        print("You tried your best to reason with him but he would not listen. He has taken over New York City.")
        damage_taken = 120
        bonus = 0
        print(f"Damage taken: {damage_taken}")
        print(f"Bonus pts: {bonus}")
    
    else:
        print("You succesfully closed the portal and saved New York City from being destroyed!")
        damage_taken = 10
        bonus = 130
        print(f"Damage taken: {damage_taken}")
        print(f"Bonus pts: {bonus}")
    
    return damage_taken, bonus    

# This function is called from the superhero_mission() function if the random hero chosen is Captain America 
# Presents the player with a decision and returns the damage_taken, bonus 
def captain_america_assistance(random_villain):
    print(f"Captain America has agreed to help you beat the villain {random_villain}! Do you choose to...")
    print(f"1. Utilizie Captain America's leadership skills to rally a team of Avengers to beat {random_villain}") 
    print(f"2. Set a trap to capture {random_villain} at the Avengers Tower") 
    decision = input("Enter the number of your choice: ")

    while decision not in ["1", "2"]:
        print("")
        print("Invalid choice. Do you choose to...")
        print(f"1. Utilizie Captain America's leadership skills to rally a team of Avengers to beat {random_villain}") 
        print(f"2. Set a trap to capture {random_villain} at the Avengers Tower")
        decision = input("Enter the number of your choice: ")
    
    print("")
    if decision == "1":
        print(f"You did not have enough time to get a team together. {random_villain} has taken over the city.")
        damage_taken = 89
        bonus = 2
        print(f"Damage taken: {damage_taken}")
        print(f"Bonus pts: {bonus}")
    
    else:
        print(f"Using a skillfull plan, you were able to trap {random_villain}, saving the city. Good work!")
        damage_taken = 10
        bonus = 130
        print(f"Damage taken: {damage_taken}")
        print(f"Bonus pts: {bonus}")
    
    return damage_taken, bonus

# This function is called from the superhero_mission() function if the random hero chosen is Thor
# Presents the player with a decision and returns the damage_taken, bonus 
def thor_assistance(random_villain):
    print(f"Thor has agreed to help you beat the villain {random_villain}! Do you choose to...")
    print(f"1. Help Thor harness the power of Mjolnir, his hammer, to weaken {random_villain}.") 
    print(f"2. Tap into Thor's knowledge of Asgardian principles to come up with an effective strategy to beat {random_villain}.") 
    decision = input("Enter the number of your choice: ")

    while decision not in ["1", "2"]:
        print("")
        print("Invalid choice. Do you choose to...")
        print(f"1. Help Thor harness the power of Mjolnir, his hammer, to weaken {random_villain}.") 
        print(f"2. Tap into Thor's knowledge of Asgardian principles to come up with an effective strategy to beat {random_villain}.") 
        decision = input("Enter the number of your choice: ")
    
    print("")
    if decision == "1":
        print(f"Great work. The power of Thor's hammer was strong enough to defeat {random_villain}! You have saved the city.")
        damage_taken = 10
        bonus = 132
        print(f"Damage taken: {damage_taken}")
        print(f"Bonus pts: {bonus}")
    
    else:
        print(f"Unfortunately, Thor's knowledge was not useful in this situation. {random_villain} has taken over the city.")
        damage_taken = 120
        bonus = 0
        print(f"Damage taken: {damage_taken}")
        print(f"Bonus pts: {bonus}")
    
    return damage_taken, bonus    

# This function is called from the superhero_mission() function if the random hero chosen is Doctor Strange 
# Presents the player with a decision and returns the damage_taken, bonus 
def doctor_strange_assitance(random_villain):
    print(f"Doctor Strange has agreed to help you beat the villain {random_villain}! Do you choose to...")
    print(f"1. Use the time stone Doctor Strange possesses to slow {random_villain} down.") 
    print("2. Help Doctor Strange reverse time to undo the damage that has already been done to the city.") 
    decision = input("Enter the number of your choice: ")

    while decision not in ["1", "2"]:
        print("")
        print("Invalid choice. Do you choose to...")
        print(f"1. Use the time stone Doctor Strange possesses to slow {random_villain} down.") 
        print("2. Help Doctor Strange reverse time to undo the damage that has already been done to the city.") 
        decision = input("Enter the number of your choice: ")
    
    print("")
    if decision == "1":
        print(f"Great work. Slowing {random_villain} down was just enough to save the city in time!")
        damage_taken = 10
        bonus = 132
        print(f"Damage taken: {damage_taken}")
        print(f"Bonus pts: {bonus}")
    
    else:
        print(f"Unfortunately, the spell went wrong and you have created a time loop.")
        damage_taken = 120
        bonus = 0
        print(f"Damage taken: {damage_taken}")
        print(f"Bonus pts: {bonus}")
    
    return damage_taken, bonus

# Calculates the remaining health after a mission from damage_taken and bonus points
def manage_health(current_health, damage_taken, bonus):
    remaining_health = current_health - damage_taken
    remaining_health = remaining_health + bonus
    return remaining_health

# Displays the player's final score and the message indicating the outcome of their adventure
def game_completition(remaining_health):
    print("")
    if remaining_health < 0:
        print("Good try. Your health is below 0 so you have died.")
    
    else:
        print(f"Good game! Your remaining health is {remaining_health}. You survive.")

# Main function that calls the other game functions
def main():
    superhero_name, current_health = choose_superhero()
    game_intro(superhero_name, current_health)
    decision = make_decision()
    damage_taken, bonus = superhero_mission(decision, current_health)
    remaining_health = manage_health(current_health, damage_taken, bonus)
    game_completition(remaining_health)

main()




    




