temperatura = float(input("Digite a temperatura: "))
unidade_origem = input("Digite a unidade da temperatura (C para Celsius, F para Fahrenheit, K para Kelvin): ").strip().upper()
unidade_destino = input("Digite a unidade para a qual deseja converter (C para Celsius, F para Fahrenheit, K para Kelvin): ").strip().upper()

if unidade_origem == 'C':
    if unidade_destino == 'F':
        fahrenheit = (temperatura * 9/5) + 32
        print(f"{temperatura}°C é igual a {fahrenheit:.2f}°F")

    elif unidade_destino == 'K':
        kelvin = temperatura + 273.15
        print(f"{temperatura}°C é igual a {kelvin:.2f}K")

    else:
        print("Conversão inválida.")

elif unidade_origem == 'F':
    if unidade_destino == 'C':
        celsius = (temperatura - 32) * 5/9
        print(f"{temperatura}°F é igual a {celsius:.2f}°C")

    elif unidade_destino == 'K':
        kelvin = (temperatura - 32) * 5/9 + 273.15
        print(f"{temperatura}°F é igual a {kelvin:.2f}K")

    else:
        print("Conversão inválida.")

elif unidade_origem == 'K':
    if unidade_destino == 'C':
        celsius = temperatura - 273.15
        print(f"{temperatura}K é igual a {celsius:.2f}°C")

    elif unidade_destino == 'F':
        fahrenheit = (temperatura - 273.15) * 9/5 + 32
        print(f"{temperatura}K é igual a {fahrenheit:.2f}°F")
        
    else:
        print("Conversão inválida.")