while True:

    senha = input("Digite a senha (ou 'fim' para encerrar): ")

    if senha.lower() == 'fim':
        print("Encerrando o programa.")
        break

    try:
        if len(senha) < 8:
            raise ValueError("Senha deve ter pelo menos 8 caracteres.")
        
        if not any(char.isdigit() for char in senha):
            raise ValueError("Senha deve conter pelo menos um número.")
        
        if len(senha) >= 8 and any(char.isdigit() for char in senha):
            print("Senha válida.")
            break
    
    except ValueError as e:
        print(f"Erro: {e}")