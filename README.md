# Trip-Planner

This is a Python program that helps you manage your travels. It has the following features:

- Add new travels to a list.
- Add details about travel transport.
- Show a list of all your travels.
- Show the details of all travel transport.
- Show all the cities you have visited.
- Show all the countries you have visited.
- Exit the program.

**Prerequisites**

- Python 3.x installed on your machine.
- The following packages need to be installed `wikipedia`

You can install the packages by running `pip install -r requirements.txt` in your terminal.

**How to use**

1. Run `trip_planner.py` in your terminal.
2. The program will display a menu with options to add new travel, add new details of travel transport, show travels, show transport details, show all cities visited, show all countries visited, or exit the program.
3. Choose the option you want and follow the prompts.
4. After each operation, the program will return to the main menu.
5. To exit the program, choose option 7 in the menu.

**Classes**

**City**
The `City` class represents a city that you have visited/planning to visit. It has the following attributes:

- `name`: a string representing the name of the city.
- `information`: an integer representing the amount of information available about the city.

**Country**
The `Country` class represents a country that you have visited/planning to visit. It has the following attributes:

- `name`: a string representing the name of the country.
- `information`: an integer representing the amount of information available about the country.

**Travel**
The `Travel` class represents a travel that you have taken/planning to take. It has the following attributes:

- `trip_name`: a string representing the name of the travel.
- `spend_money`: an integer representing the amount of money spent on the travel.
- `start_travel`: a datetime object representing the start date of the travel.
- `finish_travel`: a datetime object representing the finish date of the travel.
- `city`: a City object representing the city visited/planning to visit.
- `country`: a Country object representing the country visited/planning to visit.

**Transport**
The `Transport` class represents the details of the transport used during a travel. It has the following attributes:

- `travel_time`: a string representing the amount of time spent traveling.
- `travel_A_B`: a string representing the type of transport used to travel from A to B.
- `travel_B_A`: a string representing the type of transport used to travel from B to A.

**Manager**
The `Manager` class manages all the functions of the program. It has the following methods:

- `show_menu()`: displays the main menu.
- `execute_menu(choice)`: executes the user's choice from the main menu.
- `change_date(date_str)`: converts a date string in the format "YYYY.MM.DD" to a datetime object.
- `wiki_info(place)`: gets a short summary of the given place from Wikipedia.
- `add_new_travel()`: adds a new travel to the list of travels.
- `transport_details()`: adds the details of transport used during a travel.
- `show_transpoer_details()`: displays the details of all transport used during all travels.
- `show_travels()`: displays the details of all travels.
- `show_cities()`: displays the details of all cities visited.
- `show_countries()`: displays the details of all countries visited.


