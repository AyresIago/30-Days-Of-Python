#Use filter to filter out countries containing 'land'.

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def contains_land(country):
  if 'land' not in country:
    return True
  return False

countries_without_land = filter(contains_land, countries)

print(list(countries_without_land))