import jogadores as jogador
import navios

jogador_1 = ''
jogador_2 = ''
emjogo = False
navio1 = navios.navios_disponiveis_j1
navio2 = navios.navios_disponiveis_j2

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
    

def comandosIC():
    print(tabuleiro_j1)
    print(tabuleiro_j2)

def comandosD(comandos, jogo):
    pass

def comandosCN(player, tipo, linha, coluna, orientacao):
    if jogador.jogadores_em_jogo[0] == player:
        for n in navio1['tipos_de_navios']:
            for chave in n:
                if chave == tipo:
                    if n[chave]['quantidade'] == 0:
                        print('Não existem mais navios deste tipo.')    
                    else:
                        if orientacao == 'N':
                            colocar_norte_j1()
                            n[chave]['quantidade'] -= 1
                        elif orientacao == 'S':
                            colocar_sul_j1()
                            n[chave]['quantidade'] -= 1
                        elif orientacao == 'E':
                            colocar_este_j1(linha, coluna, tipo)
                            n[chave]['quantidade'] -= 1
                        elif orientacao == 'O':
                            colocar_oeste_j1(linha, coluna, tipo)
                            n[chave]['quantidade'] -= 1
                    
    elif jogador.jogadores_em_jogo[1] == player:
        for n in navio2['tipos_de_navios']:
            for chave in n:
                if chave == tipo:
                    if n[chave]['quantidade'] == 0 :
                        print('Não existem mais navios deste tipo.')
                    else:
                            if orientacao == 'N':
                                colocar_norte_j2()
                                n[chave]['quantidade'] -= 1
                            elif orientacao == 'S':
                                colocar_sul_j2()
                                n[chave]['quantidade'] -= 1
                            elif orientacao == 'E':
                                colocar_este_j2(linha, coluna, tipo)
                                n[chave]['quantidade'] -= 1
                            elif orientacao == 'O':
                                colocar_oeste_j2(linha, coluna, tipo)
                                n[chave]['quantidade'] -= 1



def get_tamanho(tipo):
    for i in navio1['tipos_de_navios']:
        for chave in i:
            if chave == tipo:
                tamanho = i[chave]['tamanho']
                return tamanho


def colocar_norte_j1():
    pass

def colocar_norte_j2():
    pass

def colocar_sul_j1():
    pass

def colocar_sul_j2():
    pass

def colocar_este_j1(linha, coluna, tipo):
    gt = get_tamanho(tipo)
    a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    for u in range(0, gt):
        tabuleiro_j1[int(linha)-1][a.index(coluna) + u] = 1


def colocar_este_j2(linha, coluna, tipo):
    gt = get_tamanho(tipo)
    a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    for u in range(0, gt):
        tabuleiro_j2[int(linha)-1][a.index(coluna) + u] = 1

def colocar_oeste_j1(linha, coluna, tipo):
    gt = get_tamanho(tipo)
    a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    for u in range(0, gt):
        tabuleiro_j1[int(linha)-1][a.index(coluna) - u] = 1

def colocar_oeste_j2(linha, coluna, tipo):
    gt = get_tamanho(tipo)
    a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    for u in range(0, gt):
        tabuleiro_j2[int(linha)-1][a.index(coluna) - u] = 1
        
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
            comandosIC()
        elif comandos[0] == 'D':
            comandosD(comandos, jogo)
        elif comandos[0] == 'CN':
            player = comandos[1]
            tipo = comandos[2]
            linha = comandos[3]
            coluna = comandos[4]
            orientacao = comandos[5]
            comandosCN(player, tipo, linha, coluna, orientacao)
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