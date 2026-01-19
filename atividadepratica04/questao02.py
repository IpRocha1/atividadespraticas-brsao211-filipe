notas = []

while True:
        nota = input("Digite uma nota de 0 a 10 e FIM para encerrar: ").upper()

        if nota == 'FIM':
            break
        
        try:
            nota = int(nota)

            if nota < 0 or nota > 10:
                print("Por favor, digite um número entre 0 e 10.")
                continue

            notas.append(nota)

        except ValueError:
            print("Entrada inválida. Por favor, digite um número entre 0 e 10.")
        
if len(notas) > 0:
    media = sum(notas) / len(notas)
    print(f"A média das notas é: {media:.2f}")
else:
    print("Nenhuma nota foi inserida.")