par = 0
impar = 0

while True:

    numero = input("Digite um número inteiro positivo ou FIM para encerrar: ")

    if numero.upper() == "FIM":
        print("Encerrando o programa.")
        break

    try:
        numero = int(numero)
        if numero < 0:
            print("Por favor, digite um número inteiro positivo.")
            continue

        if numero%2 == 0:
            print(f"O número {numero} é par.")
            par += 1
        else:
            print(f"O número {numero} é ímpar.")
            impar += 1
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro positivo ou FIM para encerrar.")

print(f"Total de números pares: {par}")
print(f"Total de números ímpares: {impar}")
        