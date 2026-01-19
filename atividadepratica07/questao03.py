import csv
class LeituraArquivo:
    def __init__(self, arquivo):
        self.arquivo = f"atividadepratica07/{arquivo}"

    def exibir_conteudo(self):
        try:
            with open(self.arquivo, 'r', newline='', encoding ='utf-8') as file:
                arquivo_csv = csv.reader(file)
                print("Conteúdo do arquivo:")
                for linha in arquivo_csv:
                    print(', '.join(linha))                
        except FileNotFoundError:
            print(f"Erro: O arquivo '{self.arquivo}' não foi encontrado.")
        except Exception as e:
            print(f"Ocorreu um erro ao ler o arquivo: {e}")

if __name__ == "__main__":
    nome_arquivo = input("Digite o nome do arquivo a ser lido (ex: dados_pessoais.csv): ")
    leitura_arquivo = LeituraArquivo(nome_arquivo)
    leitura_arquivo.exibir_conteudo()