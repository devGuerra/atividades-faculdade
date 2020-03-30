print('Os planos disponiveis sao: Basic, Silver, Gold, Platinum')
plano = input('Digite o seu plano: ').lower()
valor = float(input('Digite sua renda anual: R$ '))
porcentagem = 0

if plano == 'basic':
    porcentagem = 30
elif plano == 'silver':
    porcentagem = 20
elif plano == 'gold':
    porcentagem = 10
elif plano == 'platinum':
    porcentagem = 5
else:
    print('Plano não identificado')

taxa = valor * (porcentagem / 100)

if taxa > 0:
    print("A porcentagem do seu plano e {}% e a taxa anual R$ {:.2f}".format(str(porcentagem), taxa))