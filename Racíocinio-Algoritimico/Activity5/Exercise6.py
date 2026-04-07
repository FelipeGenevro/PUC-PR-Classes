#Algoritmo que solicita uma palavra e retorna apenas a palavra sem vogais

import unicodedata

texto = input("Digite um texto: ")

texto_sem_acento = unicodedata.normalize('NFD', texto)
texto_sem_acento = ''.join(
    c for c in texto_sem_acento if unicodedata.category(c) != 'Mn'
)

vogais = "aeiouAEIOU"

resultado = ''.join(
    c for c in texto_sem_acento if c not in vogais
)

print("Resultado:", resultado)