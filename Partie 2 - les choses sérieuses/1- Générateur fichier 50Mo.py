import random
with open('fichier_50mo', 'w') as f:
    num_chars = 3125000 #choisi en effectuant une règle de trois: je sais que ma chaîne de charactère fait 16 charactères, 16*3125000 = 50 Mo = 50 MB
    f.write(''.join(random.choice('0123456789ABCDEF') for i in range(16)) * num_chars)