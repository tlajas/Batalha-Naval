def jogadores():
    return {
        'jogadores': []
    } 


def adicionar_jogadores(jogo, nome):
    jogador = {
        nome : {
                'jogos': 0,
                'vitorias': 0
        }
    }
    jogo['jogadores'].append(jogador)


def tem_jogador(jogo, nome):
    for jogador in jogo['jogadores']:
        if nome in jogador:
            return True
    return False
   

def remover_jogadores(jogo, nome):
    for jogador in jogo['jogadores']:
        for chave in jogador:
            if chave == nome:
                jogador.clear()
                break


def listar_jogadores(jogo):
    if jogo['jogadores'] == []:
        print('Não existem jogadores registados.')
    else:
        for jogador in jogo['jogadores']:
            for chave in sorted(jogador.keys()):
                nomes = []
                nomes.append(chave)            
            print(nomes)


def esta_na_lista(jogo, nome):
    for jogador in jogo['jogadores']:
        for chave in jogador:
            if chave == nome:
                return False
    return True
      


    
    