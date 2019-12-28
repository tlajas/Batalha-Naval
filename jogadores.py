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
        if jogador['nome'] == nome:
            jogador['jogadores'].remove(nome)
            
def listar_jogador(jogo, nome):
    jogadores['jogadores'].sort()
    print (jogadores['jogadores'])
    