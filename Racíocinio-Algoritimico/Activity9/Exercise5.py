def somaImposto(taxaImposto, custo):
    imposto = custo * (taxaImposto / 100)
    custo_final = custo + imposto
    return custo_final


# Entrada de dados
custo = float(input("Digite o custo do produto: R$ "))
taxa = float(input("Digite a taxa de imposto (%): "))

# Cálculo
valor_final = somaImposto(taxa, custo)

# Resultado
print(f"Valor final com imposto: R$ {valor_final:.2f}")