import pandas as pd

class DadosPessoais:
    def __init__(self):
        self.arquivo = "atividadepratica07/dados_pessoais.csv"

    def salvar_dados(self, dados):
        df = pd.DataFrame(dados)
        try:
            df.to_csv(self.arquivo, index=False)
        except Exception as e:
            print(f"Falha ao salvar os dados: {e}")

if __name__ == "__main__":
    dados = []
    try:
        while True:
            nome = input("Digite seu nome: ")
            idade = int(input("Digite sua idade: "))
            cidade = input("Digite sua cidade: ")
            dado = {
                'Nome': nome,
                'Idade': idade,
                'Cidade': cidade
            }
            dados.append(dado)
            if input("Deseja inserir novos dados? (s/n): ").lower() != 's':
                break
    except ValueError:
        print("Entrada inválida. Por favor, insira os dados corretamente.")
    dados_pessoais = DadosPessoais()
    dados_pessoais.salvar_dados(dados)