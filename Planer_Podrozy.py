import wikipedia

class City:
    def __init__(self, city_, city_information_=0):
        self.city = city_
        self.city_information = city_information_

class Country:
    def __init__(self, country_, country_information_=0):
        self.country = country_
        self.country_information = country_information_

class Travel:
    def __init__(self, trip_name_, spend_money_, start_travel_, finish_travel_, city_: City,
                 country_: Country):
        self.trip_name = trip_name_
        self.spend_money = spend_money_
        self.start_travel = start_travel_
        self.finish_travel = finish_travel_
        self.city = city_
        self.country = country_

class Transport:
    def __init__(self, travel_time_, travel_A_B_, travel_B_A_):
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
            print("\n")

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
        country_name = input("Enter country which you visited/planning visit: ")
        city_name = input("Enter city which you visited/planning visit: ")
        start_travel = input("Enter when you started/planning start travel (DD.MM.YYYY): ")
        finish_travel = input("Enter when you finish/planning start travel (DD.MM.YYYY): ")
        spend_money = int(input("Enter how much money you have spent: "))
        #city_info = wikipedia.summary(f"{city_name}", sentences = 1)
        #country_info = wikipedia.summary(f"{country_name}", sentences = 1)
        city = City(city_name)
        country = Country(country_name)

        new_travel = Travel(trip_name_=trip_name, country_=country, city_=city, start_travel_=start_travel,
                                finish_travel_=finish_travel, spend_money_=spend_money)

        self.travels.append(new_travel)
        self.cities.append(city)
        self.countries.append(country)

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

        new_transport_details = Transport(travel_A_B_=travel_A_B, travel_B_A_=travel_B_A, travel_time_=travel_time)
        self.transports.append(new_transport_details)

    def show_transpoer_details(self):
        for count, nations in enumerate(self.transports):
            print(f"{count}:\n"
                  f"Type of transport, you travel from A to B - {nations.travel_A_B}\n"
                  f"Type of transport, you travel from B to A - {nations.travel_B_A}\n"
                  f"All time which you spend in both way - {nations.travel_time}h\n")
    def show_travels(self):
        for count, trips in enumerate(self.travels):
            print(f"{count}:\n"
                  f"Trip name - {trips.trip_name}\n"
                  f"Country which you visited/planning visit - {trips.country_name}\n"
                  f"City which you visited/planning visit - {trips.city_name}\n"
                  f"Date when you will start or started travel - {trips.start_travel}\n"
                  f"Date when you will finish or finished travel - {trips.finish_travel}\n"
                  f"How much money you spent or will you spend - {trips.spend_money}zł\n")
        print("\n")
    def show_cities(self):
        for count, cities in enumerate(self.cities):
            print(f"{count} - {cities.city}")
        print("\n")
    def show_countries(self):
        for count, nations in enumerate(self.countries):
            print(f"{count} - {nations.country}")
        print("\n")

    def stop_menu(self):
        self.start = False





def main():

    menu = Manager()

    menu.show_menu()

if __name__ == "__main__":
    main()







