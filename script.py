destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "Sao Paulo, Brazil", "Cairo, Egypt"]

attractions = [[] for i in range(5)]

test_traveler = ["Erin Wilkes", "Shanghai, China", ["historical site", "art"]]

def get_destination_index(destination):
  return destinations.index(destination)

def get_traveler_location(traveler):
	return get_destination_index(traveler[1])

def add_attraction(destination, attraction):
  try: 
    destination_index = get_destination_index(destination)
    attractions[destination_index].append(attraction)
    return
  except ValueError:
    print("That location isn't in our destination list.")
    return

add_attraction("Los Angeles, USA", ["Venice Beach", ["beach"]])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

test_destination_index = get_traveler_location(test_traveler)