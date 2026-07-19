#Use map to change each name to uppercase in the names list

names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']

def to_upper_case(name):
  return name.upper()

names_upper = list(map(to_upper_case, names))

print(names_upper)