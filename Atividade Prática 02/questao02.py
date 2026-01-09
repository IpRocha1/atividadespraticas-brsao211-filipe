nome_do_produto = input("Digite o nome do produto: ")
preco_original = float(input("Digite o preço original do produto (R$): "))
desconto = 0.2  # 20% de desconto

desconto = preco_original * desconto
preco_final = preco_original - desconto

print("Produto:", nome_do_produto)
print("Preço Original: R$ %.2f" % preco_original)
print("Desconto: R$ %.2f" % desconto)
print("Preço Final: R$ %.2f" % preco_final)