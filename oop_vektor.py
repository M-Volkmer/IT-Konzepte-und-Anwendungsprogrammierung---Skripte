class Vektor: 
    """ 2D Vektor Klasse """

    def __init__(self, x, y):              
        self.x = x 
        self.y = y 

    def __add__(self, other): 
        """ Ueberladener '+' Operator """
        return Vektor( self.x+other.x, self.y+other.y )

    def __str__(self): 
        """ Ueberladene print Funktion """
        return "[%f %f]" % (self.x, self.y) 
        

if __name__ == '__main__':
    
    print("\nBeispiel Polymorphismus")
    
    # Erzeuge zwei Vektor Objekte
    v1 = Vektor(3,4)
    v2 = Vektor(1,2) 
    
    # Addiere 2 Vektoren
    vs = v1 + v2 
              
    # Ausgabe des neuen Vektors    
    print('vs =', vs)