tabuleiro_navios_j1 = [[0 for c in range(1,11)] for r in range(0,10)]

tabuleiro_navios_j2 = [[0 for c in range(1,11)] for r in range(0,10)]

tabuleiro_ataques_j1 = [[0 for c in range(1,11)] for r in range(0,10)]

tabuleiro_ataques_j2 = [[0 for c in range(1,11)] for r in range(0,10)]


def tabuleiro_navios_j1_colunas(coluna):
    for i in range(0,10):
        print(tabuleiro_navios_j1[i][coluna])

def tabuleiro_navios_j2_colunas(coluna):
    for i in range(0,10):
        tabuleiro_navios_j1[i][coluna])

def tabuleiro_ataques_j1_colunas(coluna):
    for i in range(0,10):
        print(tabuleiro_navios_j1[i][coluna])

def tabuleiro_ataques_j2_colunas(coluna):
    for i in range(0,10):
        print(tabuleiro_navios_j1[i][coluna])