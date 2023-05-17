valores = list()
mai = 0
men = 0

for pos in range(0,5):
    valores.append(int(input(f'Digite um valor para posição {pos}: '))) # preenchendo a lista
    
    if pos == 0: # analisando o maiore menor
        mai = men = valores[pos]
    else:
        if valores[pos] > mai:
            mai = valores[pos]
        if valores[pos] < men:
            men = valores[pos]

print('=-'*30)

print(f'Voce digitou os valores {valores}')

print(f'O maior valor digitado foi {mai} na posição ', end='') 
for i,v in enumerate(valores): # Pegando a posição do maior 
    if v == mai:
        print(f'{i}...')
print(f'O menor valor digitado foi {men} na posição ', end='')
for i, v in enumerate(valores): # Pegando a posição do menor
    if v == men:
        print(f'{i}...')