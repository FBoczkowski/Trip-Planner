class Travel:
    def __init__(self, place_, apartment_night_, trip_name_, spend_money_, start_travel_, end_travel_):
        self.place = place_
        self.aprtment_night = apartment_night_
        self.trip_name = trip_name_
        self.spend_money = spend_money_
        self.start_travel = start_travel_
        self.end_travel = end_travel_
    
class City(Travel):
    def __init__(self, city, population_):
        super().__init__(city)
        self.population = population_

class Country(Travel):
    def __init__(self, country, capitol_):
        super().__init__(country)
        self.capitol = capitol_

class Transport(Travel):
    def __init__(self, travel_cost, transport_type_, travel_time_, travel_A_B_, travel_B_A_):
        super().__init__(travel_cost)
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

    def execute_menu(self, choice):
        if choice == "1":

        elif choice == "2":
            print(f"{self.travels}")
        elif choice == "3":
            print(f"{self.cities}")
        elif choice == "4":
            print(f"{self.countries}")
        elif choice == "5":
            self.start = False









