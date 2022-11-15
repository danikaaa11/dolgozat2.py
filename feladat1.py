import random

osztaly=[]

for i in range(27):
    magassag = random.randint(160,200)
    osztaly.append(magassag)

print("A osztály tanulónak magassága:",osztaly)

#1 feladat

atlag = sum(osztaly)
print("Az osztály össz magassága ",(sum(osztaly)))
print("Az osztály tanulóknak az átlag magassága ",(round(atlag, 2)))

#2 feladat #Ez feladat nem megy köszönöm a megértését. :) 
print("Ő a legmagasabb ",max(osztaly))
print("Ő a legalacsonyabb ",min(osztaly))

#3 feladat

print("Ennyi az osztály legkissebb és legnagyobb közötti különbség cm-be: ",max(osztaly)-min(osztaly))
    
#4 feladat

print("Ekkora lenne mindenki a osztályból ha fel álna a másik vállálra m-be: ",atlag//100)

#5 feladat

ujtanulo = [182]
ujosztaly = osztaly + ujtanulo
print("Az új tanulóval együtt: ",ujosztaly)

#6 feladat
sorrend = ujosztaly.sort()
print("Az új tornasor: ",ujosztaly)    

#7 feladat #Nem biztos hogy jó. :)
if():
    print("Vannak egymagasak: ")
else:
    print("Nincsenek egymagasak")    
