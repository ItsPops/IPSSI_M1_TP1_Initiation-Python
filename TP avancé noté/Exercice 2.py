##François BRILLE
#MCS 2022-2024
#Révisions python
#Exercice 2

#On définit ici le nombre à trouver et les deux listes de nombre
numberToFind = 21
list1 = [10,7,4,12,8]
list2 = [15,9,4,13,2]

#On soustrait le nombre à trouver de chaque nombre de la première liste. Si le résultat de cette soustraction est dans la seconde liste, on a gagné.
length = len(list1)
for i in range(length):
    substract = numberToFind - list1[i]
    if substract in list2:
        print("[" + str(list1[i]) + "," + str(substract) + "]")
