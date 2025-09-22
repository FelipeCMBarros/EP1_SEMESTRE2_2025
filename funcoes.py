import random

def cria_pecas(n):
    pecas = []

    for x in range(n):
        pecas.append([x + 1, 'amarelo'])
        pecas.append([x + 1, 'azul'])
        pecas.append([x + 1, 'ciano'])
        pecas.append([x + 1, 'rosa'])
        pecas.append([x + 1, 'verde'])
        pecas.append([x + 1, 'vermelho'])

    return pecas

def cria_tabuleiro(n):
    pecas = cria_pecas(n)
    
    random.shuffle(pecas)
    
    tabuleiro = []

    for x in range(n):
        linha = pecas[x*6:(x+1)*6]  
        tabuleiro.append(linha)
    
    return tabuleiro