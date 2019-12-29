def jogadores():
    return {
        'jogadores': []
    } 


def adicionar_jogadores(jogo, nome):
    jogadores = {
        'nome' : nome
    }
    jogo['jogadores'].append(jogadores)


def tem_jogador(jogo, nome):
    for jogador in jogo['jogadores']:
        if jogador['nome'] == nome:
            return True
    return False
   

def remover_jogadores(jogo, nome):
    pass


def listar_jogadores(jogo):
    nomes = []
    for jogador in jogo['jogadores']:
        nomes.append(jogador['nome'])
        nomes.sort()
    if nomes == []:
        print('Jogador Inexistente')
    else:
        print(', '.join(nomes))


def esta_na_lista(jogo, nome):
    for jogador in jogo['jogadores']:
        if nome not in jogador['nome']:
            return True
    return False
      


    
    