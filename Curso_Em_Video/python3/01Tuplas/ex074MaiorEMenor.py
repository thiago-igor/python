from random import randint

numeros = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))

print(f'Os valores sorteados foram: {numeros}')

print(f'O Maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')