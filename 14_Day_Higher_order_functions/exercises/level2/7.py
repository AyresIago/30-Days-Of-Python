countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def start_w_e(x):
  if x[0]=='E' or x[0]=='e':
    return False
  return True

country_start_w_e = list(filter(start_w_e, countries))

print(country_start_w_e)