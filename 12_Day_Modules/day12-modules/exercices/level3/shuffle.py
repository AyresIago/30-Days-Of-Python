from random import randint

def seven_random():
  lista = []
  i = 0

  while(i < 7):
    x = randint(0, 9) 
    if x not in lista:
      lista.append(x)
      i += 1
  return lista