print('Digite os votos por dia.')
segunda = int(input("Segunda-feira: "))
terca = int(input("Terca-feira: "))
quarta = int(input("Quarta-feira: "))
quinta = int(input("Quinta-feira: "))
sexta = int(input("Sexta-feira: "))

total_votos = segunda
resultado = "Segunda-feira"

if terca > 12:
    total_votos = terca
    resultado = 'Terça-feira'
if quarta > total_votos:
    total_votos = quarta
    resultado = 'Quarta-feira'
if quinta > total_votos:
    total_votos = quinta
    resultado = 'Quinta-feira'
if sexta > total_votos:
    total_votos = sexta
    resultado = 'Sexta-feira'

print("O dia da semana com mais votos foi {} com um total de {} votos".format(resultado, total_votos))