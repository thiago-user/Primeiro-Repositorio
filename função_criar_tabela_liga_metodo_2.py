# Essa função não foi testada com um número ímpar de equipes!


from random import shuffle


#equipes = ["Athletic Bilbao", "Dep Alaves", "Atletico Madrid", "Barcelona FC", "Real Betis", "Celta de Vigo", "Eibar", "Espanyol", "Getafe", "Granada", "Leganes", "Levante", "Mallorca", "Osasuna", "Real Madrid", "Real Sociedad", "Sevilla", "Valencia", "Valladolid", "Villarreal"]
equipes = ['Alpha', 'Beta', 'Gamma', 'Delta']

# A função de receber uma lista com strings representando as equipes do campeonato
def gerar_tabela(equipes):
    """ Recebe uma lista com equipes e retorna uma (lista com sublistas e strings) "tabela" semelhante a uma tabela de uma liga de pontos corridos com jogos de idade e volta"""
    # Calcula o número total de rodadas
    num_rdds = len(equipes) * (len(equipes) - 1) // (len(equipes) // 2)
    # Calcula o número de jogos por rodada
    jpr = len(equipes) // 2
    
    # usando list comprehensions para criar uma lista de rodadas vazias (sem jogos)
    tabela = [[] for rdd in range(num_rdds // 2)]
    
    # Criamos uma lista com todos os confrontos de ida
    confrontos = [[equipes[home], equipes[away]] for home in range(0, num_rdds // 2) for away in range(home+1, len(equipes))]
    
    # Seleciona alguns jogos da lista 'confrontos' e inverte mandante e visitante... assim, todas as equipes terão jogos em casa e fora
    confrontos += [[confrontos[x][0], confrontos[x][1]] if x % 2 == 0 else [confrontos[x][1], confrontos[x][0]] for x in range(0, num_rdds // 2 * jpr)]
    del confrontos[:num_rdds // 2 * jpr]

    rdd = 0
    # Pegamos um confronto da lista de confrontos
    for confronto in confrontos:
        while True:
            # Verificamos em cada jogo de uma rodada ('tabela[rdd]') especifica se uma das duas equipes do confronto escolhido ('confronto') já está jogando nessa rodada
            for jogo in tabela[rdd]:
                # Se verdadeiro, significa que uma das equipes do confronto selecionado já está jogando nessa rodada, então, fazemos um 'break' e verificamos a próxima rodada
                if confronto[0] in jogo or confronto[1] in jogo:
                    rdd += 1
                    if not rdd < num_rdds//2:
                        rdd = 0
                    break
            # Se nenhuma das equipes for encontrada na rodada, vamos adicionar esse confronto à essa rodada
            else:
                tabela[rdd].append(confronto)
                rdd += 1
                if not rdd < num_rdds//2:
                    rdd = 0
                break

    # Até aqui, apenas as rodadas de "ida" foram criadas, agora criaremos as rodadas de "volta"
    for r in range(0, num_rdds // 2):
        # O 'shuffle' serve para que as mesmas equipes não fiquem sempre abrindo/fechando as rodadas
        shuffle(tabela[r])
        # Criamos uma nova rodada "vazia"
        tabela.append([])
        for jogo in range(0, jpr):
            # Adicionamos os jogos de uma rodada especificada por 'r',  à rodada vazia, invertendo mandante e visitante e invertendo a ordem dos jogos, de forma que o primeiro jogo da rodada de "ida", seja o último da rodada de "volta".
            tabela[-1].insert(0, [tabela[r][jogo][1], tabela[r][jogo][0]])

    return tabela

print(gerar_tabela(equipes))
