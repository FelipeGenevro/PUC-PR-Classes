import sys

def calcular_orcamento(horas, minutos, colaboradores, km, pedagios,
                      taxa_hora=50, preco_gasolina=7, consumo_km_l=10,
                      pedagio_unit=19.9, desgaste_km=1):

    if colaboradores < 1:
        print("O projeto deve ter pelo menos 1 pessoa!")
        sys.exit()

    if horas < 0 or minutos < 0 or km < 0 or pedagios < 0:
        print("Valores não podem ser negativos!")
        sys.exit()

    # IDA + VOLTA
    tempo_horas_ida = (horas * 60 + minutos) / 60
    tempo_horas_total = tempo_horas_ida * 2

    km_total = km * 2
    pedagios_total = pedagios * 2

    # Deslocamento
    valor_deslocamento = taxa_hora * tempo_horas_total * colaboradores
    valor_individual = taxa_hora * tempo_horas_total

    # Combustível
    litros = km_total / consumo_km_l
    valor_gasolina = litros * preco_gasolina

    # Outros custos
    valor_pedagios = pedagios_total * pedagio_unit
    desgaste = km_total * desgaste_km

    valor_total = valor_deslocamento + valor_gasolina + valor_pedagios + desgaste

    return {
        "tempo_total": tempo_horas_total,
        "km_total": km_total,
        "pedagios_total": pedagios_total,
        "deslocamento": valor_deslocamento,
        "individual": valor_individual,
        "gasolina": valor_gasolina,
        "pedagios": valor_pedagios,
        "desgaste": desgaste,
        "total": valor_total
    }


# INPUT
horas = int(input("Horas da ida: "))
minutos = int(input("Minutos da ida: "))
colaboradores = int(input("Colaboradores: "))
km = float(input("Distância da ida (km): "))
pedagios = int(input("Pedágios da ida: "))

resultado = calcular_orcamento(horas, minutos, colaboradores, km, pedagios)

print("\n------------------------------")
print(f"Tempo total ida + volta: {resultado['tempo_total']:.2f}h")
print(f"KM total ida + volta: {resultado['km_total']:.2f} km")
print(f"Pedágios ida + volta: {resultado['pedagios_total']}")
print("------------------------------")
print(f"Deslocamento: R${resultado['deslocamento']:.2f}")
print(f"Gasolina: R${resultado['gasolina']:.2f}")
print(f"Pedágios: R${resultado['pedagios']:.2f}")
print(f"Desgaste: R${resultado['desgaste']:.2f}")
print("------------------------------")
print(f"TOTAL: R${resultado['total']:.2f}")