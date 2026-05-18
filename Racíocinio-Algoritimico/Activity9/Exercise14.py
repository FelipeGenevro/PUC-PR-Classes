from itertools import permutations

def eh_quadrado_magico(q):
    soma = 15

    return (
        q[0] + q[1] + q[2] == soma and
        q[3] + q[4] + q[5] == soma and
        q[6] + q[7] + q[8] == soma and

        q[0] + q[3] + q[6] == soma and
        q[1] + q[4] + q[7] == soma and
        q[2] + q[5] + q[8] == soma and

        q[0] + q[4] + q[8] == soma and
        q[2] + q[4] + q[6] == soma
    )


def mostrar_quadrado(q):
    print(q[0], q[1], q[2])
    print(q[3], q[4], q[5])
    print(q[6], q[7], q[8])
    print()


def quadrados_magicos():
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    quantidade = 0

    for combinacao in permutations(numeros):
        if eh_quadrado_magico(combinacao):
            mostrar_quadrado(combinacao)
            quantidade += 1

    print("Quantidade de quadrados mágicos encontrados:", quantidade)


quadrados_magicos()