country = input("Enter name of country\n")
visits = int(input("Enter number of visits\n"))
cities = (input("Enter cities separated by ','\n")).split(",")

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


def add_new_country(str_country, int_visits, list_cities):
    travel_log.append({"country": str_country, "visits": int_visits, "cities": list_cities})


add_new_country(country, visits, cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")
print(travel_log)
