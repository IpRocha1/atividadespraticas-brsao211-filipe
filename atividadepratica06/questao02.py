import requests

class UsuarioAleatorio:
    def __init__(self):
        self.url = "https://randomuser.me/api/"

    def obter_usuario(self):
        resposta = requests.get(self.url)
        if resposta.status_code == 200:
            dados = resposta.json()
            usuario = dados['results'][0]
            return {
                'nome': f"{usuario['name']['first']} {usuario['name']['last']}",
                'email': usuario['email'],
                'pais': usuario['location']['country']
            }
        else:
            raise Exception("Erro ao obter dados do usuário.")

if __name__ == "__main__":
    gerador = UsuarioAleatorio()
    usuario = gerador.obter_usuario()
    print(f"Nome: {usuario['nome']}")
    print(f"Email: {usuario['email']}")
    print(f"País: {usuario['pais']}")