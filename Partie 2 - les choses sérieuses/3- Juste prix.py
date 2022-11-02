import random
justePrix = random.randrange(0, 100)
print(justePrix)
userInput = ""

while justePrix != userInput:
    try:
        userInput = int(input("Choissisez un nombre... "))
        if userInput > justePrix:
            print("C'est moins ! ")
        elif userInput < justePrix:
            print("C'est plus ! ")
        elif userInput == justePrix:
            print("Bravo ! Le juste prix était bel et bien " + str(justePrix))
            break
        elif userInput == str(exit):
            break
    except ValueError:
        print("Une erreur est survenue. Avez-vous saisi un nombre ?")
    except KeyboardInterrupt:
        print("")
        print("Bye bye...")
        break