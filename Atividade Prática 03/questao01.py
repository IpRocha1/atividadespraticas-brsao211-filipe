idade = int(input("Digite sua idade: "))

if idade >= 0 and idade <= 12:
    print("Criança (0-12 anos)")
elif idade > 12 and idade <= 17:
    print("Adolescente (13-17 anos)")
elif idade > 17 and idade <= 59:
    print("Adulto (18-59 anos)")
elif idade >= 60:
    print("Idoso (60 anos ou mais)")