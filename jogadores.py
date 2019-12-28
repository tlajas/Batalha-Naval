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
    for jogador in jogo['jogadores']:
        jogador['nome'].remove(nome)
                

def esta_na_lista(jogo, nome):
    for jogador in jogo['jogadores']:
        if nome not in jogador['nome']:
            return True
    return False
      

def listar_jogador(jogo):
    jogo['jogadores'].sort()
    print (jogo['jogadores'])
    