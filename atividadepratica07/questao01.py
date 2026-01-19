import pandas as pd

class TempoExecucao:
    def __init__(self, arquivo):
        self.arquivo = arquivo

    def processar_logs_treinamento(self):
        leitor = pd.read_csv(self.arquivo)
        media = leitor['tempo_execucao'].mean()
        desvio_padrao = leitor['tempo_execucao'].std()
        return media, desvio_padrao

if __name__ == "__main__":
    arquivo = "atividadepratica07/logs_treinamento.csv"
    tempo_execucao = TempoExecucao(arquivo)
    media, desvio_padrao = tempo_execucao.processar_logs_treinamento()
    print(f"Média de execução: {media:.2f}")
    print(f"Desvio padrão de execução: {desvio_padrao:.2f}")

