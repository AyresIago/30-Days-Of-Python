#Use filter to filter out countries having exactly six characters.

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def six_char(x):
  if len(x) == 6:
    return True
  return False

country_w_6_char = list(filter(six_char, countries))

print(country_w_6_char)