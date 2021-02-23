#Felhantering Uppgift 03
#Arvid Anderson TE19D
print("""
  ___ _ __   __ _  ___ ___ 
 / __| '_ \ / _` |/ __/ _ 
 \__ \ |_) | (_| | (_|  __/
 |___/ .__/ \__,_|\___\___|
     |_|                   
 """)

#Input loopar kollar om tal är mindre än 1 och om det inte är en INT
while True:
    try:
        antal_input = int(input("Hur många gånger vill du åka spårvagn?: "))
        assert antal_input > 0, "Ditt tal är mindre än ett!" #Om tal är mindre en 0 assertionerror
        break
    except AssertionError as a:
        print(a)
    except ValueError:
        print("Du måste mata in ett heltal (INT)") #Om det inte är int som jag specificerat på inputen så blir det int error

while True:
    try:
        engång_input = int(input("Vad är engångs kostnaden?: "))
        assert engång_input > 0, "Ditt tal är mindre än ett!"
        break
    except AssertionError as a:
        print(a)
    except ValueError:
        print("Du måste mata in ett heltal (INT)")

while True:
    try:
        månad_input = int(input("Vad kostar ett månadskort?: "))
        assert månad_input > 0, "Ditt tal är mindre än ett!"
        break
    except AssertionError as a:
        print(a)
    except ValueError:
        print("Du måste mata in ett heltal (INT)")

#Enkel if sats som kollar om det lönar sig med månadskort eller engångsbiljetter
if antal_input * engång_input > månad_input:
    print("Du borde köpa ett månadskort!")
elif antal_input * engång_input == månad_input:
    print("Du kan välja om du vill köpa ett månadskort eller engångsbiljetter, det hade kostat dig lika mycket!")
else:
    print("Du borde köpa engångsbiljetter!")