import jogadores as jogador
import navios
import pickle

jogador_1 = ''
jogador_2 = ''
emjogo = False
emcombate = False
navio1 = navios.navios_disponiveis_j1
navio2 = navios.navios_disponiveis_j2
navios_para_remover = []
navios_para_remover2 = []


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


def comandosIJ(comandos):
    global jogador_1
    global jogador_2
    jogador_1 = comandos[1]
    jogador_2 = comandos[2]
    if not jogador.em_jogo:
        jogador.iniciar_jogo(jogador_1, jogador_2)
    elif jogador.em_jogo:
        print('Existe um jogo em curso.')


def comandosIC():
    global emcombate
    for n in navio1['tipos_de_navios']:
        for chave in n:
            t = n[chave]['quantidade']
    for i in navio2['tipos_de_navios']:
        for key in i:
            g = i[key]['quantidade']
    if emcombate == False and g == 0 and t == 0 and jogador.em_jogo == True:
        emcombate = True
        print('Combate iniciado.')
    elif g != 0 and t != 0 and jogador.em_jogo == True:
        print('Navios não colocados.')
    elif emcombate == True:
        print('Combate já foi iniciado.')
    elif not jogador.em_jogo:
        print('Não existe jogo em curso.')


def get_tamanho(tipo):
    for i in navio1['tipos_de_navios']:
        for chave in i:
            if chave == tipo:
                tamanho = i[chave]['tamanho']
                return tamanho


def comandosCN(player, tipo, linha, coluna, orientacao):
    if player == jogador.jogadores_em_jogo[0]:
        for n in navio1['tipos_de_navios']:
            for chave in n:
                if chave == tipo:
                    if n[chave]['quantidade'] == 0:
                        print('Não existem mais navios deste tipo.')    
                    else:
                        if orientacao == 'N':
                            colocar_norte_j1(linha, coluna, tipo)                           
                        elif orientacao == 'S':
                            colocar_sul_j1(linha, coluna, tipo)             
                        elif orientacao == 'E':
                            colocar_este_j1(linha, coluna, tipo)
                        elif orientacao == 'O':
                            colocar_oeste_j1(linha, coluna, tipo)
                                             
    elif player == jogador.jogadores_em_jogo[1]:
        for n in navio2['tipos_de_navios']:
            for chave in n:
                if chave == tipo:
                    if n[chave]['quantidade'] == 0 :
                        print('Não tem mais navios dessa tipologia disponíveis.')
                    else:
                            if orientacao == 'N':
                                colocar_norte_j2(linha, coluna, tipo)                             
                            elif orientacao == 'S':
                                colocar_sul_j2(linha, coluna, tipo)                              
                            elif orientacao == 'E':
                                colocar_este_j2(linha, coluna, tipo)                
                            elif orientacao == 'O':
                                colocar_oeste_j2(linha, coluna, tipo)
                           
    elif player not in jogador.jogadores_em_jogo[0] or player not in jogador.jogadores_em_jogo[1]:
        print('Jogador não participa no jogo em curso.')
    
    elif jogador.jogadores_em_jogo == []:
        print('Não existe jogo em curso.')


def colocar_norte_j1(linha, coluna, tipo):
    l = []
    gt = get_tamanho(tipo)
    a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    if a.index(coluna) > 10 or a.index(coluna) < 0 or int(linha)-1 > 10 or int(linha)-1 < 0 or int(linha)-1 - gt < -1:
        print('Posição irregular.') 
    else:
        for u in range(0, gt):
            tabuleiro_j1[int(linha)- 1 - u][a.index(coluna)] = 1
            l.append(a[a.index(coluna) + u]+ str(int(linha) - u))
        navios_para_remover.append(l)
        for n in navio1['tipos_de_navios']:
            for chave in n:
                if chave == tipo:
                    n[chave]['quantidade'] -= 1
        print('Navio colocado com sucesso.')

