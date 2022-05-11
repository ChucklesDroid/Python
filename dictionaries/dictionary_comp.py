#  Dictionaries also support comprehension just like list and sets

even_no = { x:x**2 for x in range(1,11) if x%2==0 }
print(even_no)

cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
cities_in_C = { keys:round((values-32)*(5.0/9.0)) for keys,values in cities_in_F.items() }
print(cities_in_F, cities_in_C, sep='\n')

cold_cities = {key:value for key,value in cities_in_F.items() if value <= 50 }
print(cold_cities)

desc_cities = {key: "Warm" if value > 50 else "cold" for key,value in cities_in_F.items()}
print(desc_cities)

#  We can even return values from a function
def temp_func(value):
    if value >= 75:
        return "Hot"
    elif 75 >= value >= 50:
        return "Warm"
    else:
        return "Cold"

desc_cities = {key:temp_func(value) for key,value in cities_in_F.items()}
print(desc_cities)
