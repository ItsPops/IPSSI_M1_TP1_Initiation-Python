from random import *
from string import *

print("Bivenue dans le générateur de string !")
i = int(input("Sélectionner la longueur de la chaîne de charactère aléatoire: "))
print("La chaîne de charactère générée avec " + str(i) + " charactères est: " + ''.join(choices(ascii_lowercase, k=i)))
print("")

print("Bivenue dans le générateur de nombre !")
x = int(input("Sélectionner la borne min: "))
y = int(input("Sélectionner la borne max: "))
print("Le nombre généré entre " + str(x) + " et " + str(y) + " est: " + str(randint(x, y)))
print("")

print("Bivenue dans le générateur de multiple de 7 entre 0 et 70 !")
print("Le multiple de 7 entre 0 est 70 est: " + str(randrange(0, 70, 7)))
print("")
