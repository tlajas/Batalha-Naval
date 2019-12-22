tabuleiro_navios_j1 = [[0 for c in range(1,11)] for r in range(0,10)]

tabuleiro_navios_j2 = [[0 for c in range(1,11)] for r in range(0,10)]

tabuleiro_ataques_j1 = [[0 for c in range(1,11)] for r in range(0,10)]

tabuleiro_ataques_j2 = [[0 for c in range(1,11)] for r in range(0,10)]

colunas_alfabeto = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}

def tabuleiro_navios_j1_colunas():
    for i in range(0, 10):
        for j in range(0 ,10):
            print(tabuleiro_navios_j1[i][j])
tabuleiro_navios_j1_colunas()


def tabuleiro_navios_j2():
    pass

def tabuleiro_ataques_j1():
    pass

def tabuleiro_ataques_j2():
    pass