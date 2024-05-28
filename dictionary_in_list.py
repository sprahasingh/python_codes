country = input("Enter name of country\n")
visits = int(input("Enter number of visits\n"))
list_of_cities = (input("Enter cities seperated by ','\n")).split(",")

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

def add_new_country(country, visits, list_of_cities):
  travel_log.append({"country": country, "visits": visits, "cities": list_of_cities})

add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")
print(travel_log)