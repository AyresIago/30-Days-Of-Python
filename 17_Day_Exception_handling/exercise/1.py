'''names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']. 
Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.'''

names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']

#unpacking the list
*nordic_countries, es, ru = names

print(nordic_countries)
print(es)
print(ru)