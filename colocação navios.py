import tabuleiro as tab
import navios

def colocar_navios(jogador, tipo):
    if jogador == jogador_1:
        for navios1 in navios.navios_disponiveis_j1:
            if tipo == navios1['codigo']:
                navios1['quantidade'] -= 1
    elif jogador == jogador_2:
        for navios2 in navios.navios_disponiveis_j2:
            if tipo == navios2['codigo']:
                navios2['quantidade'] -= 1
    

for navios1 in navios.navios_disponiveis_j1:
    print(navios1)    
