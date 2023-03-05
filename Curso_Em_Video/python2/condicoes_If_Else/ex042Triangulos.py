print('----- Digite os 3 lados do triangulo: -----')
l1 = int(input('lado 1: '))
l2 = int(input('lado 2: '))
l3 = int(input('lado 3: '))

if(l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1+ l2):
    print('Os Segmentos a cima podem formar um triangulo ', end='') # end= '' isso significa que nao teremos um enter depois desse print
    if(l1 == l2 == l3):
        print(f'EQUILATERO de lados: [{l1}] [{l2}] [{l3}]')

    elif(l1 == l2 or l2== l3 or l1 == l3):
        print(f'ISÓSCELES de lados: [{l1}] [{l2}] [{l3}]')
    
    else:
        print(f'ESCALENO de lados: [{l1}] [{l2}] [{l3}]')
    
else:
    print(f'Nao podemos formar um triangulo com os lados: [{l1}] [{l2}] [{l3}] ')
