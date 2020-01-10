import jogadores as jogador
import navios

jogador_1 = ''
jogador_2 = ''
emjogo = False

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


def comandosRJ(nome, jogo):
    nome_jogador = nome
    if jogador.tem_jogador(jogo, nome_jogador):
        print('Jogador existente.')
        return 0
    else:
        jogador.adicionar_jogadores(jogo, nome_jogador)
        print('Jogador registado com sucesso.')
        return nome_jogador
    
    
def comandosEJ(comandos, jogo):
    nome_jogador = comandos[1]
    if jogador.esta_na_lista(jogo, nome_jogador):
        print ('Jogador não existente.')
    else:
        jogador.remover_jogadores(jogo, nome_jogador)
        print ('Jogador removido com sucesso.')


def comandosLJ(jogo):
    jogador.listar_jogadores(jogo)


def comandosIJ(comandos, jogo):
    global emjogo
    global jogador_1
    global jogador_2
    jogador_1 = comandos[1]
    jogador_2 = comandos[2]
    if not emjogo:
        jogador.iniciar_jogo(jogo, jogador_1, jogador_2)
        emjogo = True
    elif emjogo:
        print('Existe um jogo em curso.')
    

def comandosIC(comandos, jogo):
    pass

def comandosD(comandos, jogo):
    pass

def comandosCN(comandos, player, tipo, fila, coluna, orientacao):
    pass


        


#def orientacao_j1(comandos, player, tipo):
#    for navios1 in navios.navios_disponiveis_j1:
#        if comandos[5] == 'N' and navios_1['codigo'] == tipo:
#            
#
#            
#        elif comandos[5] == 'S':
#            colocar_sul()
#        elif comandos[5] == 'E':
#            colocar_este()
#        elif comandos[5] == 'O':
#            colocar_oeste()

def colunaj1(coluna):
    if coluna == 'A':
        tabuleiro_j1_colunas(0)
    elif coluna == 'B':
        tabuleiro_j1_colunas(1)
    elif coluna == 'C':
        tabuleiro_j1_colunas(2)
    elif coluna == 'D':
        tabuleiro_j1_colunas(3)
    elif coluna == 'E':
        tabuleiro_j1_colunas(4)
    elif coluna == 'F':
        tabuleiro_j1_colunas(5)
    elif coluna == 'G':
        tabuleiro_j1_colunas(6)
    elif coluna == 'H':
        tabuleiro_j1_colunas(7)
    elif coluna == 'I':
        tabuleiro_j1_colunas(8)
    elif coluna == 'J':
        tabuleiro_j1_colunas(9)

def colunaj2(coluna):
    if coluna == 'A':
        tabuleiro_j2_colunas(0)
    elif coluna == 'B':
        tabuleiro_j2_colunas(1)
    elif coluna == 'C':
        tabuleiro_j2_colunas(2)
    elif coluna == 'D':
        tabuleiro_j2_colunas(3)
    elif coluna == 'E':
        tabuleiro_j2_colunas(4)
    elif coluna == 'F':
        tabuleiro_j2_colunas(5)
    elif coluna == 'G':
        tabuleiro_j2_colunas(6)
    elif coluna == 'H':
        tabuleiro_j2_colunas(7)
    elif coluna == 'I':
        tabuleiro_j2_colunas(8)
    elif coluna == 'J':
        tabuleiro_j2_colunas(9)

def colocar_norte():
    pass

def colocar_sul():
    pass

def colocar_este():
    pass

def colocar_oeste():
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

def main():
    jogo = jogador.jogadores()
    nomes = []
    while True:
        line = input()
        if not line:
            break
        comandos = line.split(' ')

        if comandos[0] == 'RJ':
            nomes.append(comandosRJ(comandos[1], jogo))
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
            player = comandos[1]
            tipo = comandos[2]
            fila = comandos[3]
            coluna = comandos[4]
            orientacao = comandos[5]
            comandosCN(comandos, player, tipo, fila, coluna, orientacao)
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
            print(nomes)
            print('Instrução inválida')

if __name__ == "__main__":
    main()


   # if comandos[1] == jogador_1:
   #     for navios1 in navios.navios_disponiveis_j1:
   #         if tipo == navios1['codigo']:
   #             navios1['quantidade'] -= 1
   #         elif navios1['quantidade'] == 0:
   #             print('Não lhe restam mais navios desse tipo para colocar.')
   #     colunaj1(comandos)    
   #     
   # 
   # else:
   #     for navios2 in navios.navios_disponiveis_j2:
   #         if tipo == navios2['codigo']:
   #             navios2['quantidade'] -= 1
   #         elif navios2['quantidade'] == 0:
   #             print('Não lhe restam mais navios desse tipo para colocar.')
   #     colunaj2(comandos)