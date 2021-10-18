while True: 
    zahl = input("Positive Zahl eingeben : ") 

    if zahl < 0: 
        print("Negative Zahlen nicht erlaubt!")
        continue 

    if zahl == 0: 
        print("Skript wird beendet!")
        break 
    
    print("Zahl =", zahl)