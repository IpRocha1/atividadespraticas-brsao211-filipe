valor_real = float(input("Digite o valor em reais (R$): "))
dolar = 5.25
euro = 6.15

valor_dolar = valor_real / dolar
valor_euro = valor_real / euro

print(f"O valor em dólares é: U$ {valor_dolar:.2f}")
print(f"O valor em euros é: € {valor_euro:.2f}")