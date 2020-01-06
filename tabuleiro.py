tabuleiro_navios_j1 = []
for i in range(10):
    tabuleiro_linha = []
    for j in range(10):
        tabuleiro_linha.append(0)
    tabuleiro_navios_j1.append(tabuleiro_linha)


tabuleiro_navios_j2 = []
for i in range(10):
    tabuleiro_linha = []
    for j in range(10):
        tabuleiro_linha.append(0)
    tabuleiro_navios_j2.append(tabuleiro_linha)


tabuleiro_ataques_j1 = []
for i in range(10):
    tabuleiro_linha = []
    for j in range(10):
        tabuleiro_linha.append(0)
    tabuleiro_ataques_j1.append(tabuleiro_linha)
print(tabuleiro_ataques_j1)

                      
tabuleiro_ataques_j2 = []
for i in range(10):
    tabuleiro_linha = []
    for j in range(10):
        tabuleiro_linha.append(0)
    tabuleiro_ataques_j2.append(tabuleiro_linha)


def tabuleiro_navios_j1_colunas(coluna):
    for i in range(0,10):
        print(tabuleiro_navios_j1[i][coluna])

def tabuleiro_navios_j2_colunas(coluna):
    for i in range(0,10):
        print(tabuleiro_navios_j1[i][coluna])

def tabuleiro_ataques_j1_colunas(coluna):
    for i in range(0,10):
        print(tabuleiro_navios_j1[i][coluna])

def tabuleiro_ataques_j2_colunas(coluna):
    for i in range(0,10):
        print(tabuleiro_navios_j1[i][coluna])