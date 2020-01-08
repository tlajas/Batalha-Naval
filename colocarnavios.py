import tabuleiro as tab
import navios
import jogadores
import main


def posicao():
    pass

def colocar_navios(jogadores):
    users = jogadores
    print(users)
    #if jogador == jogador_1:
    #    for navios1 in navios.navios_disponiveis_j1:
    #        if tipo == navios1['codigo']:
    #            navios1['quantidade'] -= 1
#
    #        elif navios2['quantidade'] == 0:
    #            print('Não lhe restam mais navios desse tipo para colocar.')
    #elif jogador == jogador_2:
    #    for navios2 in navios.navios_disponiveis_j2:
    #        if tipo == navios2['codigo']:
    #            navios2['quantidade'] -= 1
    #        elif navios2['quantidade'] == 0:
    #            print('Não lhe restam mais navios desse tipo para colocar.')


def coordenadasj1():
    if comandos[4] == 'A':
        tab.tabuleiro_j1_colunas(0)
    elif comandos[4] == 'B':
        tab.tabuleiro_j1_colunas(1)
    elif comandos[4] == 'C':
        tab.tabuleiro_j1_colunas(2)
    elif comandos[4] == 'D':
        tab.tabuleiro_j1_colunas(3)
    elif comandos[4] == 'E':
        tab.tabuleiro_j1_colunas(4)
    elif comandos[4] == 'F':
        tab.tabuleiro_j1_colunas(5)
    elif comandos[4] == 'G':
        tab.tabuleiro_j1_colunas(6)
    elif comandos[4] == 'H':
        tab.tabuleiro_j1_colunas(7)
    elif comandos[4] == 'I':
        tab.tabuleiro_j1_colunas(8)
    elif comandos[4] == 'J':
        tab.tabuleiro_j1_colunas(9)


def coordenadasj2():
    if comandos[4] == 'A':
        tab.tabuleiro_j2_colunas(0)
    elif comandos[4] == 'B':
        tab.tabuleiro_j2_colunas(1)
    elif comandos[4] == 'C':
        tab.tabuleiro_j2_colunas(2)
    elif comandos[4] == 'D':
        tab.tabuleiro_j2_colunas(3)
    elif comandos[4] == 'E':
        tab.tabuleiro_j2_colunas(4)
    elif comandos[4] == 'F':
        tab.tabuleiro_j2_colunas(5)
    elif comandos[4] == 'G':
        tab.tabuleiro_j2_colunas(6)
    elif comandos[4] == 'H':
        tab.tabuleiro_j2_colunas(7)
    elif comandos[4] == 'I':
        tab.tabuleiro_j2_colunas(8)
    elif comandos[4] == 'J':
        tab.tabuleiro_j2_colunas(9)
        
