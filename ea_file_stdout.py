""" In Diesem Beispiel geben wir einen String am Bildschirm 
    oder in ein File aus. """

# Import benoetigter Module
import sys
    
# Frage den Anwender was er will ... 
wahl = input("Ausgabe am (B)ilschirm / (F)ile : ")

# outstream Objekt  
outstream = None                    

if (wahl.upper() == 'B') : 
     print (" ... Bildschirmausgabe")
     outstream = sys.stdout
elif (wahl.upper() == 'F') :
     print (" ... Fileausgabe")
     outstream = open("test.txt", "w") 
else : 
     print ("FEHLER : Ausgabe '%s' nicht implemtiert" % wahl )

# Ausgabe sofern outstream nicht None
if outstream :           
    outstream.write("Das Fluchen ist die einzige Sprache, " +
                    "die jeder Programmierer beherrscht.\n")
    if not outstream == sys.stdout:
        outstream.close()