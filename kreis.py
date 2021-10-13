# -*- coding: utf-8 -*-
"""
File    : kreis.py
Author  : D.H. Pahr 
Date    : 26.02.2014

Mein erstes Python Skript zur Berechnung von 
Umfang und Fläche eines Kreises.
"""

# Definition von Variablen 
radius = 1.5
pi = 3.14159

# Berechne ...
umfang = 2 * radius * pi
flaeche = radius ** 2 * pi

# Ausgabe 
print(__doc__)
print("  Radius  = ", radius)
print("  Umfang  = ", umfang)
print("  Flaeche = ", flaeche)