def colocar_norte_j2(linha, coluna, tipo):
    l = []
    gt = get_tamanho(tipo)
    a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    if a.index(coluna) > 10 or a.index(coluna) < 0 or int(linha)-1 > 10 or int(linha)-1 < 0 or int(linha)-1 - gt < -1:
        print('Posição irregular.') 
    else:
        for u in range(0, gt):
            tabuleiro_j2[int(linha)- 1 - u][a.index(coluna)] = 1
            l.append(a[a.index(coluna) + u]+ str(int(linha) - u))
        navios_para_remover2.append(l)
        for n in navio2['tipos_de_navios']:
            for chave in n:
                if chave == tipo:
                    n[chave]['quantidade'] -= 1
        print('Navio colocado com sucesso.')

def colocar_sul_j1(linha, coluna, tipo):
    l = []
    gt = get_tamanho(tipo)
    a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    if a.index(coluna) > 10 or a.index(coluna) < 0 or int(linha)-1 > 10 or int(linha)-1 < 0 or int(linha)-1 + gt < -1:
        print('Posição irregular.') 
    else:
        for u in range(0, gt):
            tabuleiro_j1[int(linha)- 1 + u][a.index(coluna)] = 1
            l.append(a[a.index(coluna) + u]+ str(int(linha) - u))
        navios_para_remover.append(l)
        for n in navio1['tipos_de_navios']:
            for chave in n:
                if chave == tipo:
                    n[chave]['quantidade'] -= 1
        print('Navio colocado com sucesso.')

def colocar_sul_j2(linha, coluna, tipo):
    l = []
    gt = get_tamanho(tipo)
    a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    if a.index(coluna) > 10 or a.index(coluna) < 0 or int(linha)-1 > 10 or int(linha)-1 < 0 or int(linha)-1 + gt < -1:
        print('Posição irregular.') 
    else:
        for u in range(0, gt):
            tabuleiro_j2[int(linha)- 1 + u][a.index(coluna)] = 1
            l.append(a[a.index(coluna)]+ str(int(linha) + u))
        navios_para_remover2.append(l)
        for n in navio2['tipos_de_navios']:
            for chave in n:
                if chave == tipo:
                    n[chave]['quantidade'] -= 1
        print('Navio colocado com sucesso.')

def colocar_este_j1(linha, coluna, tipo):
    l = []
    gt = get_tamanho(tipo)
    a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    if a.index(coluna) > 10 or a.index(coluna) < 0 or int(linha)-1 > 10 or int(linha)-1 < 0 or a.index(coluna) + gt > 10:
        print('Posição irregular.') 
    else:
        for u in range(0, gt):
            tabuleiro_j1[int(linha)-1][a.index(coluna) + u] = 1
            l.append(a[a.index(coluna) + u]+ str(linha))
        navios_para_remover.append(l)
        for n in navio1['tipos_de_navios']:
            for chave in n:
                if chave == tipo:
                    n[chave]['quantidade'] -= 1
        print('Navio colocado com sucesso.')


def colocar_este_j2(linha, coluna, tipo):
    l = []
    gt = get_tamanho(tipo)
    a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    if a.index(coluna) + gt > 10 or int(linha)-1 > 10 or int(linha)-1 < 0:
        print('Posição irregular.')
    else:
        for u in range(0, gt):
            tabuleiro_j2[int(linha)-1][a.index(coluna) + u] = 1
            l.append(a[a.index(coluna) + u]+ str(linha))
        navios_para_remover2.append(l)
        for n in navio2['tipos_de_navios']:
            for chave in n:
                if chave == tipo:
                    n[chave]['quantidade'] -= 1
        print('Navio colocado com sucesso.')
        

def colocar_oeste_j1(linha, coluna, tipo):
    l = []
    gt = get_tamanho(tipo)
    a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    if a.index(coluna) > 10 or a.index(coluna) < 0 or int(linha)-1 > 10 or int(linha)-1 < 0 or a.index(coluna) - gt > 10:
        print('Posição irregular.') 
    else:
        for u in range(0, gt):
            tabuleiro_j1[int(linha)-1][a.index(coluna) - u] = 1
            l.append(a[a.index(coluna) - u]+ str(linha))
        navios_para_remover.append(l)
        for n in navio1['tipos_de_navios']:
            for chave in n:
                if chave == tipo:
                    n[chave]['quantidade'] -= 1
        print('Navio colocado com sucesso.')

