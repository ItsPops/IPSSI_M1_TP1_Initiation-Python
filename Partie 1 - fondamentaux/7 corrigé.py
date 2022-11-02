# text = input("Saissisez du texte: ")
# new = list(text)
# new[0] = "x"
# new[-1] = "x"
# print(''.join(new))

s1 = input("Saisissez du texte: ")
print(s1[-1] + s1[1:len(s1)-1] + s1[0])