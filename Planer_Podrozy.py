class Travel:
    def __init__(self, place_):
        self.place = place_

class City(Travel):
    def __init__(self, city, population_):
        super().__init__(city)
        self.population = population_

class Country(Travel):
    def __init__(self, country, capitol_):
        super().__init__(country)
        self.capitol = capitol_