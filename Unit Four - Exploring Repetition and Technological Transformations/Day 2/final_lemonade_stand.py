# This program is a single-player game which simulates players taking charge of their own business in a fictional town. 
# Before the start of each business day, players are given the day's weather forecast: Sunny, cloudy or rainy. 
# After receiving the weather report, players take charge of three factors that will affect business for the day: 
# The number of glasses of lemonade to make, the number of advertising signs, and the cost of lemonade per glass.

import random
import os
import time

assets = 200
day = 1
lemonade_cost = 2
total_profit = 0
daily_profit = 0
people_outside = 0
population = 0
weather = None

# Clear console function
def cls():
    os.system('cls' if os.name=='nt' else 'clear')


# Gets the population of the town 
def get_town_population():
    return random.randint(100, 300)

def print_lemonade_stand_intro():
    global population
    population = get_town_population()
    print(f"Welcome to Lemonade Stand! You are in a town with a population of {population} people.")
    print(f"The goal of the game is to make money by selling lemonade. ")
    print(f"Your current assets are ${assets/100:.2f} and the cost of lemonade is ${lemonade_cost/100}.")

# Randomly generates the weather based on probabilities for each weather condition
# The highest probability is sunny, then cloudy, then rainy 
def get_weather():
    weather_conditions = ["sunny", "cloudy", "rainy"]
    probabilities = {"sunny": 0.6, "cloudy": 0.3, "rainy": 0.1}
    return random.choices(weather_conditions, weights=probabilities.values())[0]

# This function gets the people who are outside on that day based on the weather 
def get_people_outside():
    if weather == "sunny":
        people_outside = round(random.uniform(population*0.4, population*0.6))
    elif weather == "rainy":
        people_outside = round(random.uniform(population*0.06, population*0.2))
    elif weather == "cloudy":
        people_outside = round(random.uniform(population*0.2, population*0.3))
    return people_outside

# This function checks if a string is an integer and returns two values 
def convert_string_to_integer(s):
    try:
        val = int(s)
    except ValueError:
        return False, 0
    return True, val

def get_glasses_made():
    # declaring assets as a global variable so its value can be changed inside the function 
    global assets

    while True:
        glasses_made = input("How many glasses of lemonade would you like to make? ")
        conversion_works, glasses_made = convert_string_to_integer(glasses_made)
        # Checks to see if the user input is an integer 
        if not conversion_works:
            print("Error: You did not enter an integer, please try again")
            continue # cycles back to the beginning of the loop 

        # Checks to see if the user has enough money 
        elif glasses_made * lemonade_cost > assets:
            print("You don't have enough money for this. ")
        
        elif glasses_made < 0:
            print("You cannot enter a negative number. ")
        else:
            break
    
    assets -= glasses_made * lemonade_cost
    return glasses_made

def get_num_of_signs():
    global assets
    while True:
        num_of_signs = input("How many advertising signs are you using (15 cents each)? ")
        conversion_works, num_of_signs = convert_string_to_integer(num_of_signs)
        # Checks to see if the user input is an integer 
        if not conversion_works:
            print("Error: You did not enter an integer, please try again")
            continue     
        
        # Checks to see if the user has enough money 
        elif num_of_signs * 15 > assets:
            print("You don't have enough money for this. ")
        
        elif num_of_signs < 0:
            print("You cannot enter a negative number. ")
        else:
            break
    
    assets -= num_of_signs * 15
    return num_of_signs
  

def get_charge_per_glass():
    while True:
        charge_per_glass = input("How much would you like to charge for each glass of lemonade (cents)? ")
        conversion_works, charge_per_glass = convert_string_to_integer(charge_per_glass)
        if not conversion_works:
            print("Error: You did not enter an integer, please try again")
        
        elif charge_per_glass < 0:
            print("You cannot enter a negative number. ")
        else:
            break
    return charge_per_glass

def get_player_input():
    global assets
    change = "yes"
    original_assets = assets
    # This loop checks if the user would like to change their answers 
    while change.lower() == "yes":
        assets = original_assets
        glasses_made = get_glasses_made()
        num_of_signs = get_num_of_signs()
        charge_per_glass = get_charge_per_glass()
        change = input("Would you like to change anything? ")

    return glasses_made, num_of_signs, charge_per_glass

# Calculate the customers at your stand based on the number of advertising signs inputted by the user
def calculate_customers_based_on_advertising(num_of_signs):
    global people_outside
    people_outside = get_people_outside()
    customers_based_on_advertising = num_of_signs * (people_outside * 0.2)
    if customers_based_on_advertising > people_outside:
        customers_based_on_advertising = people_outside
    return customers_based_on_advertising

