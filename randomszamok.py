import random
import math
def veletlen_szamok():
    i:int= 0
    while i<10:
        szam:int = math.floor (random.random()*21 + 10)
        print(szam)
        i+=1

"""Generálj 5 véletlen lottószámot(1-90 között)"""

i = 0
while i < 5:  
    szam = random.randint(1, 90)  
    print(szam)
    i += 1

"""Generálj 1 véletlen kétjegyű egész számot, és döntsd el róla, hogypáros vagy páratlan"""


i = 0

while i < 10:
    szam = math.floor(random.random() * 21 + 10)
    print(f"Szám: {szam}")

    if szam % 2 == 0:
        print("Ez a szám páros.")
    else:
        print("Ez a szám páratlan.")

    i += 1

"""Generálj 15 db egész számot [0 1] között.  Hány 1-est generáltál?"""
i = 0
egyesek_szama = 0
while i < 15:
    szam2 = math.floor(random.random( ) *2)
    print(f"Szám: {szam2}")

    if szam2 == 1:
        egyesek_szama += 1

    i+= 1

print(f"Az egyesek száma: {egyesek_szama}")
    
