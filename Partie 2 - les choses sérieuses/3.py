import random
justePrix = random.randrange(0, 100)
print(justePrix)
userInput = ""
while justePrix != userInput:
    userInput = int(input("Choissisez un nombre... "))
    if userInput > justePrix:
        print("C'est moins ! ")
    elif userInput < justePrix:
        print("C'est plus ! ")
    else: 
        print("Une erreur est survenue")
print("Bravo ! Le juste prix était: " + str(justePrix))