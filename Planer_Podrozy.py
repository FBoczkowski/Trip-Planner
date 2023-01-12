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

