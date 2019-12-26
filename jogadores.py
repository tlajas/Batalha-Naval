def jogadores():
    return {
        'jogadores': []
    } 

def adicionar_jogadores(jogadores, nome):
    jogador_1 = {
        'nome' : nome
    }
    jogadores['jogadores'].append(jogador_1)

    jogador_2 = {
        'nome' : nome
    }
    jogadores['jogadores'].append(jogador_2)

def tem_jogador(jogadores, nome):
    for jogador in jogadores['jogadores']:
        if jogador_1['nome'] == nome:
            return True
    return False
    for jogador in jogadores['jogadores']:
        if jogador_2['nome'] == nome:
            return True
    return False

def remover_jogadores(jogadores, nome):
    for jogador in jogadores['jogadores']:
        if jogador_1['nome'] == nome:
            jogadores['jogadores'].remove(jogador1)
    for jogador in jogadores['jogadores']:
        if jogador_2['nome'] == nome:
            jogadores['jogadores'].remove(jogador2)

def listar_jogador(jogadores, nome):
    jogadores['jogadores'].sort()
    print (jogadores['jogadores'])
    