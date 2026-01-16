import random
import string

class Senha:
    def __init__(self, tamanho):
        self.tamanho_senha = tamanho

    def gerar_senha(self):
        caracteres = string.ascii_letters + string.digits + string.punctuation
        senha_gerada = ''.join(random.choice(caracteres) for _ in range(self.tamanho_senha))
        return senha_gerada

if __name__ == "__main__":
    tamanho = int(input("Digite o tamanho da senha desejada: "))
    senha = Senha(tamanho)
    senha_gerada = senha.gerar_senha()
    print(f"Senha gerada: {senha_gerada}")