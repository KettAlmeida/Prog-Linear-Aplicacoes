#KETTNEY ALMEIDA DOS SANTOS - ADM - MANHÃ - AULA04-EX02

def soma_matrizes(at, b):
    assert len(at) == len(b), "Números de linhas devem ser iguais"
    assert len(at[0]) == len(b[0]), "Números de colunas devem ser iguais"

    m = len(at)
    n = len(at[0])
    soma = []
    for i in range(m):
        linha = []
        soma.append(linha)
        for j in range(n):
            coluna = at[i][j] + b[i][j]
            linha.append(coluna)
    return soma


def multx_matrizes(soma, c):
    m = len(soma)
    n = len(soma[0])
    multx = []
    for i in range(m):
        linha = []
        multx.append(linha)
        for j in range(n):
            coluna = soma[i][j] * c[i][j] -1
            linha.append(coluna)
    return multx

def subtrair_matrizes(multx, v_3):

    m = len(multx)
    n = len(multx[0])

    subtrair = []
    for i in range(m):
        linha = []
        subtrair.append(linha)
        for j in range(n):
            coluna = multx[i][j] - v_3[i][j]
            linha.append(coluna)
    return subtrair



def main():
    a = [
        [2, 1],
        [-3, 4]
    ]
    at = [
        [2, -3],
        [1, 4]
    ]
    b = [
        [0, -1],
        [2, 5]
    ]
    bt = [
        [0, -1],
        [2, 5]
    ]
    c = [
        [3, 6],
        [0, 1]
    ]

    v_3 = [
        [0, -3],
        [6, 15]
    ]

    soma = soma_matrizes(at, b)
    print(f'B+A_t :\n',soma)
    print('-=' * 5)
    multx = multx_matrizes(soma, c)
    print(f'(B+A_T)*C-1 :\n',multx)
    print('-=' * 5)
    print(f'3*B :\n',v_3)
    print('-=' * 5)
    subtrair = subtrair_matrizes(multx, v_3)
    print(f'(B+A-t)*C-1 - (3*B_t) :\n',subtrair)

main()