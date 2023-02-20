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
    def __init__(self, travel_cost_, travel_time_, travel_A_B_, travel_B_A_):
        self.travel_cost = travel_cost_
        self.travel_time = travel_time_
        self.travel_A_B = travel_A_B_
        self.travel_B_A = travel_B_A_

class Manager:
    def __init__(self):
        self.travels = []
        self.countries = []
        self.cities = []
        self.transports = []
        self.start = True

    def show_menu(self):
        while(self.start):
            print("1. Add new travel")
            print("2. Add new details of Travel Transport")
            print("3. Show travels")
            print("4. Show transport details")
            print("5. Show all cities which you visited")
            print("6. Show all countries which you visited")
            print("7. Exit")

            choice = input()
            self.execute_menu(choice)

    def execute_menu(self, choice):
        if choice == "1":
            self.add_new_travel()
        elif choice == "2":
            self.transport_details()
        elif choice == "3":
            self.show_travels()
        elif choice == "4":
            self.show_transpoer_details()
        elif choice == "5":
            self.show_cities()
        elif choice == "6":
            self.show_countries()
        elif choice == "7":
            self.start = False

        def add_new_travel(self):
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

    def transport_details(self):
        travel_A_B = input("Which type of transport do you travel from A to B? You can choose from this list:\n"
                           "- Car\n"
                           "- Plane\n"
                           "- Bus\n"
                           "- Train")
        travel_B_A = input("Which type of transport do you travel from A to B? You can choose from this list:\n"
                           "- Car\n"
                           "- Plane\n"
                           "- Bus\n"
                           "- Train")
        travel_time = input("How much time do you spend in both way?: ")
        travel_cost = input("How much money do you spend money for transport?: ")

        new_transport_details = Transport(travel_A_B_=travel_A_B, travel_B_A_=travel_B_A, travel_time_=travel_time,
                                          travel_cost_=travel_cost)
        self.transports.append(new_transport_details)

    def show_transpoer_details(self):
        print(f"{self.transports}")
    def show_travels(self):
        print(f"{self.travels}")

    def show_cities(self):
        print(f"{self.cities}")

    def show_countries(self):
        print(f"{self.countries}")

    def stop_menu(self):
        self.start = False


def main():


if __name__ == "__main__":
    main()







