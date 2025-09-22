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