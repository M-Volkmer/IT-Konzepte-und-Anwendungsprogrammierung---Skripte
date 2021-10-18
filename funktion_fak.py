# Funktion 
def fak(zahl): 
   ergebnis = 1 
   for i in range(2, zahl+1): 
      ergebnis *= i 
   return ergebnis 

# Hauptprogramm
while True: 
    eingabe = int(input("Gib eine Zahl ein: ")) 
    print(fak(eingabe))