distance = float(input("Enter the distance of the trip (km): "))
fuel_efficiency = float(input("Enter the fuel efficiency (km/L): "))
cost_per_litre = float(input("Enter the current price of fuel per litre ($): "))
passengers = int(input("Enter the number of passengers in the vehicle: "))

fuel_needed = distance/fuel_efficiency
total_cost = fuel_needed*cost_per_litre
cost_per_passenger = total_cost/passengers

print(f"The total amount of fuel needed for the trip is {round(fuel_needed,2)} litres.")
print(f"The total cost of fuel for the trip is ${round(total_cost,2)}")
print(f"The cost of fuel per passenger is ${cost_per_passenger}.")