#Felhantering Uppgift 02
#Arvid Anderson TE19D

import string
import math

#Ändra här

#Kollar om talet är fyrsiffrigt, kollar även om det är fyrsiffrigt fast det är negativt
def ar_fyrsiffrigttal(tal):
    tal_str = str(tal)
    if len(tal_str) == 4:
        return True
    elif tal_str.startswith("-") and len(tal_str) == 5:
        return True
    else:
        return False


# Testprogram
testtal = [100, 231, 10000, 10001, -1000, 102313]

#Du hade skrivit "fyrsirrigt" i programmeringsövningshäftet
for t in testtal:
    if ar_fyrsiffrigttal(t):
        print("{} är fyrsiffrigt".format(t))
    else:
        print("{} är inte fyrsiffrigt".format(t))