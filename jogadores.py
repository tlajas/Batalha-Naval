import main
em_jogo = main.emjogo

jogadores_em_jogo = []
jogadores_registados = []

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
    jogadores_registados.clear()
    jog_registados(jogo)    

def jog_registados(jogo):
    for j in jogo['jogadores']:
            for key in j:
                jogadores_registados.append(key)

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
      
def iniciar_jogo(nome1, nome2):
    jogadores_em_jogo.clear()
    global em_jogo
    if (nome1 not in jogadores_registados) or (nome2 not in jogadores_registados):
        print('Jogadores não registados.')
    else:
        jogadores_em_jogo.append(nome1)
        jogadores_em_jogo.append(nome2)
        jogadores_em_jogo.sort()
        print('Jogo iniciado entre', (' e ').join(jogadores_em_jogo))
        em_jogo = True
        return em_jogo
    




    
    