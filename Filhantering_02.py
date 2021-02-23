"""
Filhantering Uppgift 02 - Arvid Anderson TE19D

Flygplanet i ASCII ART ÄR ETT USAF PLAN!

Gjort uppgift A, B och C i samma. Kör filen för att se få fram resultat, resultatet sparas direkt till orginal filen Provresultat.txt, 
Gjort för att köras en gång

Uppgift A: Är en enkel print på f.read() for loop för att vara säker att den läser in dom första raderna som fanns med i orginal filen.
Läser bara in rad 1-19
Uppgift B: läser in varje rad till en lista, for loop för bara rad 1-19 och sorterar sedan listan med .sort() innan den skriver ut raderna i txt filen igenom med hjälp av 
en for loop som går igenom varje person i nu den sorterade listan och skriver ut. 
Uppgift C: Skapat listor för alla betygen, konverterar dom 2 sista nummrerna på raden till en string och har sedan flera if satser som kollar. Valde att inte ha elif då detta fungerar lika bra
Appendar varje elev som har betyget den matchar in på till det betygets lista. Skriver sedan ut listorna under betygets rubrik i text filen.
Loopar så skriver ut eleverna i listan under varan (rad för rad)


"""
import colorama
from colorama import Fore, Back, Style

print(Fore.LIGHTMAGENTA_EX + Back.LIGHTYELLOW_EX + """

            ______
            _\ _~-\___
    =  = ==(____AA____D
                \_____\___________________,-~~~~~~~`-.._
                /     o O o o o o O O o o o o o o O o  |\_
                `~-.__   ARVID___..----..         ANDERSON )
                      `---~~\___________/------------`````
                      =  ===(__TE19D__D
""" + Fore.WHITE + Back.BLACK)

file_name = "Provresultat.txt"

#Uppgift A
with open(file_name, "r") as f:
    print("Uppgift A - DOWN BELOW:")
    for i in range(1,20):
        print(Fore.GREEN + f.readline().strip("\n"))

#Uppgift B
with open(file_name, "r+") as f:
    file_content = []
    for i in range(1,20):
        file_content.append(f.readline())
    file_content.sort()
    f.write("\n-----------------------------------------------------------")
    f.write("\n\nCODE MADE THIS CHANGES BELOW, UPPGIFT [B] OUTPUT BELOW:\n\n")
    f.write("-----------------------------------------------------------\n")
    for person in file_content:
        f.write(person)
    f.write("\n")
    print(f"UPPGIFT B WRITTEN TO {file_name}")

#Uppgift C
with open(file_name, "r+") as f:
    file_content = []
    F = []
    E = []
    D = []
    C = []
    B = []
    A = []
    for i in range(1,20):
        file_content.append(f.readline())
    for person in file_content:
        person_numbers = int(person[-3:])
        if person_numbers < 20:
            F.append(person)
        if person_numbers >= 20 and person_numbers <= 29: 
            E.append(person)
        if person_numbers >= 30 and person_numbers <= 39:
            D.append(person)
        if person_numbers >= 40 and person_numbers <= 49:
            C.append(person)
        if person_numbers >= 50 and person_numbers <= 59:
            B.append(person)
        if person_numbers >= 60 and person_numbers <= 70:
            A.append(person)
    f.write("\n-----------------------------------------------------------")
    f.write("\n\nCODE MADE THIS CHANGES BELOW, UPPGIFT [C] OUTPUT BELOW:\n\n")
    f.write("-----------------------------------------------------------\n")
    f.write("\n[A] ELEVER - GRATTIS SMÅBARN!:\n")
    for person in A:
        f.write(person)
    f.write("\n[B] ELEVER:\n")
    for person in B:
        f.write(person)
    f.write("\n[C] ELEVER:\n")
    for person in C:
        f.write(person)
    f.write("\n[D] ELEVER:\n")
    for person in D:
        f.write(person)
    f.write("\n[E] ELEVER:\n")
    for person in E:
        f.write(person)
    f.write("\n[F] DUMMA ELEVER - BETTER LUCK NEXT TIME!:\n")
    for person in F:
        f.write(person)