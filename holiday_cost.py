# Calculate user's total holiday cost

# Set some variables
hotel_price = 150
car_cost = 50
city_costs = {
        "Paris": 250,
        "Milan": 500,
        "Rome": 600,
        "Madrid": 400,
    }
 
city_list = ["Paris", "Milan", "Rome", "Madrid"]

# Input from user to establish destination
city_flight = str(input(f"Please input your destination - {" ".join(str(x) for x in city_list)}: "))

# Error loop to get correct input if user enters 
# city option not in city_list or has a spelling error
while city_flight not in city_list:
    print(f"{city_flight} is not a valid option.")

    city_flight = str(input(f"Please input your destination - {" ".join(str(x) for x in city_list)}: "))

# Input from user for number of nights in chosen city
num_nights = int(input(f"Please enter the number of nights you will be stating at your hotel in {city_flight}: "))

# Input from user for number of days to hire a car
rental_days = int(input("Please enter the number of days you will be hiring a car: "))

# Defining the functions
# Cost of hotel per night * number of nights
def hotel_cost(num_nights):
    total_hotel_cost = num_nights * hotel_price
    print()
    print(f"The cost of your hotel stay is £{total_hotel_cost} for {num_nights} days")
    return total_hotel_cost
    
    
# Cost of plane ticket based on destination
# Costs are defined above for different cities
def plane_cost(city_flight):

    if city_flight == "Paris":
        print(f"The cost of your flight to {city_flight} is £{city_costs['Paris']}")
    elif city_flight == "Milan":
        print(f"The cost of your flight to {city_flight} is £{city_costs['Milan']}")
    elif city_flight == "Madrid":
        print(f"The cost of your flight to {city_flight} is £{city_costs['Madrid']}")
    else:
        print(f"The cost of your flight to {city_flight} is £{city_costs['Rome']}")
# Returns cost based on city
    return city_costs.get(city_flight)


# Cost of car hire based on number of days
def car_rental(rental_days):
    total_car_cost = rental_days * car_cost
    print(f"The cost of your car rental is £{total_car_cost} for {rental_days} days")
    return total_car_cost


# Total cost of the holiday - ticket + hotel + car rental
def holiday_cost(num_nights, city_flight, rental_days):
    total_hotel = hotel_cost(num_nights)
    total_flight = plane_cost(city_flight)
    total_car_rental = car_rental(rental_days)
    total = total_hotel + total_flight + total_car_rental
    return total

total = holiday_cost(num_nights, city_flight, rental_days)

# Print out the total cost of the trip - ticket + hotel + car rental
print()
print(f"The total cost of your holiday is £{total}")
print()
print("Enjoy your trip!")