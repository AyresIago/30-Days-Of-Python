#Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def start_w_e(x):
  if x[0]=='E' or x[0]=='e':
    return False
  return True

def to_upper_case(name):
  return name.upper()

countries_new = list(map(to_upper_case, filter(start_w_e, countries)))

print(countries_new)