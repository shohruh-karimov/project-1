class Country:
    def __init__(self, country_name, city, region):
        self.country_name = country_name
        self.city = city
        self.region = region

object = Country('Uzbekidtan', 'Tashkent', 'Asia')
print('country name:', object.country_name, 'city:', object.city, 'region:', object.region)