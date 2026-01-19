class Palindromo:
    def __init__(self, texto):
        self.texto = texto

    def eh_palindromo(self):
        texto_limpo = ''.join(filter(str.isalnum, self.texto)).lower()
        return texto_limpo == texto_limpo[::-1]
    
if __name__ == "__main__":
    texto_inicial = input("Digite uma frase para verificar se é um polidromo: ")
    palindromo = Palindromo(texto_inicial)
    
    if palindromo.eh_palindromo():
        print(f'"{texto_inicial}" é um polidromo.')
    else:
        print(f'"{texto_inicial}" não é um polidromo.')