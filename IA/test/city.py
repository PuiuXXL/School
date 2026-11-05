class City:
    def __init__(self,name):
        self.name = name
        self.temperatures = []

    def add_temperature(self,temperature):
        if temperature >= -50 and temperature <= 50:
            self.temperatures.append(temperature)
        else:
            print(f"Temperatura invalida pentru orasul {self.name}")

    def average_temperature(self):
        if len(self.temperatures) !=  0:
            return sum(self.temperatures)/len(self.temperatures)
        else:
            return 0
    def __str__(self):
        return f"Orasul {self.name} cu temperatura medie de {self.average_temperature()}"


def mild_cities(cities):
    new_list = [city for city in cities if city.average_temperature() >= 15]
    return new_list
    

city1 = City("Deva")
city2 = City("Cluj-Napoca")
city3 = City("Bucuresti")

city1.add_temperature(20)
city1.add_temperature(30)

city2.add_temperature(50)
city2.add_temperature(30)

city3.add_temperature(10)
city3.add_temperature(19)

cities = []
cities.append(city1)
cities.append(city2)
cities.append(city3)

# for city in cities:
#     print(city)
new_list = mild_cities(cities)
for city in new_list:
    print(city)