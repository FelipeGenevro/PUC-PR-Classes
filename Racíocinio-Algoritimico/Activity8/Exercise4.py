"""
4. Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as
consoantes.
"""

list = []

word = input("Digita uma palavra de 10 caracteres: ")
for i in word:
    if i not in "aeiou":
        list.append(i)
    else:
        pass

print(list)
print(len(list))