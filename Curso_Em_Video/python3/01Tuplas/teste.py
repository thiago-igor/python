lanche = ('hamburguer', 'suco', 'pudim')

#for cont in range(0, len(lanche)):
#   print(lanche[cont])

 #OU

for comida in lanche:
    print(f'Eu vou comer {comida}')

#Para enumerar:

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')