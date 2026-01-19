"Crie um programa que leia e escreva arquivos no formato , que salve em um dicionário com nome, idade e cidade em um arquivo JSON e depois leia o mesmo arquivo exibindo os dados, caso o arquivo não existir ou ocorrer erro ao salvar, mostre uma mensagem de falha."
import json

class Pessoa:
    def __init__(self, nome, idade, cidade):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade

    def to_dict(self):
        return {
            'nome': self.nome,
            'idade': self.idade,
            'cidade': self.cidade
        }
    
def salvar_pessoa_em_json(pessoa, nome_arquivo):
    try:
        with open(f"atividadepratica07/{nome_arquivo}", 'w') as arquivo_json:
            json.dump(pessoa.to_dict(), arquivo_json)
        print("Dados salvos com sucesso.")
    except Exception as e:
        print(f"Falha ao salvar os dados: {e}")
    
def ler_pessoa_de_json(nome_arquivo):
    try:
        with open(f"atividadepratica07/{nome_arquivo}", 'r') as arquivo_json:
            dados = json.load(arquivo_json)
            return dados
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except Exception as e:
        print(f"Falha ao ler os dados: {e}")
    return None

if __name__ == "__main__":
    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")
    cidade = input("Digite a cidade: ")

    pessoa = Pessoa(nome, idade, cidade)
    nome_arquivo_salvar = input("Digite o nome do arquivo JSON para salvar os dados: ")

    salvar_pessoa_em_json(pessoa, nome_arquivo_salvar)

    nome_arquivo_ler = input("Digite o nome do arquivo JSON para ler os dados: ")

    dados_lidos = ler_pessoa_de_json(nome_arquivo_ler)
    if dados_lidos:
        print("Dados lidos do arquivo JSON:")
        print(dados_lidos)