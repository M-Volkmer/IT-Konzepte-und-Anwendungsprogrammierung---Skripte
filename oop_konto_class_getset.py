def inhaber(self):
    """ Gibt den Namen des Inhabers zurueck """
    print(".. getter wird aufgerufen")
    return self.__Inhaber

def setInhaber(self, neuer_Inhaber):
    """ Aendert den Namen des Inhabers """
    print(".. setter wird aufgerufen")
    self.__Inhaber = neuer_Inhaber