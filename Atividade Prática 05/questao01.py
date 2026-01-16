class Gorjeta:
    def __init__(self, valor_conta, percentual_gorjeta):
        self.valor_conta = valor_conta
        self.percentual_gorjeta = percentual_gorjeta

    def calcularGorjeta(self):
        calculo_gorjeta = self.valor_conta * (self.percentual_gorjeta / 100)
        return calculo_gorjeta

    def valorTotal(self):
        valor_final = self.valor_conta + self.calcularGorjeta()
        return valor_final


if __name__ == "__main__":
    valor_conta = float(input("Digite o valor da conta: "))
    percentual_gorjeta = float(input("Digite o percentual da gorjeta (%): "))

    gorjeta = Gorjeta(valor_conta, percentual_gorjeta)
    valor_gorjeta = gorjeta.calcularGorjeta()
    valor_total = gorjeta.valorTotal()

    print(f"Valor da gorjeta: R$ {valor_gorjeta:.2f}")
    print(f"Valor total da conta com gorjeta: R$ {valor_total:.2f}")