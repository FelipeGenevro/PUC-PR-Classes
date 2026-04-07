#Algoritmo que calcula quantos reais serão obtidos após x dias de 1 real dobrando diariamente

dias = int(input("digite por quantos dias você quer que 1 real dobre:"))
valor = 1
valor_final = 0
for i in range(dias):
    valor *= 2
    valor_final += valor

resultado = valor_final + 1

print(f"você terá R${resultado:,} reais no total após {dias} dias dobrando o valor")