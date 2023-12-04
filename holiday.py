# Define a dictionary with information about cities as key, and
# a list value including flight cost, hotel cost, and car rental cost per day.
cities = {
    "AMSTERDAM": [420, 95.20, 45.80],
    "ATHENS": [320, 72.50, 40.20],
    "AUCKLAND": [950, 110.20, 55.60],
    "BARCELONA": [320, 76.45, 38.20],
    "BANGKOK": [850, 52.30, 35.15],
    "BEIJING": [1000, 68.54, 32.45],
    "BERLIN": [245, 60.81, 59.57],
    "BRUSSELS": [380, 98.60, 50.40],
    "BUCHAREST": [280, 54.30, 35.80],
    "BUENOS AIRES": [870, 78.55, 49.80],
    "CAIRO": [550, 45.70, 30.40],
    "CALGARY": [720, 120.50, 58.30],
    "CAPE TOWN": [999, 79.64, 54.29],
    "CARACAS": [450, 60.20, 35.60],
    "CEBU": [720, 25.18, 15.05],
    "CHICAGO": [720, 140.20, 65.80],
    "COPENHAGEN": [450, 110.20, 55.60],
    "DAKAR": [680, 92.80, 48.60],
    "DALLAS": [820, 130.40, 68.20],
    "DUBAI": [780, 108.45, 50.04],
    "DUBLIN": [380, 105.40, 48.60],
    "EDINBURGH": [450, 89.60, 42.30],
    "HONG KONG": [1100, 112.80, 55.50],
    "ISTANBUL": [280, 80.60, 45.30],
    "JAKARTA": [600, 45.20, 32.10],
    "JOHANNESBURG": [888, 75.11, 56.57],
    "KUALA LUMPUR": [700, 65.30, 38.40],
    "LIMA": [520, 70.20, 42.60],
    "LISBON": [340, 76.80, 42.50],
    "LONDON": [700, 173.94, 77.30],
    "LOS ANGELES": [980, 164.34, 88.45],
    "LUXEMBOURG": [320, 110.80, 55.40],
    "MADRID": [380, 94.50, 48.20],
    "MANILA": [780, 30.67, 20.33],
    "MARRAKECH": [420, 65.20, 38.90],
    "MELBOURNE": [1100, 118.18, 60.07],
    "MEXICO CITY": [520, 80.20, 45.60],
    "MIAMI": [950, 140.50, 72.80],
    "MONTREAL": [800, 120.40, 65.20],
    "MOSCOW": [590, 65.80, 40.60],
    "MUMBAI": [450, 25.27, 18.08],
    "MUNICH": [380, 95.60, 50.20],
    "NAIROBI": [600, 65.40, 38.20],
    "NEW DELHI": [520, 35.80, 25.60],
    "NEW YORK": [675, 183.47, 70.12],
    "OSAKA": [1550, 96.20, 52.80],
    "PARIS": [250, 98.15, 61.24],
    "PRAGUE": [310, 68.50, 38.20],
    "RIYADH": [670, 110.40, 55.90],
    "RIO DE JANEIRO": [960, 66.33, 41.20],
    "ROME": [175, 64.24, 55.64],
    "SAN FRANCISCO": [950, 160.70, 75.40],
    "SAO PAULO": [950, 98.40, 60.20],
    "SEOUL": [1300, 78.90, 45.60],
    "SINGAPORE": [950, 110.50, 55.60],
    "STOCKHOLM": [470, 102.80, 48.70],
    "SYDNEY": [1200, 126.33, 62.48],
    "TEL AVIV": [480, 102.30, 48.50],
    "TOKYO": [1700, 92.34, 58.45],
    "TORONTO": [875, 125.31, 68.68],
    "VIENNA": [320, 87.60, 42.30],
    "VANCOUVER": [890, 128.40, 68.20],
    "WASHINGTON, D.C.": [720, 130.20, 68.60],
}

# Variables for dictionary indices being constant
city_cost_index = 0
hotel_cost_index = 1
car_cost_index = 2


