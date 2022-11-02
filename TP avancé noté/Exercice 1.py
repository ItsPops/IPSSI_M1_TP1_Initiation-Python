##François BRILLE
#MCS 2022-2024
#Révisions python
#Exercice 1

#On définit les bornes de notre premier range A
borneMinA = 10
borneMaxA = 102

#On définit les bornes de notre second range B
borneMinB = 101
borneMaxB = 150

#On vérifie que les bornes minimales ne soient pas supérieures au bornes maximales, sinon on quitte.
#On compare d'abord les bornes extrêmes: la borne basse du premier range doit être <= à la borne haute du second range
#On compare ensuite les bornes intermédiaires: la borne haute du premier range doit être >= à la borne basse du second range

if borneMinA > borneMaxA or borneMinB > borneMaxB:
    print("Erreur: toute borne maximale doit être supérieure à la borne minimale du même range.")
    exit
else:
    if borneMinA <= borneMaxB and borneMaxA >= borneMinB:
        print("Yes")