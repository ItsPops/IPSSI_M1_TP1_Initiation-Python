text = input("Saissisez du texte: ")
new = list(text)
new[0] = "x"
new[-1] = "x"
print(''.join(new))