# Function to calculate hotel cost based on the number of nights.
def hotel_cost(num_nights):
    return round(num_nights * cities[city_flight][hotel_cost_index], 2)
    
# Function to get plane cost for a given city.
def plane_cost(city_flight):
    return cities[city_flight][city_cost_index]

# Function to calculate car rental cost based on the number of days.    
def car_rental(rental_days):
    return round(rental_days * cities[city_flight][car_cost_index], 2)

# Function to calculate total cost of the holiday.
def holiday_cost(num_nights, rental_days):
    total_cost = round(hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days), 2)
    return total_cost


print("\n\n________________________________________________________________")

print("Welcome to EasyBook Dream Holiday Travel Agency")
print("________________________________________________________________")

print("\nExplore the world with us and make your dream holiday a reality!")
print("Book your trip now and embark on the adventure of a lifetime!")

print("\n________________________________________________________________")

# List the cities we offer to our clients
print("\nCities we cater:")
for city in cities:
    print(f"- {city}")

print("________________________________________________________________")

# Get user input for destination city, number of nights, and rental days.
# Error handling for city flight input
while True:

    city_flight = input("\nPlease enter city desitnation: ").upper().strip()

    if city_flight.isalpha() or city_flight in cities:
        
        # If the city is not in the dictionary, print message.
        if city_flight not in cities:
            
            print("\t\t\t______________________________________________________")
            print("\n\t\t\t Apolgies! We don't offer that destination yet.")
            print("\t\t\t______________________________________________________\n")
            continue

        else:
            break
            
    else:
        print("Invalid input! Please use only alphabets.")
        continue

# Error handling for num nights input
while True:
    
    try:

        num_nights = int(float(input("\nPlease enter how many nights you wish to stay: ")))
        
        # Check if user does not want to book a hotel for the trip
        if num_nights == 0:
            
            # Error handling for choice input
            while True:
                
                choice = input("\nAre you sure you don't want to book a hotel for this trip?(y/n): ").lower().strip()
                
                if choice in ["y", "n"]:
                    break
                
                else:
                    print("Please choose between (y/n!)")
                    continue
            
            if choice == "y":
                break

        elif num_nights < 0:
            print("Please enter a positive value!")
        
        else:
            break

    except Exception:
        print("Invalid input! Please enter a numeric value.")

# Error handling for rental days input
while True:
    
    try:

        rental_days = int(float(input("\nPlease enter how many days you want to hire a car: ")))
        
        # Check if user does not want to hire a car for the trip
        if rental_days == 0:
            
            # Error handling for choice input
            while True:
                
                choice = input("\nAre you sure you don't want to hire a car for this trip?(y/n): ").lower().strip()
                
                if choice in ["y", "n"]:
                    break
                
                else:
                    print("Please choose between (y/n!)")
                    continue
            
            if choice == "y":
                break

        elif rental_days < 0:
            print("Please enter a positive value!")
        
        else:
            break

    except Exception:
        print("Invalid input! Please enter a numeric value.")


# Display details and cost breakdown of the user's holiday plan.
print("\n\n\t\t\t______________________________________________________")

print(f"\n\t\t\t Flight cost to {city_flight} is £{plane_cost(city_flight)}\n")

if num_nights == 0:
    print(f"\t\t\t Hotel cost: N/A")
else:
    print(f"\t\t\t Hotel cost: £{hotel_cost(num_nights)} for {num_nights} nights at a rate of £{cities[city_flight][hotel_cost_index]}")

if rental_days == 0:
    print(f"\t\t\t Car hire cost: N/A")
else:
    print(f"\t\t\t Car hire cost: £{car_rental(rental_days)} for {rental_days} days at a rate of £{cities[city_flight][car_cost_index]}")

print(f"\n\t\t\t The total cost for your holiday is: £{holiday_cost(num_nights, rental_days)}")
print("\n\t\t\t Thank you for booking with us!")

print("\t\t\t______________________________________________________\n")