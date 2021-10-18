"""
File    : dpMath.py
Author  : D.H. Pahr 
Date    : 26.02.2014

Mathematik Modul
"""

# Funktion 
def fak(zahl): 
   ergebnis = 1 
   for i in range(2, zahl+1): 
      ergebnis *= i 
   return ergebnis