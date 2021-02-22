#Felhantering Uppgift 4
import time
from colorama import Fore, Back, Style
import statistics
#Lista för alla talen
tal_lista = []

#Kolla om talet upprepas lista
redan_kollade = []
print("""

 _    _        _                              
| |  | |      | |                             
| |  | |  ___ | |  ___  ___   _ __ ___    ___ 
| |/\| | / _ \| | / __|/ _ \ | '_ ` _ \  / _ 
\  /\  /|  __/| || (__| (_) || | | | | ||  __/
 \/  \/  \___||_| \___|\___/ |_| |_| |_| \___|

                                     
Arvid Anderson TE19D ©                                         
                                         
""")
time.sleep(2)

"""Flera looper för alla inputs slippa behöva skriva om alla om någont
blivit fel, finns säkert bättre sätt att lösa detta på men inget jag vet just nu

Checkar om talen är negativa med assert eller om det blir en ValueError med hjälp av ValueError. """

# Tal 1 loop
while True:
    try:
        tal1 = int(input(Fore.GREEN + "Mata in ditt första tal: "))
        assert tal1 > 0, "The number is negative!"
        break
    except AssertionError as a:
        print(Fore.RED + "ERROR BELOW ↓")
        print(a)
        print("Try again with an non negative number...")
    except ValueError as value:
        print(Fore.RED + "ERROR BELOW ↓")
        print(value)
        print("Try again with an int as an input...")

# Tal 2 loop
while True:
    try:
        tal2 = int(input(Fore.GREEN + "Mata in ditt andra tal: "))
        assert tal2 > 0, "The number is negative!"
        break
    except AssertionError as a:
        print(Fore.RED + "ERROR BELOW ↓")
        print(a)
        print("Try again with an non negative number...")
    except ValueError as value:
        print(Fore.RED + "ERROR BELOW ↓")
        print(value)
        print("Try again with an int as an input...")

# Tal 3 loop
while True:
    try:
        tal3 = int(input(Fore.GREEN + "Mata in ditt tredje tal: "))
        assert tal3 > 0, "The number is negative!"
        break
    except AssertionError as a:
        print(Fore.RED + "ERROR BELOW ↓")
        print(a)
        print("Try again with an non negative number...")
    except ValueError as value:
        print(Fore.RED + "ERROR BELOW ↓")
        print(value)
        print("Try again with an int as an input...")

# Tal 4 loop
while True:
    try:
        tal4 = int(input(Fore.GREEN + "Mata in ditt fjärde tal: "))
        assert tal4 > 0, "The number is negative!"
        break
    except AssertionError as a:
        print(Fore.RED + "ERROR BELOW ↓")
        print(a)
        print("Try again with an non negative number...")
    except ValueError as value:
        print(Fore.RED + "ERROR BELOW ↓")
        print(value)
        print("Try again with an int as an input...")

# Tal 5 loop
while True:
    try:
        tal5 = int(input(Fore.GREEN + "Mata in ditt femte tal: "))
        assert tal5 > 0, "The number is negative!"
        break
    except AssertionError as a:
        print(Fore.RED + "ERROR BELOW ↓")
        print(a)
        print("Try again with an non negative number...")
    except ValueError as value:
        print(Fore.RED + "ERROR BELOW ↓")
        print(value)
        print("Try again with an int as an input")

#Lägger till alla tal i en lista
tal_lista.extend([tal1,tal2,tal3,tal4,tal5])

#La till bara för att testa men tyckte det var kul att ha med, typ av felhantering i detta fall bara fel medelande 
for tal in tal_lista:
    if tal in redan_kollade:
        print(Fore.RED + "[WARNING] Upprepat nummer bland dina inputs: {}".format(tal))
    else:
        redan_kollade.append(tal)


#Reset färg på text
print(Fore.WHITE)

#Printar största talet
print(Fore.YELLOW + f"Största talet du skrivit in är: {max(tal_lista)}")
#Printar minsta talet
print(Fore.YELLOW + f"Största talet du skrivit in är: {min(tal_lista)}")
#Printar medianen
print(Fore.YELLOW + f"Medianen av talen du skrivit in är: {statistics.median(tal_lista)}")
#Printar medelvärdet
print(Fore.YELLOW + f"Medelvärdet av talen du skrivit in är: {statistics.mean(tal_lista)}")


exit()