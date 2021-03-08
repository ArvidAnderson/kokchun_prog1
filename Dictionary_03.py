"""
Skapar en dict
Lägger till alla pokemons i det dict jag skapat, förvarar typen och index i en lista
Har en input så du kan välja pokemon.
Pokemon är key så du söker efter en pokemon och sen printar ju ut typen och index från key.

"""


pokedex = {}

with open('pokemonlista.txt', 'r') as f:
    for line in f:
        index, pokemon, typ = line.split()
        pokedex[pokemon] = [typ, index]


user_input = str(input("Select a pokemon: ")).capitalize()

print(f"Din valda pokemon: {user_input}")
print(f"Typ: {pokedex[user_input][0]}, Index: {pokedex[user_input][1]}")