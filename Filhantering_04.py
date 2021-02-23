"""
Filhantering Uppgift 04 - Arvid Anderson TE19D

Har gjort en rollers_pro_dicers funktion som tar amount som inparameter. i denna funktionen finns en lista som sparar alla talen.
Jag sparar talen för att sedan kunna räkna hur många tal det är av varje.
Jag delar antalet av talet med antalet gånger jag slog tärningarna då får jag fram sannolikheten.

Praktiskt att använda funktion då man slipper ha samma kod om och om igen!

A för Append permission

for loop längst ner som kör igång funktionen med inparamtern 10, 1000, 10000, 1000000

"""
import random as rnd
import colorama
from colorama import Fore, Back, Style, init
init(autoreset=True)

print(Fore.LIGHTMAGENTA_EX + Back.LIGHTYELLOW_EX + """

▐▓█▀▀▀▀▀▀▀▀▀█▓▌░▄▄▄▄▄░
▐▓█░░▀░░▀▄░░█▓▌░█▄▄▄█░
▐▓█░░▄░░▄▀░░█▓▌░█▄▄▄█░ ＡＲＶＩＤ ＡＮＤＥＲＳＯＮ
▐▓█▄▄▄▄▄▄▄▄▄█▓▌░█████░                 𝕋𝔼𝟙𝟡𝔻
░░░░▄▄███▄▄░░░░░█████░


""")

file_name = "diceRollerDeluxus.txt"

def rollers_pro_dicers(amount):
    dices_10 = []
    for i in range(amount):
        dices_10.append(rnd.randint(1,6))
    with open(file_name, "a") as f:
        f.write("Amount of dices: {} \n".format(amount))
        f.write("Antal Ettor: " + str(dices_10.count(1)) + " Sannolikhet: " + str(dices_10.count(1) / amount) + "\n")
        f.write("Antal Tvaor: " + str(dices_10.count(2)) + " Sannolikhet: " + str(dices_10.count(2) / amount) + "\n")
        f.write("Antal Treor: " + str(dices_10.count(3)) + " Sannolikhet: " + str(dices_10.count(3) / amount) + "\n")
        f.write("Antal Fyror: " + str(dices_10.count(4)) + " Sannolikhet: " + str(dices_10.count(4) / amount) + "\n")
        f.write("Antal Femmor: " + str(dices_10.count(5)) + " Sannolikhet: " + str(dices_10.count(5) / amount) + "\n")
        f.write("Antal Sexor: " + str(dices_10.count(6)) + " Sannolikhet: " + str(dices_10.count(6) / amount) + "\n")
        f.write("\n")

dankyboi = 1
for i in range(5):
    dankyboi *= 10
    rollers_pro_dicers(dankyboi)


