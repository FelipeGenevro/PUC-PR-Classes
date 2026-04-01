#algoritmo que conta quantas vogais tem em uma frase

import unicodedata


a = 0
e = 0
i = 0
o = 0
u = 0


def remover_acentos(word):
    return "".join(
        filter(
            lambda c: unicodedata.category(c) != 'Mn',
            unicodedata.normalize('NFD', word)
        )
    )


word = input("Digite uma palavra: ")
resultado = remover_acentos(word)

print(resultado)

for vogal in resultado:
    if vogal == "a":
        a += 1
    elif vogal == "e":
        e += 1
    elif vogal == "i":
        i += 1
    elif vogal == "o":
        o += 1
    elif vogal == "u":
        u += 1

total = len(resultado)
soma = a + e + i + o + u
perc = (soma / total) * 100

print(f"A = {a}")
print(f"E = {e}")
print(f"I = {i}")
print(f"O = {o}")
print(f"U = {u}")
print(f"O total de vogais é {soma}")
print(f"sua frase é {perc:.2f}% composta por vogais")

