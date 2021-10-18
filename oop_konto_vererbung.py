class Konto:
    """ Basis Konto Klasse """

    def __init__(self, inhaber, kontonummer, kontostand):
        """ Konstruktor, Aufruf bei Instanzierung """
        print(".. Konto anlegen")
        self.Inhaber = inhaber
        self.Kontonummer = kontonummer
        self.Kontostand = kontostand
        self.zeige_konto()

    def einzahlen(self, betrag):
        """ Mach eine Einzahlung """
        print(".. Einzahlen   : %i %5.1f" % (self.Kontonummer, betrag))
        self.Kontostand += betrag

    def auszahlen(self, betrag):
        """ Mach eine Auszahlung """
        print(".. Auszahlen   : %i %5.1f" % (self.Kontonummer, betrag))
        self.Kontostand -= betrag

    def zeige_konto(self):
        """ Zeige die Kontodaten am Bildschirm """
        print(".. Konto       :", self.Inhaber)
        print("   Kontonummer :", self.Kontonummer)
        print("   Kontostand  :", self.Kontostand)


class Girokonto(Konto):
    """ Giro Konto Klasse """

    def __init__(self, inhaber, kontonummer, kontostand, sollzinsen, habenzinsen):
        """ Giro Konstruktor, Aufruf bei Instanzierung """
        self.__Sollzinsen = sollzinsen
        self.__Habenzinsen = habenzinsen
        # initialisiere Konto
        Konto.__init__(self, inhaber, kontonummer, kontostand)

    def ueberweisung(self, ziel, betrag):
        """ Mach eine Ueberweisung """
        print(".. Transfer    : %i %s %i %5.1f" % (self.Kontonummer, "->", ziel.Kontonummer, betrag))
        self.Kontostand -= betrag
        ziel.Kontostand += betrag


class Sparkonto(Konto):
    """ Sparbuch Konto Klasse """

    def __init__(self, inhaber, kontonummer, kontostand, zinssatz):
        """ Spar Konstruktor, Aufruf bei Instanzierung """
        self.Zinssatz = zinssatz
        # initialisiere des Kontos
        Konto.__init__(self, inhaber, kontonummer, kontostand)

    def zeige_konto(self):
        """ Zeige die Kontodaten am Bildschirm, ueberschreibt Konto Funktion """
        Konto.zeige_konto(self)
        print("   Zinssatz    :", self.Zinssatz)


if __name__ == '__main__':
    print("\nKontobeispiel mit Vererbung")

    # Erzeuge zwei Konto-Objekte
    kg = Girokonto("Heinz Meier", 78340, 12000.0, 0.05, 0.01)
    ks = Sparkonto("Heinz Meier", 78341, 4000.0, 0.03)

    print("------------------------------")

    # Mach was damit ...
    kg.einzahlen(1000)
    ks.einzahlen(2000)
    kg.auszahlen(300)
    kg.ueberweisung(ks, 100)

    print("------------------------------")

    # Zeige Kontodaten am Bildschirm    
    kg.zeige_konto()
    ks.zeige_konto() 