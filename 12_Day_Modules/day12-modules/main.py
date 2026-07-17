import mymodule

nome = mymodule.generate_full_name('iago', 'lima')

print(nome)

from mymodule import generate_full_name

nome2 = generate_full_name('joao', 'otavio')

print(nome2)

from mymodule import generate_full_name as fullname

nome3 = fullname('juca', 'jucao')

