list = []

def imprimir():
    for i in range(1, n):
        list.append(str(i) * i)
        print(list)
        list.clear()

n = int(input("Digite um numero: "))

imprimir()