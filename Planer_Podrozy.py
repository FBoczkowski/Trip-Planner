class Travel:
    def __init__(self, place_, apartment_night_, trip_name_, spend_money_, start_travel_, finish_travel_, city_,
                 country_, transport_):
        self.place = place_
        self.aprtment_night = apartment_night_
        self.trip_name = trip_name_
        self.spend_money = spend_money_
        self.start_travel = start_travel_
        self.finish_travel = finish_travel_
        self.city = city_
        self.country = country_
        self.transport = transport_

class City:
    def __init__(self, city_, population_):
        self.city = city_
        self.population = population_

class Country:
    def __init__(self, country_, capitol_):
        self.country = country_
        self.capitol = capitol_

class Transport:
    def __init__(self, travel_cost_, transport_type_, travel_time_, travel_A_B_, travel_B_A_):
        self.travel_cost = travel_cost_
        self.transport_type = transport_type_
        self.travel_time = travel_time_
        self.travel_A_B = travel_A_B_
        self.travel_B_A = travel_B_A_

class Manager:
    def __init__(self):
        self.travels = []
        self.countries = []
        self.cities = []
        self.start = True

    def show_menu(self):
        while(self.start):
            print("1. Add new travel")
            print("2. Show travels")
            print("3. Show all cities which you visited")
            print("4. Show all countries which you visited")
            print("5. Exit")

            choice = input()
            self.execute_menu(choice)
    def add_new_travel(self, choice):
        if choice == "1":
            trip_name = input("Enter Trip name: ")
            country = input("Enter country which you visited/planning visit: ")
            city = input("Enter city which you visited/planning visit: ")
            start_travel = input("Enter when you started/planning start travel (DD.MM.YYYY): ")
            finish_travel = input("Enter when you finish/planning start travel (DD.MM.YYYY): ")
            transport = input("Enter which type of transport you have used: ")
            spend_money = input("Enter how much money you have spent: ")

            new_travel = Travel(trip_name_=trip_name, country_=country, city_=city, start_travel_=start_travel,
                                finish_travel_=finish_travel, transport_=transport, spend_money_=spend_money)
            self.travels.append(new_travel)
            self.cities.append(Travel(city_=city))
            self.countries.append(Travel(country_=country))


    def show_travels(self, choice):
        if choice == "2":
            print(f"{self.travels}")

    def show_cities(self, choice):
        if choice == "3":
            print(f"{self.cities}")

    def show_countries(self, choice):
        if choice == "4":
            print(f"{self.countries}")

    def stop_menu(self, choice):
        if choice == "5":
            self.start = False









