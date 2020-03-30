mediaInpar = 0.0
mediaPar = 0.0
aluno = 0

print("===================")
print("Digite a nota dos alunos IMPARES")
for x in range(1, 51, 2):
  notaInpar = float(input("Digite a nota do aluno {}: ".format(x)))
  mediaInpar = mediaInpar + notaInpar

print("===================")
print("Digite a nota dos alunos PARES")
print("Alunos par: ")
for x in range(2, 51, 2):
  notaPar = float(input("Digite a nota do aluno {}: ".format(x)))
  mediaPar = mediaPar + notaPar

print("A media dos alunos ímpares é {}".format(mediaInpar/25))
print("A media dos alunos pares é {}".format(mediaPar/25))