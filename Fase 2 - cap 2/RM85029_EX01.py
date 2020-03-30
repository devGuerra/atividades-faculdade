peso = float(input("Digite o seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura ** 2)
status = 'Bom'

if imc < 16:
    status = 'Baixo peso Grau III'
elif imc >= 16 and imc <= 16.99:
    status = "Baixo peso Grau II"
elif imc >= 17 and imc <= 18.49:
    status = "Baixo peso Grau I"
elif imc >= 18.50 and imc <= 24.99:
    status = "peso ideal"
elif imc >= 25 and imc <= 29.99:
    status = "Sobrepeso"
elif imc >= 30 and imc <= 34.99:
    status = "Obesidade Grau I"
elif imc >= 35 and imc <= 39.99:
    status = "Obesidade Grau II"
else:
    status = "Obesidade Grau III"

print('O seu imc é {:.1f}, você esta com {}.'.format(imc, status))