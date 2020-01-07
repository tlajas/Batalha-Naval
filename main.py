import jogadores as jogador
import tabuleiro as tab

def main():
    emjogo = False
    jogo = jogador.jogadores()       
    while True:
        line = input()
        if not line:
            break
        comandos = line.split(' ')

        if comandos[0] == 'RJ':
            comandosRJ(comandos, jogo)
        elif comandos[0] == 'EJ':
            comandosEJ(comandos, jogo)
        elif comandos[0] == 'LJ':
            comandosLJ(jogo)
        elif comandos[0] == 'IJ':
            comandosIJ(comandos, jogo)
        elif comandos[0] == 'IC':
            comandosIC(comandos, jogo)
        elif comandos[0] == 'D':
            comandosD(comandos, jogo)
        elif comandos[0] == 'CN':
            comandosCN(comandos, jogo)
        elif comandos[0] == 'RN':
            comandosRN(comandos , jogo)
        elif comandos[0] == 'T':
            comandosT(comandos, jogo)
        elif comandos[0] == 'V':
            comandosV(comandos, jogo)
        elif comandos[0] == 'G':
            comandosG(comandos, jogo)
        elif comandos[0] == 'L':
            comandosL(comandosL, jogo)
        else:
            print('Instrução inválida')

def comandosRJ(comandos, jogo):
    nome_jogador = comandos[1]
    if jogador.tem_jogador(jogo, nome_jogador):
        print('Jogador existente.')
    else:
        jogador.adicionar_jogadores(jogo, nome_jogador)
        print('Jogador registado com sucesso.')
    
    
def comandosEJ(comandos, jogo):
    nome_jogador = comandos[1]
    if jogador.esta_na_lista(jogo, nome_jogador):
        print ('Jogador não existente.')
    if emjogo:
        print('Jogador participa no jogo em curso.')
    else:
        jogador.remover_jogadores(jogo, nome_jogador)
        print ('Jogador removido com sucesso.')

def comandosLJ(jogo):
    jogador.listar_jogadores(jogo)

def comandosIJ(comandos, jogo):
    jogador_1 = comandos[1]
    jogador_2 = comandos[2]
    jogador.iniciar_jogo(jogo, jogador_1, jogador_2)
    emjogo = True    

def comandosIC(comandos, jogo):
    pass
def comandosD(comandos, jogo):
    pass
def comandosCN(comandos, jogo): 
    if comandos[4] == 'A':
        tab.tabuleiro_navios_j1_colunas(0)
    elif comandos[4] == 'B':
        tab.tabuleiro_navios_j1_colunas(1)
    elif comandos[4] == 'C':
        tab.tabuleiro_navios_j1_colunas(2)
    elif comandos[4] == 'D':
        tab.tabuleiro_navios_j1_colunas(3)
    elif comandos[4] == 'E':
        tab.tabuleiro_navios_j1_colunas(4)
    elif comandos[4] == 'F':
        tab.tabuleiro_navios_j1_colunas(5)
    elif comandos[4] == 'G':
        tab.tabuleiro_navios_j1_colunas(6)
    elif comandos[4] == 'H':
        tab.tabuleiro_navios_j1_colunas(7)
    elif comandos[4] == 'I':
        tab.tabuleiro_navios_j1_colunas(8)
    elif comandos[4] == 'J':
        tab.tabuleiro_navios_j1_colunas(9)

    
        
def comandosRN(comandos, jogo):
    pass
def comandosT(comandos, jogo):
    pass
def comandosV(comandos, jogo):
    pass
def comandosG(comandos, jogo):
    pass
def comandosL(comandos, jogo):
    pass


if __name__ == "__main__":
    main()