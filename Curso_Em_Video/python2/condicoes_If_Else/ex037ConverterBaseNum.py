print('------CONVERSOR DE BASE------')
num = int(input('DIGITE UM NUMERO: '))

opcao = int(input('''Escolha uma das bases para converter:
[1] Converter BINARIO 
[2] Converter OCTAL
[3] Converter HEXADECIMAL
Opção: '''))

if(opcao == 1):
    print(f'{num} convertido para BINARIO é igual a {bin(num)[2:]}') # [2:] estamos fatiando as 2 primeiras posiçoes da string posição 0 e 1, pois seria so para identificar que é binario. Do mesmo modo nos demais

elif(opcao == 2):
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')

elif(opcao == 3):
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')

else:
    print('Opção Invalida!')