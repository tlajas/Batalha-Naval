tabuleiro_j1 = []
for i in range(10):
    tabuleiro_linha = []
    for j in range(10):
        tabuleiro_linha.append(0)
    tabuleiro_j1.append(tabuleiro_linha)


tabuleiro_j2 = []
for i in range(10):
    tabuleiro_linha = []
    for j in range(10):
        tabuleiro_linha.append(0)
    tabuleiro_j2.append(tabuleiro_linha)



def tabuleiro_j1_colunas(coluna):
    for i in range(0,10):
        tabuleiro_j1[i][coluna] = 1

def tabuleiro_j2_colunas(coluna):
    for i in range(0,10):
        tabuleiro_j2[i][coluna] = 1

