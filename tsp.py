from scipy.spatial.distance import euclidean
import matplotlib.pyplot as plt
import numpy as np
import random

def main(tamanho_populacao, geracao, tamanho_torneio, probabilidade_cruzamento, probabilidade_mutacao):

    def gerando_populacao(tamanho_populacao):
        '''
        :parameter tamanho_populacao
        :return população gerada a partir da entrada do tamanho da população
        é criada uma população contendo dois arrays onde, x representa latitude e y representa longitude
        '''
        populacao = []
        for i in range(tamanho_populacao):
            x = np.arange(1, tamanho_populacao)
            np.random.shuffle(x)
            x = np.insert(x, 0, 0)
            x = np.insert(x, tamanho_populacao, 0)
            y = np.arange(1, tamanho_populacao)
            np.random.shuffle(y)
            y = np.insert(y, 0, 0)
            y = np.insert(y, tamanho_populacao, 0)
            populacao.append([x,y])

        return populacao

    def distancia(verticeX, verticeY):
        '''
        :parameter verticeX irá pegar os valores da longitude, que foi gerada na criação da população
        :parameter verticeY irá pegar os valores da longitude, que foi gerada na criação da população
        :return o cálculo da distância euclidiana
        '''
        dist = euclidean(verticeX, verticeY)
        return round(dist, 1)

    def funcao_fitness(tamanho_populacao, verticeX, verticeY):
        '''
        :parameter tamanho_populacao, irá definir o valor da variavel idx onde se inicia de 0 até o tamanho da populcao
        :parameter verticeX irá pegar os valores da latitude de acordo com o idx passado
        :parameter verticeY irá pegar os valores da longitude de acordo com o idx passado
        :return o custo total pecorrido durante o circuito pelas cidades, onde tem o inicio em 0 e o final em 0
        '''
        custo = 0
        for idx in range(tamanho_populacao):
            custo += distancia([verticeX[idx], verticeY[idx]], [verticeX[idx + 1], verticeY[idx + 1]])
        return custo

    pop = gerando_populacao(tamanho_populacao)
    custos= []
    '''
    :parameter geracao, é a variavel que ira definir a quantidade de gerações
    '''
    for i in range(geracao):
        '''
        :parameter tamanho_troneio, irá promover um torneio entre um grupo de individuos aleatoriamente tomanados na população
        dessa forma, o individuo que tiver melhor aptidao entre o grupo, é selecionado para a proxima geração da nova população
        '''
        for j in range(tamanho_torneio):
            if random.random() <= probabilidade_cruzamento:
                pai1, pai2 = None, None
                '''
                seleção dos individuos aleatoriamente pai1 e pai2
                '''
                while True:
                    pai1 = random.randint(0, tamanho_populacao - 1)
                    pai2 = random.randint(0, tamanho_populacao - 1)
                    if pai1 != pai2:
                        break

                filho1_x_validos = [gene for gene in range(tamanho_populacao)]
                filho1_y_validos = [gene for gene in range(tamanho_populacao)]
                filho2_x_validos = filho1_x_validos[:]
                filho2_y_validos = filho1_y_validos[:]
                filho1_x, filho1_y, filho2_x, filho2_y = [], [], [], []
                # cruzamento de um ponto
                while True:
                    # selecionando um ponto
                    ponto = random.randint(0, tamanho_populacao - 1)
                    #não seleciona as extremidades
                    if ponto != 0 and ponto != tamanho_populacao - 1:
                        for p in range(ponto):
                            if pop[pai1][0][p] not in filho1_x:
                                filho1_x.append(pop[pai1][0][p])
                                filho1_x_validos.remove(pop[pai1][0][p])

                            else:
                                elemento_x = random.choice(filho1_x_validos)
                                filho1_x.append(elemento_x)
                                filho1_x_validos.remove(pop[pai1][0][p])

                            if pop[pai1][1][p] not in filho1_y:
                                filho1_y.append(pop[pai1][1][p])
                                filho1_y_validos.remove(pop[pai1][1][p])
                            else:
                                elemento_y = random.choice(filho1_y_validos)
                                filho1_y.append(elemento_y)
                                filho1_y_validos.remove(elemento_y)

                            if pop[pai2][0][p] not in filho2_x:
                                filho2_x.append(pop[pai2][0][p])
                                filho2_x_validos.remove(pop[pai2][0][p])
                            else:
                                elemento_x = random.choice(filho1_x_validos)
                                filho2_x.append(elemento_x)
                                filho2_x_validos.remove(elemento_x)

                            if pop[pai2][1][p] not in filho2_y:
                                filho2_y.append(pop[pai2][1][p])
                                filho2_y_validos.remove(pop[pai2][1][p])
                            else:
                                elemento_y = random.choice(filho1_y_validos)
                                filho2_y.append(elemento_y)
                                filho2_y_validos.remove(elemento_y)

                        for p in range(ponto, tamanho_populacao):
                            if pop[pai2][0][p] not in filho1_x:
                                filho1_x.append(pop[pai2][0][p])
                                filho1_x_validos.remove(pop[pai2][0][p])
                            else:
                                elemento_x = random.choice(filho1_x_validos)
                                filho1_x.append(elemento_x)
                                filho1_x_validos.remove(elemento_x)

                            if pop[pai2][1][p] not in filho1_y:
                                filho1_y.append(pop[pai2][1][p])
                                filho1_y_validos.remove(pop[pai2][1][p])

                            else:
                                elemento_y = random.choice(filho1_y_validos)
                                filho1_y.append(elemento_y)
                                filho1_y_validos.remove(elemento_y)

                            if pop[pai1][0][p] not in filho2_x:
                                filho2_x.append(pop[pai1][0][p])
                                filho2_x_validos.remove(pop[pai1][0][p])
                            else:
                                elemento_x = random.choice(filho2_x_validos)
                                filho2_x.append(elemento_x)
                                filho2_x_validos.remove(elemento_x)

                            if pop[pai1][1][p] not in filho2_y:
                                filho2_y.append(pop[pai1][1][p])
                                filho2_y_validos.remove(pop[pai1][1][p])
                            else:
                                elemento_y = random.choice(filho2_y_validos)
                                filho2_y.append(elemento_y)
                                filho2_y_validos.remove(elemento_y)
                        filho1_x.insert(len(pop), 0)
                        filho1_y.insert(len(pop), 0)
                        filho2_x.insert(len(pop), 0)
                        filho2_y.insert(len(pop), 0)
                        break
                # aplica o operador de mutação
                if random.random() <= probabilidade_mutacao:
                    gene1, gene2 = None, None

                    while True:
                        gene1 = random.randint(1, tamanho_populacao - 1)
                        gene2 = random.randint(1, tamanho_populacao - 1)
                        gene3 = random.randint(1, tamanho_populacao - 1)
                        gene4 = random.randint(1, tamanho_populacao - 1)
                        if gene1 != gene2 and gene3 != gene4:
                            filho1_x[gene1], filho1_x[gene2] = filho1_x[gene2], filho1_x[gene1]
                            filho1_y[gene1], filho1_y[gene2] = filho1_y[gene2], filho1_y[gene1]

                            filho2_x[gene3], filho2_x[gene4] = filho2_x[gene4], filho2_x[gene3]
                            filho2_y[gene3], filho2_y[gene4] = filho2_y[gene4], filho2_y[gene3]
                            break

                #obtém fitness de todo mundo
                fitness_pai1 = funcao_fitness(tamanho_populacao, pop[pai1][0], pop[pai1][1])
                fitness_pai2 = funcao_fitness(tamanho_populacao, pop[pai2][0], pop[pai2][1])
                fitness_filho1 = funcao_fitness(tamanho_populacao, filho1_x, filho1_y)
                fitness_filho2 = funcao_fitness(tamanho_populacao, filho2_x, filho2_y)

                if fitness_filho1 < fitness_pai1 or fitness_filho1 < fitness_pai2:
                    if fitness_filho1 < fitness_pai1:
                        pop.pop(pai1)
                    else:
                        pop.pop(pai2)
                    pop.append([filho1_x, filho1_y])
                elif fitness_filho2 < fitness_pai1 or fitness_filho2 < fitness_pai2:
                    if fitness_filho2 < fitness_pai1:
                        pop.pop(pai1)
                    else:
                        pop.pop(pai2)
                    pop.append([filho2_x, filho2_y])

        # obtém o melhor
        melhor_individuo = pop[0][:]
        for individuo in range(1, tamanho_populacao):
            if funcao_fitness(tamanho_populacao, pop[individuo][0], pop[individuo][1]) < funcao_fitness(tamanho_populacao, melhor_individuo[0], melhor_individuo[1]):
                melhor_individuo = pop[individuo]
        print(f"Iteração: {i + 1} Melhor caminho {melhor_individuo} Custo: {funcao_fitness(tamanho_populacao, melhor_individuo[0], melhor_individuo[1])}")
        custos.append(funcao_fitness(tamanho_populacao, melhor_individuo[0], melhor_individuo[1]))

    plt.figure(figsize=(100, 50))
    plt.subplot(221),  plt.plot(custos, 'r-o')
    plt.title("Custos")
    plt.subplot(222), plt.plot(melhor_individuo[0], melhor_individuo[1], 'r-o')
    plt.title("Melhor Caminho" + " Custo Final " + str(custos[-1]))
    plt.show()

if __name__ == "__main__":
    main(tamanho_populacao=10, geracao=1000, tamanho_torneio=3, probabilidade_cruzamento=0.7, probabilidade_mutacao=0.6)