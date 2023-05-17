valores = list()
while(True):
    v = (int(input('Digite um valor: ')))
    if v not in valores:
        valores.append(v)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado, não vou adicionar!')

    c = str(input('Quer continuar? [S/N]: '))
    if c in 'Nn':
        break

valores.sort()
print(valores)