import requests

class CEP:
    def __init__(self, cep):
        self.cep = cep
        self.url = f"https://viacep.com.br/ws/{cep}/json/"

    def obter_endereco(self):
        resposta = requests.get(self.url)
        if resposta.status_code == 200:
            dados = resposta.json()
            if 'erro' in dados:
                raise Exception("CEP não encontrado.")
            return {
                'logradouro': dados.get('logradouro', ''),
                'bairro': dados.get('bairro', ''),
                'cidade': dados.get('localidade', ''),
                'estado': dados.get('uf', '')
            }
        else:
            raise Exception("Erro ao obter dados do CEP.")
        
if __name__ == "__main__":
    cep_input = input("Digite o CEP (somente números): ")
    cep = CEP(cep_input)
    try:
        endereco = cep.obter_endereco()
        print(f"Logradouro: {endereco['logradouro']}")
        print(f"Bairro: {endereco['bairro']}")
        print(f"Cidade: {endereco['cidade']}")
        print(f"Estado: {endereco['estado']}")
    except Exception as e:
        print(e)