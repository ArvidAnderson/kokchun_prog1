word = []
morsedict = {}

with open('morse.txt', 'r') as f:
    for line in f:
        key, value = line.split()
        morsedict[key.replace(':', '')] = value

def morse(string):
    for i in string:
        word.append(morsedict[i])
    output = ''.join(word)
    print(output)

user_input = str(input("Skriv ett valfritt ord för att konvertera till morsecode: ")).upper()
morse(user_input)