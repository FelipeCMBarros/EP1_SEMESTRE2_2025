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

def get_coordenadas(tabuleiro, valor, cor):
    for i, linha in enumerate(tabuleiro):
        for j, peca in enumerate(linha):
            if peca[0] == valor and peca[1] == cor:
                return [i, j]
    return [-1, -1]

def movimento_valido(tabuleiro, origem, destino):
    linha_o, col_o = origem
    linha_d, col_d = destino
    
    peca_origem = tabuleiro[linha_o][col_o]
    peca_destino = tabuleiro[linha_d][col_d]
    
    mesma_linha_ou_coluna = (linha_o == linha_d) or (col_o == col_d)
    
    mesmo_valor_ou_cor = (peca_origem[0] == peca_destino[0]) or (peca_origem[1] == peca_destino[1])
    
    return mesma_linha_ou_coluna and mesmo_valor_ou_cor

def movimento_valido(tabuleiro, origem, destino):
    linha_o, col_o = origem
    linha_d, col_d = destino
    
    peca_origem = tabuleiro[linha_o][col_o]
    peca_destino = tabuleiro[linha_d][col_d]
    
    mesma_linha_ou_coluna = (linha_o == linha_d) or (col_o == col_d)
    
    mesmo_valor_ou_cor = (peca_origem[0] == peca_destino[0]) or (peca_origem[1] == peca_destino[1])
    
    return mesma_linha_ou_coluna and mesmo_valor_ou_cor

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

def get_coordenadas(tabuleiro, valor, cor):
    for i, linha in enumerate(tabuleiro):
        for j, peca in enumerate(linha):
            if peca[0] == valor and peca[1] == cor:
                return [i, j]
    return [-1, -1]

def movimento_valido(tabuleiro, origem, destino):
    linha_o, col_o = origem
    linha_d, col_d = destino
    
    peca_origem = tabuleiro[linha_o][col_o]
    peca_destino = tabuleiro[linha_d][col_d]
    
    mesma_linha_ou_coluna = (linha_o == linha_d) or (col_o == col_d)
    
    mesmo_valor_ou_cor = (peca_origem[0] == peca_destino[0]) or (peca_origem[1] == peca_destino[1])
    
    return mesma_linha_ou_coluna and mesmo_valor_ou_cor

def movimentos_possiveis(tabuleiro, peca):
    origem = get_coordenadas(tabuleiro, peca[0], peca[1])
    
    if origem == [-1, -1]: 
        return []
    
    linha_o, col_o = origem
    movimentos = []
    
    for j in range(len(tabuleiro[0])):
        destino = [linha_o, j]
        if destino != origem and movimento_valido(tabuleiro, origem, destino):
            movimentos.append(destino)
    
    for i in range(len(tabuleiro)):
        destino = [i, col_o]
        if destino != origem and movimento_valido(tabuleiro, origem, destino):
            movimentos.append(destino)
    
    return movimentos