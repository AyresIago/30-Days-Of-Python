'''
Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:
Sort countries by name, by capital, by population
Sort out the ten most spoken languages by location.
Sort out the ten most populated countries.

'''
from countries_data import countries

#1

sorted_by_name = sorted(countries, key= lambda c: c['name'])

sorted_by_capital = sorted(countries, key=lambda c: c.get('capital', ''))

sorted_by_population = sorted(countries, key=lambda c: c.get('population', 0), reverse=True)

print(sorted_by_name)
print(sorted_by_capital)
print(sorted_by_population)

#2
dic = {}

def count_language(dictionary, country):
  for c in country:
    for language in c['languages']:
      if language in dictionary:
        dictionary[language] += 1
      else:
        dictionary[language] = 1
  return dictionary

languages = count_language(dic, countries)

# Ordenação dos itens do dicionario, o lambda pega o primeiro indice da tupla
top_languages = sorted(languages.items(), key=lambda x: x[1], reverse=True)

# Corta os 10 primeiros
top_10_languages = top_languages[:10]

print(top_10_languages)

#3
top_10_population =  sorted_by_population[:10]

print(top_10_population)


