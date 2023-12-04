# Solo-Travel-Agency

EasyBook Solo Dream Holiday Travel Agency Overview The provided Python script represents a simplified booking system for EasyBook Dream Holiday Travel Agency. The agency offers flights, hotel accommodations, and car rentals for various cities around the world. Users can input their desired destination city, the number of nights they wish to stay, and the number of days they want to hire a car. The script then calculates and displays the total cost of the holiday, including flight, hotel, and car rental expenses.

Key Components

cities Dictionary This dictionary contains information about different cities, including the cost of a flight, hotel, and car rental per day. The cities and their corresponding costs are defined as key-value pairs.

Functions hotel_cost(num_nights): Calculates the hotel cost based on the number of nights the user wishes to stay.

plane_cost(city_flight): Retrieves the flight cost for the specified destination city.

car_rental(rental_days): Calculates the car rental cost based on the number of days the user wants to hire a car.

holiday_cost(num_nights, rental_days): Computes the total cost of the holiday by summing up the flight, hotel, and car rental costs.

User Input and Error Handling The script prompts users to input their destination city, the number of nights they want to stay, and the number of days they want to hire a car. It includes error handling mechanisms to ensure valid inputs and provides users with the option to skip booking a hotel or car.

Output The script outputs a detailed cost breakdown for the user's holiday plan, including the flight cost, hotel cost (if applicable), car hire cost (if applicable), and the total cost. The information is presented in a user-friendly format.

How to Use Run the script. Enter the desired destination city, number of nights for hotel stay, and number of days for car rental when prompted. Review the cost breakdown and total cost for the holiday. Optionally, skip booking a hotel or car by entering 0 for the respective duration. Note The script uses a dictionary (cities) to store information about cities and costs. Make sure to update this dictionary with accurate information as needed. The code is designed for simplicity and may require further enhancements for a production environment, such as data validation, exception handling, and integration with a booking system.

Contributors Gian Palmares Feel free to customize and expand upon this script to meet the specific needs of EasyBook Dream Holiday Travel Agency.
