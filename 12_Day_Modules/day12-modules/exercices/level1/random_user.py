from random import randint, choices
from string import ascii_letters, digits

def random_user_id():
  return randint(100000, 999999)

def user_id_gen_by_user():
  characters = int(input())
  n = int(input())
  all_characters = ascii_letters + digits

  for i in range(n):
    id = ''
    id = id.join(choices(all_characters, k=characters))
    print(id)

