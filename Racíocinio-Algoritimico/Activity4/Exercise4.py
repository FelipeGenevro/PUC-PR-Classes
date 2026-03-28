#algoritmo para um sistema de loja que permite o vendedor definir o valor do produto e escolher uma forma de pagamento

valor_etiqueta = float(input("Digite o valor do produto na etiqueta:"))

print("Insira a forma de pagamento:")
print("1 - À vista em dinheiro ou cheque, recebe 10% de desconto")
print("2 – À vista no cartão de crédito, recebe 15% de desconto")
print("3 – Em duas vezes, preço normal de etiqueta sem juros")
print("4 - Em duas vezes, preço normal de etiqueta mais juros de 10%")

forma_de_pagamento = int(input("OBS: digite apenas o número!"))

etiqueta = valor_etiqueta

if forma_de_pagamento == 1:
    valor_final = etiqueta * 0.90
    print(f"pagando à vista no dinheiro, o produto custará R${valor_final} reais")
elif forma_de_pagamento == 2:
    valor_final = etiqueta * 0.85
    print(f"pagando à vista no cartão de crédito, o produto custará R${valor_final} reais")
elif forma_de_pagamento == 3:
    parcela = etiqueta / 2
    print(f"pagando em duas vezes no cartão sem juros, o valor final será R${etiqueta} reais, em duas parcelas de R${parcela} reais")
elif forma_de_pagamento == 4:
    valor_final = etiqueta * 1.1
    parcela = valor_final / 2
    print(f"pagando em duas vezes no cartão com juros, o valor final será R${valor_final} reais, em duas parcelas de R${parcela} reais")