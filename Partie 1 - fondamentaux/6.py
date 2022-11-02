text = input("Saissisez du texte: ")
firstChar = str(text[0])
concatChar = ""
if text.count(firstChar) > 0:
    for char in text: 
        if char == firstChar:
            concatChar = concatChar + "*"
        else:
            concatChar = concatChar + char
    concatChar = concatChar
    concatChar = firstChar + concatChar[1:]
    print(concatChar)
