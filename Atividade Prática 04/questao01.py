while True:
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    operador = input("Digite o operador (+, -, *, /) ou 'sair' para encerrar: ")

    if operador.lower() == 'sair':
        print("Encerrando a calculadora. Até mais!")
        break

    try:
        if operador == '+':
            resultado = numero1 + numero2
        elif operador == '-':
            resultado = numero1 - numero2
        elif operador == '*':
            resultado = numero1 * numero2
        elif operador == '/':
            if numero2 == 0:
                print("Erro: Divisão por zero não é permitida.")
                continue
            resultado = numero1 / numero2
        else:
            print("Operador inválido. Por favor, tente novamente.")
            continue
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

    print(f"O resultado de {numero1} {operador} {numero2} é: {resultado}")