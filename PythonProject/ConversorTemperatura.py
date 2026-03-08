#Conversor de Temperatura ( Graus celcius, farenheit e kelvin)

uni_medida = input("qual unidade de temperatura você quer converter?\n").upper()
if uni_medida == "C":
    valorC = float(input("o valor da tempratura: \n"))
    medida2 = input("Para qual unidade de temperatura voce quer converter?\n").upper()
    if medida2 == "F":
        resultadoC_f = valorC * 9/5 + 32
        print(f'O valor de {valorC} graus celcius é igual a {resultadoC_f:.2f} fahrenheit.')
    elif medida2 == "K":
        resultadoC_k = valorC + 273.15
        print(f'O valor de {valorC} graus celcius é igual a {resultadoC_k:.2f} Kelvin.')
    else:
        print(f'{valorC:.2f} graus Celcius (não houve conversão!)')

elif uni_medida == "F":
    valorF = float(input("Qual o valor da temperatura? \n"))
    medida2 = input("Para qual unidade de temperatura voce quer converter?\n")
    if medida2 == "K":
        resultadoF_k = (valorF - 32) * 5 / 9 + 273.15
        print(f'O valor {valorF} graus fahrenheit é igual a {resultadoF_k:.2f} Kelvin.')
    elif medida2 == "C":
        resultadoC = (valorF-32)* 5/9
        print(f'O valor {valorF} graus fahrenheit é igual a {resultadoC:.2f} Celcius.')
    else:
        print(f'{valorF:.2f} graus fahrenheit (não houve conversão!)')

elif uni_medida == "K":
    valorK = float(input("Qual o valor da temperatura? \n"))
    medida2 = input("Para qual unidade você quer converter?\n")
    if medida2 == "F":
        resultadoK_f = (valorK - 273.15) * 9 / 5 + 32
        print(f'O valor {valorK} em kelvin para fahrenheit é igual a {resultadoK_f:.2f} Fahrenheit.')
    if medida2 == "C":
        resultadoK_c = valorK - 273.15
        print(f'O valor {valorK} em Kelvin para celcius é igual a {resultadoK_c:.2f} Celcius.')
    else:
        print(f'O valor é {valorK:.2f} (não houve conversão!)')
else:
    print(f'Digite uma medida de temperatura válida!!')