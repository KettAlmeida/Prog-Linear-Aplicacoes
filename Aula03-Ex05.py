# -----------------------------------------------------------------------------------------------------
#  Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e
#  no qual a soma das linhas, colunase diagonais é a mesma. Por exemplo, veja um quadrado
#  mágico de lado 3, com números de 1 a 9:
# ------------------------------------------------------------------------------------------------------

n = int(input("Tamanho da Matriz? "))

A = []
print('-=' * 20)
for l in range(n):
    x = []
    for c in range(n):
        x.append(int(input('Digite o valor de [' + str(l) + ',' + str(c) + ']:')))
    A.append(x)
# diagonal principal
magico = 0
for l in range(n):
    magico = magico + A[l][l]

# diagonal secundaria
soma = 0
for l in range(n):
    soma = soma + A[l][n - 1 - l]
if (soma != magico):
    print('-=' * 20)
    print("Não é um quadrado mágico :( ")
    exit()

# linhas
for l in range(n):
    soma = 0
    for c in range(n):
        soma = soma + A[l][c]
    if (soma != magico):
        print('-=' * 20)
        print("Não é um quadrado mágico :( ")
        exit()

# colunas
for c in range(n):
    soma = 0
    for l in range(n):
        soma = soma + A[l][c]
    if (soma != magico):
        print('-=' * 20)
        print("Não é um quadrado mágico :( ")
        exit()
print('-=' * 20)
print("É um quadrado mágico :) ")

print(A)
