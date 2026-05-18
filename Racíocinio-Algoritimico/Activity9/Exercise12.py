import random

def embaralhar_palavra(palavra):
    # Padroniza para minúsculas
    palavra = palavra.lower()

    # Transforma em lista
    letras = list(palavra)

    # Embaralha as letras
    random.shuffle(letras)

    # Junta novamente em string
    return ''.join(letras)


# Input do usuário
texto = input("Digite uma palavra: ")

resultado = embaralhar_palavra(texto)

print("Palavra embaralhada:", resultado)    