# word1 = input("Please type in the first word: ")
# word2 = input("Please type in the second word: ")

# string1 = list(word1)
# temporaryString = list(word2)
# string2 = temporaryString[::-1]

# string3 = []
# length1 = len(string1)
# length2 = len(string2)
# a = 0
# maxLength = len(word1)
# while a < maxLength:
#     if a < length1: 
#         string3.append(string1[a])
#     if a < length2 :
#         string3.append(string2[a])
#     a+=1
# word3 = ''.join(string3)
# print(word3)

s1 = "Bonjour"
s2 = "Salut"
s3 = ""
j = 1

if len(s1) > len(s2):
    for i in range(len(s1)):
        s3 = s3 + s1[i] + s2[len(s2)-(i+1)]
        #j += 1
    print(s3)
else: 
