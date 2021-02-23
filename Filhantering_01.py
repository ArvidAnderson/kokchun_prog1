"""
Filhantering Uppgift 01 - Arvid Anderson TE19D
Simulerar tärningskast med random randint. Använder en for loop för att simulera 10 tärningskast och lägga till varje kast i en listan,
sedan kör jag en with open med append som permission då jag inte gillar f.open("filename") då man måste använda sig utav f.close() -
det är för lätt att glömma.
Skriver ut min lista som en str till txt filen diceRoll.txt, sedan en sorterad version av listan och tillsist används -
count för att räkna antalet femmor i listan
"""
import random as rnd
simulerade_tärningar = []
for i in range(1,11):
    tärning = rnd.randint(1,6)
    simulerade_tärningar.append(tärning)
with open("diceRoll.txt", "a") as f:
    f.write("Listan osorterad: " + str(simulerade_tärningar) + "\n")
    simulerade_tärningar.sort()
    f.write("Listan sorterad: " + str(simulerade_tärningar) + "\n")
    f.write("Antal femmor: "+ str(simulerade_tärningar.count(5)) + "\n")




