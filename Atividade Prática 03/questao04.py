ano = int(input("Digite um ano: "))

bissexto = ano % 4

if (bissexto == 0 and ano % 100 != 0) or ano % 400 == 0:
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")