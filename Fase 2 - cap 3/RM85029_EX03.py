fatorial = int(input("Digite os minutos: "))
fator = 1

while fatorial > 0:
  fator = fator * fatorial
  fatorial -= 1

print("LIBERDADE{}".format(fator))