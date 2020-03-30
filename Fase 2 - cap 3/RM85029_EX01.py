alimento = ''
calorias = 0.0
opt = -1

while opt != 3:
    print("=================================")
    print("Digite a opção:")
    print("1 - Adicionar nova refeição")
    print("2 - Consultar calorias do dia")
    print("3 - Sair")
    opt = int(input("Digite a opção: "))
    print("=================================")

    if opt == 1:
        alimento = input("Digite o alimento: ")
        calorias = calorias + float(input("Digite as calorias: "))
        print("Alimento adicionado.")

    elif opt == 2:
        print("As calorias consumidas no dia foram {}".format(calorias))

print("Obrigado por usar o programa.")
