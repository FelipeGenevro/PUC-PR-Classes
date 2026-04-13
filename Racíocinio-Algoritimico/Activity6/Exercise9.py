"""
Elaborar um programa em Python que converta um número decimal em hexadecimal,
fazendo uso de divisões sucessivas
"""

decimal = int(input("Digite um número decimal: "))

if decimal == 0:
    print("Hexadecimal: 0")
else:
    hex_resultado = ""
    digitos = "0123456789ABCDEF"

    while decimal > 0:
        resto = decimal % 16
        hex_resultado = digitos[resto] + hex_resultado
        decimal = decimal // 16

    print(f"Hexadecimal: {hex_resultado}")