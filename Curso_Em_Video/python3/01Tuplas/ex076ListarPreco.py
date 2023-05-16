listagem = ('lapis', 1.75,
            'Borracha', 2,
            'caneta', 3.50,
            'caderno', 19.90)

print('-'*40)
print(f'{"LISTAGEM DE PRECOS":^40}') #centralizar com 40 espaços
print('-'*40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='') #alinhar com 30 espaços preenchidos por um '.'
    else:
        print(f'R$:{listagem[pos]:>7.2f}') # alinhar com 7 espaços e 2f = 2 casas decimais 

print('-'*40)