#KETTNEY ALMEIDA DOS SANTOS - ADM - MANHÃ - AULA04-EX01
def subtrair_matrizes(b, c):
    assert len(b) == len(c), "Números de linhas devem ser iguais"
    assert len(b[0]) == len(c[0]), "Números de colunas devem ser iguais"

    m = len(b)
    n = len(b[0])

    subtrair = []
    for i in range(m):
        linha = []
        subtrair.append(linha)
        for j in range(n):
            colula = b[i][j] - c[i][j]
            linha.append(colula)
    return subtrair


def soma_matrizes(a, subtrair):
    m = len(a)
    n = len(a[0])
    soma = []
    for i in range(m):
        linha = []
        soma.append(linha)
        for j in range(n):
            colula = a[i][j] + subtrair[i][j]
            linha.append(colula)
    return soma


def multiplicar_matrizes(b, soma):
    m = len(b)
    n = len(b[0])
    mult = []
    for i in range(m):
        linha = []
        mult.append(linha)
        for j in range(n):
            colula = b[i][j] * soma[i][j]
            linha.append(colula)
    return mult


def main():
    a = [
        [2, 1],
        [-3, 4]
    ]
    b = [
        [0, -1],
        [2, 5]
    ]

    c = [
        [3, 6],
        [0, 1]
    ]
    subtrair = subtrair_matrizes(b, c)
    print(f'(B-C_t): \n',subtrair)
    print('-=' * 5)
    soma = soma_matrizes(a, subtrair)
    print(f'[A+(B-C)]\n',soma)
    print('-=' * 5)
    mult = multiplicar_matrizes(b, soma)
    print(f'[A+(B-C)]*B\n',mult)

main()