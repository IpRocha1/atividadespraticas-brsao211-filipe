import requests

class CotacaoReal:
    def __init__(self, moeda):
        self.url = "https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
        self.moeda_destino = moeda

    def obter_cotacao(self):
        resposta = requests.get(self.url.format(moeda=self.moeda_destino))
        if resposta.status_code == 200:
            dados = resposta.json()
            chave = f"{self.moeda_destino}BRL"
            if chave in dados:
                valor_atual = float(dados[chave]['bid'])
                valor_maximo = float(dados[chave]['high'])
                valor_minimo = float(dados[chave]['low'])
                ultima_atualizacao = dados[chave]['create_date']
                return valor_atual, valor_maximo, valor_minimo, ultima_atualizacao
            else:
                raise Exception("Moeda não encontrada.")
        else:
            raise Exception("Erro ao obter dados da moeda.")

if __name__ == "__main__":
    moeda_input = input("Digite a sigla da moeda (ex: USD, EUR, GBP): ").upper()
    valor_atual = CotacaoReal(moeda_input)

    try:
        valor_cotacao, valor_maximo, valor_minimo, ultima_atualizacao = valor_atual.obter_cotacao()
        print(f"Cotação do {moeda_input} em relação ao Real: R$ {valor_cotacao:.2f}")
        print(f"Valor máximo: R$ {valor_maximo:.2f}")
        print(f"Valor mínimo: R$ {valor_minimo:.2f}")
        print(f"Última atualização: {ultima_atualizacao}")
    except Exception as e:
        print(e)