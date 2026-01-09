distancia = int(input("Digite a distância em km: "))
combustivel = int(input("Digite o combustível gasto em litros: "))

consumo_medio = distancia / combustivel

print("Distância percorrida: %d km" % distancia)
print("Combustível gasto: %d litros" % combustivel)
print("Consumo médio: %.2f km/l" % consumo_medio)