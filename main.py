import jogadores as jogo

def main():
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
            comandosLJ(comandos, jogo)
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
    jogador_nome = comandos[1]
    if jogo.tem_jogador(jogadores, nome):
        print('Jogador existente')
    else:
        jogo.adicionar_jogador(jogadores, nome)
        print('Jogador registado com sucesso')
    
def comandosEJ(comandos, jogo):
    if jogo.jogadores['jogadores'] == []:
        print ('Jogador não existente')
    else:
        jogo.remover_jogadores
        print ('Jogador removido com sucesso')

def comandosLJ(comandos, jogo):
    pass
def comandosIJ(comandos, jogo):
    pass
def comandosIC(comandos, jogo):
    pass
def comandosD(comandos, jogo):
    pass
def comandosCN(comandos, jogo):
    pass
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