word1 = input("Please type in the first word: ")
word2 = input("Please type in the second word: ")

string1 = list(word1)
temporaryString = list(word2)
string2 = temporaryString[::-1]

string3 = []
length1 = len(string1)
length2 = len(string2)
a = 0
maxLength = len(word1)
while a < maxLength:
    if a < length1: 
        string3.append(string1[a])
    if a < length2 :
        string3.append(string2[a])
    a+=1
word3 = ''.join(string3)
print(word3)