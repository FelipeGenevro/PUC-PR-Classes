#Algoritmo capaz de calcular o Imposto de Renda de acordo com as métricas entregues pelo professor

rendimento_mensal = float(input("Qual o seu rendimento mensal? "))
dependentes = int(input("Qual o número de dependentes? "))
pensao_alimenticia_valor = float(input("Qual o valor da sua pensão alimentícia? "))
outras_deducoes_valor = float(input("Qual o total de suas outras deduções? "))

valor_dependente = 189.59

base_calculo = rendimento_mensal - ((valor_dependente * dependentes) + pensao_alimenticia_valor + outras_deducoes_valor)

if base_calculo < 0:
    base_calculo = 0

if base_calculo <= 2428.80:
    aliquota = 0.0
    parcela_deduzir = 0.0
    faixa = "faixa 1"
elif base_calculo <= 2826.65:
    aliquota = 0.075
    parcela_deduzir = 182.16
    faixa = "faixa 2"
elif base_calculo <= 3751.05:
    aliquota = 0.15
    parcela_deduzir = 394.16
    faixa = "faixa 3"
elif base_calculo <= 4664.68:
    aliquota = 0.225
    parcela_deduzir = 675.49
    faixa = "faixa 4"
else:
    aliquota = 0.275
    parcela_deduzir = 908.73
    faixa = "faixa 5"

imposto = (base_calculo * aliquota) - parcela_deduzir

if imposto < 0:
    imposto = 0

print(f"Você se enquadra na {faixa}")
print(f"Alíquota nominal: {aliquota * 100:.1f}%")
print(f"Imposto devido: R$ {imposto:.2f}")