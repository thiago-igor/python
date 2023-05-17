num = [2,9,5,1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2) #Na posição 2 inserir o valor '0'
num.pop(0) #eliminou o 9 na posição 0
if 2 in num:
    num.remove(2) # Remove o primeiro 2 que encontra na lista
else:
    print('Não achei o numero 2')

#print(num)
#print(f'Essa Lista tem {len(num)} elementos')


valores = []
valores.append(5)
valores.append(6)
valores.append(7)

for v in valores: # para cada 'v' em valores:
    print(f'{v} - ', end='')

print()#para polar a linha

for c, v in enumerate(valores): #Pega a posição 'c' e o valor 'v'
    print(f'Na posição {c} encontrei o valor {v}!') 

print('Cheguei ao final da lista')


print()

valores2 = list()

for cont in range(0,5):
    valores2.append(int(input('Digite um Numero: ')))

for c, v in enumerate(valores2): #Pega a posição 'c' e o valor 'v'
    print(f'Na posição {c} encontrei o valor {v}!') 

print('Cheguei ao final da lista')


print()

a = [2,3,5,7,9]
b = a[:] #[:] significa uma copia de 'a', se n tivesse [:] estariamos fazendo uma ligação entre eles