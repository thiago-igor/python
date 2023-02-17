#Listas:
#           0         1        2
nomes = ['fabio', 'Andre', 'Thiago']
print(nomes[1])
for nome in nomes:
    print(nome)


numeros = [0, 1, 2, 3, 4, 5]
numeros.append(6) # add na ultima posição da lista
numeros2 = numeros.copy() # copia da lista
print(numeros.index(4)) # numero na posição 5
numeros.insert(0, -1) # add -1 na posição 0
print(numeros.index(0)) 
numeros.pop(0) #remove o elemento no indice 0
numeros.reverse() # inverte a lista 
numeros.sort() # deixa a lista em ordem crescente 


for numero in numeros:
    print(numero)

