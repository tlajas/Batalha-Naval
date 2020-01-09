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
        nomes = []
        for jogador in jogo['jogadores']:
            for chave in jogador.keys():
                nomes.append(chave) 
        nomes.sort()           
        print("\n".join(nomes))


def esta_na_lista(jogo, nome):
    for jogador in jogo['jogadores']:
        for chave in jogador:
            if chave == nome:
                return False
    return True
      
def iniciar_jogo(jogo, nome1, nome2):
    nomes = []
    for jogador in jogo['jogadores']:
        if nome1 in jogador:
            nomes.append(nome1)
        if nome2 in jogador:
            nomes.append(nome2)
    if len(nomes) == 2:
        nomes.sort()
        print(nomes)
    elif len(nomes) < 2:
        print('Não existem jogadores suficientes para iniciar o jogo.') 
    




    
    