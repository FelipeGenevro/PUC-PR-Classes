def valorPagamento(valor_prestacao, dias_atraso):
    if dias_atraso == 0:
        return valor_prestacao
    else:
        multa = valor_prestacao * 0.03
        juros = valor_prestacao * 0.001 * dias_atraso
        valor_final = valor_prestacao + multa + juros
        return valor_final


quantidade_prestacoes = 0
total_pago = 0

while True:
    valor = float(input("Digite o valor da prestação (0 para encerrar): R$ "))

    if valor == 0:
        break

    dias = int(input("Digite o número de dias em atraso: "))

    valor_a_pagar = valorPagamento(valor, dias)

    print(f"Valor a pagar: R$ {valor_a_pagar:.2f}")

    quantidade_prestacoes += 1
    total_pago += valor_a_pagar


print("\nRELATÓRIO DO DIA")
print(f"Quantidade de prestações pagas: {quantidade_prestacoes}")
print(f"Valor total pago: R$ {total_pago:.2f}")