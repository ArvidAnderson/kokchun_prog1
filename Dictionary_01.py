"""Vet inte hur många poäng dom olika kurserna är + orkade inte lägga till alla men detta fungerar!

Enkel for loop som plussar på en variablen """

kurser = {
    'prog1' : 100,
    'webutv' : 100,
    'tilprog' : 100,
    'matte' : 100,
}

points = 0

for key,value in kurser.items():
    points += value

print(points)