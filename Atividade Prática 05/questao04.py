from datetime import datetime

class QuantidadeDias:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def total_dias(self):
        dia_atual = datetime.today()
        data_inicial = datetime(self.ano, self.mes, self.dia)
        diferenca = dia_atual - data_inicial
        total_dias = diferenca.days
        return total_dias

if __name__ == "__main__":
    dia = int(input("Digite o dia: "))
    mes = int(input("Digite o mês: "))
    ano = int(input("Digite o ano: "))

    quantidade_dias = QuantidadeDias(dia, mes, ano)
    total = quantidade_dias.total_dias()
    print(f"Total de dias desde {dia}/{mes}/{ano} até hoje: {total} dias")