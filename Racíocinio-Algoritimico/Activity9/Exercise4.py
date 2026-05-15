def verificar_numero(valor):
    if valor > 0:
        return 'P'
    else:
        return 'N'


# Entrada do usuário
numero = float(input("Digite um número: "))

# Resultado
resultado = verificar_numero(numero)

print(f"Resultado: {resultado}")