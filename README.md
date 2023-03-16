# Trip-Planner
This is a Python program that allows users to manage their travels. Users can create new travels, add travel transport details, and view all their past travels. The program uses the typing module and Wikipedia API.
Installation
Clone the repository: git clone https://github.com/<USERNAME>/travel-manager.git
Install the required packages: pip install -r requirements.txt
Usage
Run python main.py to start the program.
Use the menu options to add a new travel, add travel transport details, show travels, show transport details, show all cities visited, and show all countries visited.
To exit the program, select 7 from the menu.
Classes
City
Represents a city with a name and information about the city.
Constructor takes two parameters: name_ and information_=0.
Country
Represents a country with a name and information about the country.
Constructor takes two parameters: name_ and information_=0.
Travel
Represents a travel with a name, spend money, start and finish travel date, city and country details.
Constructor takes six parameters: trip_name_, spend_money_, start_travel_, finish_travel_, city_: City, and country_: Country.
Transport
Represents a transport with travel time and travel details for going from point A to point B and from point B to point A.
Constructor takes three parameters: travel_time_, travel_A_B_, and travel_B_A_.
Manager
Represents the main manager for travels and the UI for the program.
The constructor initializes lists for travels, cities, countries, and transports.
The show_menu function displays the menu options and prompts the user to make a selection.
The execute_menu function calls the appropriate function based on the user's selection.
The add_new_travel function prompts the user for travel details and creates a new Travel object with those details.
The transport_details function prompts the user for transport details and creates a new Transport object with those details.
The show_transpoer_details function displays all the transport details.
The show_travels function displays all the travels.
The show_cities function displays all the cities visited and provides a short summary of each city using the Wikipedia API.
The show_countries function displays all the countries visited.
Contributing
Contributions are welcome! If you find any bugs or have any suggestions for improvement, please submit an issue or pull request.
