"""Importerar random för jag behöver den modulen
Skapar mitt dictonary med namnet frekvenstablell
Gör en for loop som lägger ökar key i dictonary med 1
Printar ut frekvenstabellen

"""


import random as rnd

frekvenstabell = {
    '1': 0,
    '2': 0,
    '3': 0,
    '4': 0,
    '5': 0,
    '6': 0,
}

for i in range(100000):
    slag = rnd.randint(1,6)
    frekvenstabell[str(slag)] += 1

print('Frekvenstabell')
for key, value in frekvenstabell.items():
    print(f"{key}: {value}")