def colocar_oeste_j2(linha, coluna, tipo):
    l = []
    gt = get_tamanho(tipo)
    a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    if a.index(coluna) > 10 or a.index(coluna) < 0 or int(linha)-1 > 10 or int(linha)-1 < 0 or a.index(coluna) - gt > 10:
        print('Posição irregular.') 
    else:
        for u in range(0, gt):
            tabuleiro_j2[int(linha)-1][a.index(coluna) - u] = 1
            l.append(a[a.index(coluna) - u]+ str(linha))
        navios_para_remover2.append(l)
        for n in navio2['tipos_de_navios']:
            for chave in n:
                if chave == tipo:
                    n[chave]['quantidade'] -= 1
        print('Navio colocado com sucesso.')
        
def verificar_j1(linha, coluna):
    a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    if tabuleiro_j1[int(linha)-1][a.index(coluna)] == 0:
        return True
    else:
        return False

def verificar_j2(linha, coluna):
    a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    if tabuleiro_j2[int(linha)-1][a.index(coluna)] == 0:
        return True
    else:
        return False

def comandosRN(player, linha, coluna):
    if player == jogador.jogadores_em_jogo[0] and jogador.em_jogo == True:
        if verificar_j1(linha, coluna):
            print('Não existe navio na posição.')
        else:
            remover_j1(linha, coluna)
            print('Navio removido com sucesso.')
    elif player == jogador.jogadores_em_jogo[1]:
        if verificar_j2(linha, coluna):
            print('Não existe navio na posição.')
        else:
            remover_j2(linha, coluna)
            print('Navio removido com sucesso.')
    elif player not in jogador.jogadores_em_jogo:
        print('Jogador não participa no jogo em curso.')
    elif jogador.em_jogo == False:
        print('Não existe jogo em curso.')
       

def remover_j1(linha, coluna):
    col=[]
    a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    li=[]    
    for n in navios_para_remover:
        if coluna + str(linha) in n:            
            for i in n:
                col.append(i[0])
                li.append(i[1])                    
            for c in col:
                for num in li:
                    tabuleiro_j1[int(num) - 1][a.index(c)] = 0
            navios_para_remover.remove(n)

def remover_j2(linha, coluna):
    col=[]
    a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    li=[]
    for n in navios_para_remover2:
        if coluna + str(linha) in n:
            for i in n:
                col.append(i[0])
                li.append(i[1])
            for c in col:
                for num in li:
                    tabuleiro_j2[int(num) - 1][a.index(c)] = 0
            navios_para_remover2.remove(n)

def comandosD(comandos,jogo):
    pass
def comandosT(comandos, jogo):  
    pass
def comandosV(comandos, jogo):
    pass
def comandosG():
    pass
def comandosL():
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
            comandosIJ(comandos)
        elif comandos[0] == 'IC':
            comandosIC()
        elif comandos[0] == 'D':
            player = comandos[1]
            comandosD(comandos, jogo)
        elif comandos[0] == 'CN':
            player = comandos[1]
            tipo = comandos[2]
            linha = comandos[3]
            coluna = comandos[4]
            orientacao = comandos[5]
            comandosCN(player, tipo, linha, coluna, orientacao)
        elif comandos[0] == 'RN':
            player = comandos[1]
            linha = comandos[2]
            coluna = comandos[3]            
            comandosRN(player, linha, coluna)
        elif comandos[0] == 'T':
            comandosT(comandos, jogo)
        elif comandos[0] == 'V':
            comandosV(comandos, jogo)
        elif comandos[0] == 'G':
            comandosG()
        elif comandos[0] == 'L':
            comandosL()
        else:
            print(nomes)
            print('Instrução inválida')

if __name__ == "__main__":
    main()
