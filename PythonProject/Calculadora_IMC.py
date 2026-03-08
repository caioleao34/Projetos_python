#calculadora IMC
peso = float(input("quantos quilos você pesa?\n"))
altura = float(input("qual a sua altura?\n"))

#cáculo do peso do índice de massa corporal
imc = peso / altura**2

if imc < 18.5:
    print(f'Voce está baixo do peso! seu índice: {imc:.2f})')
elif 18.5 <= imc <= 25:
    print(f'seu peso etá normal! seu índice:{imc:.2f}')
elif 25 <= imc <= 30:
    print(f'Você está acima do peso! seu índice: {imc:.2f}')
else:
    print(f'Você está obeso! seu índice: {imc:.2f}')