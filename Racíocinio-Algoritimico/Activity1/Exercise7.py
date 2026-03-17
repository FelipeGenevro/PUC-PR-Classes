#algoritmo que calcula o preço total de uma fábrica a partir do preço de custo junto a 2 taxas fixas

prod_cost = float(input('Digite o valor de custo de fábrica do produto: '))

tax_1 = prod_cost * 0.28
tax_2 = prod_cost * 0.45

total_cost = prod_cost + tax_1 + tax_2

print(f"o valor total de produção é de {total_cost} reais")