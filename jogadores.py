def jogadores():
    return {
        'jogador_1': [],
        'jogador_2': []
    } 

def adicionar_jogadores(jogo, nome):
    jogador_1 = {
        'nome' : nome
    }
    jogo['jogador_1'].append(jogador_1)

    jogador_2 = {
        'nome' : nome
    }
    jogo['jogador_2'].append(jogador_2)

def tem_jogador(jogo, nome):
    for jogador_1 in jogo['jogador_1']:
        if jogador_1['nome'] == nome:
            return True
    return False
    for jogador_2 in jogo['jogador_2']:
        if jogador_2['nome'] == nome:
            return True
    return False

def remover_jogadores(jogo, nome):
    for jogador in jogadores['jogadores']:
        if jogador_1['nome'] == nome:
            jogadores['jogadores'].remove(jogador1)
    for jogador in jogadores['jogadores']:
        if jogador_2['nome'] == nome:
            jogadores['jogadores'].remove(jogador2)

def listar_jogador(jogo, nome):
    jogadores['jogadores'].sort()
    print (jogadores['jogadores'])
    