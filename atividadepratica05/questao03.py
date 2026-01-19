class PrecoFinal:
    def __init__(self, valor_produto, percentual_desconto):
        self.valor_produto = valor_produto
        self.percentual_desconto = percentual_desconto

    def calcular_desconto(self):
        calculo_desconto = self.valor_produto * (self.percentual_desconto / 100)
        return calculo_desconto

    def valor_total(self):
        valor_final = self.valor_produto - self.calcular_desconto()
        return valor_final


if __name__ == "__main__":
    valor_produto = float(input("Digite o valor da conta: "))
    percentual_desconto = float(input("Digite o percentual do desconto (%): "))

    gorjeta = PrecoFinal(valor_produto, percentual_desconto)
    valor_desconto = gorjeta.calcular_desconto()
    valor_total = gorjeta.valor_total()

    print(f"Valor do produto: R$ {valor_produto:.2f}")
    print(f"Valor do desconto: R$ {valor_desconto:.2f}")
    print(f"Valor total do produto com desconto: R$ {valor_total:.2f}")