# Calculates the number of customers who see the stand without seeing the advertising signs
def get_customers_who_see_stand():
    return random.randint(10, 30)

# Calculates the number of customers at the stand in total 
def get_customers_at_stand(num_of_signs):
    customers_based_on_advertising = calculate_customers_based_on_advertising(num_of_signs)
    customers_who_see_stand = get_customers_who_see_stand()
    if customers_based_on_advertising + customers_who_see_stand > people_outside:
        return people_outside
    else:
        return customers_based_on_advertising + customers_who_see_stand
        

# This function finds the glasses of lemonade sold using the number of customers at the stand. It finds 
# the number of customers who are interested in buying lemonade based on weather and the charge per glass.
# Ex. When the weather is sunny, even if the price per glass is higher, more people will be willing to buy lemonade 
# Returns the number of glasses sold.
def get_glasses_sold(customers_at_stand, charge_per_glass, glasses_made):
    customers_who_buy_lemonade = 0
    if weather == "sunny":
        if charge_per_glass <= 10:
            # if the charge per glass is less than or equal to 10 cents, every customer at the stand will buy a glass of lemonade
            customers_who_buy_lemonade = customers_at_stand
        elif 10 < charge_per_glass < 20:
            customers_who_buy_lemonade = round(customers_at_stand * 0.6)
        elif 20 <= charge_per_glass <= 30:
            customers_who_buy_lemonade = round(customers_at_stand * 0.5)
        elif 30 < charge_per_glass < 40:
            customers_who_buy_lemonade = round(customers_at_stand * 0.1)
        else:
            return 0 
    elif weather == "rainy":
        if charge_per_glass <= 10:
            customers_who_buy_lemonade = round(customers_at_stand * 0.3)
        elif 10 < charge_per_glass < 20:
            customers_who_buy_lemonade = round(customers_at_stand * 0.1)
        
        else:
            return 0 

    else:  # cloudy
        if charge_per_glass <= 10:
            customers_who_buy_lemonade = round(customers_at_stand * 0.5)
        elif 10 < charge_per_glass < 20:
            customers_who_buy_lemonade = round(customers_at_stand * 0.4)
        elif 20 <= charge_per_glass <= 30:
            customers_who_buy_lemonade = round(customers_at_stand * 0.2)
        
        else:
            return 0 

    # returns the minimum of glasses made and customers who buy lemonade because you cannot sell more than you have 
    return min(customers_who_buy_lemonade, glasses_made)




# This function simulates one day of the lemonade stand game. 
def execute_one_round_of_game():
    global day, lemonade_cost, assets, weather, total_profit
    cls()
    weather = get_weather()
    # Updates the cost of lemonade every 5 days by adding $0.02
    if day%5 == 0:
        lemonade_cost = lemonade_cost + 2
    print(f"\nDay {day}: Today, it is {weather}!")
    print(f"The cost of lemonade is ${lemonade_cost/100} and you have ${round(assets/100,2):.2f}.\n")

    glasses_made, num_of_signs, charge_per_glass =  get_player_input()

    customers_at_stand = get_customers_at_stand(num_of_signs)
    glasses_sold = get_glasses_sold(customers_at_stand, charge_per_glass, glasses_made)
    income = glasses_sold * charge_per_glass
    expenses = 15 * num_of_signs + lemonade_cost * glasses_made
    daily_profit = income - expenses
    assets += income
    total_profit += daily_profit

    print()
    print(f"Day {day}")
    print(f"{glasses_made} glasses made")
    print(f"{num_of_signs} signs made")
    print(f"{glasses_sold:.0f} glasses sold")
    print(f"${charge_per_glass / 100:.2f} per glass")

    print()
    print(f"Income: ${income / 100:.2f}")
    print(f"Expenses: ${expenses / 100:.2f}")
    print()
    print("Calculating profit ", end='')
    for i in range(4):
        print(".", end='')
        time.sleep(0.5)
    print(f"\nToday's Profit: ${round(daily_profit / 100,2):.2f}")
    print(f"Total Profit: ${round(total_profit / 100,2):.2f}")
    print(f"Assets: ${round(assets / 100,2):.2f}")
    day += 1


def main():
    # This is the main function of the game
    # It starts with an intro, and then continues to play rounds of the game until the user indicates they want to stop
    print_lemonade_stand_intro()
    
    keep_playing = True
    while keep_playing:
        # \n indicates new line
        response_to_keep_playing = input("\nWould you like to keep playing? ")
        if response_to_keep_playing.lower() == "no":
            keep_playing = False
        else:
            execute_one_round_of_game()

    end_game()


def end_game():
    print("See you next time!")
    


main()
