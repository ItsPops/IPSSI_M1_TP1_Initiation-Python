import random
import string

#Defining vars
passwordLength = 8
howManyUppers = 1
howManyNumbers = 2
howManySpecials = 7

while True:
    password = ""
    #Constraining numbers of digits
    for digits_index in range(howManyNumbers):
        password = password + random.choice(string.digits)

    #Constraining numbers of special chars
    for punctuation_index in range(howManySpecials):
        password = password + random.choice(string.punctuation)

    #Constraining numbers of uppercase letters
    for upper_index in range(howManyUppers):
        password = password + random.choice(string.ascii_uppercase)

    #Filling with lowercase
    for index in range(passwordLength - howManyNumbers - howManySpecials - howManyUppers):
        password = password + random.choice(string.ascii_lowercase)

    print("Password generated: " + ''.join(random.sample(password,len(password))))
    input("Press Enter to continue... ")
    print("")