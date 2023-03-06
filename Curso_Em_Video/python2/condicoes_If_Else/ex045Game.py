from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Sua Opção: '))

print('-='*11)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-='*11)

if(computador == 0 ):  #Computador == pedra
    if jogador == 0:
        print('EMPATE')
    elif (jogador ==1):
        print('Jogador GANHOU')
    elif(jogador == 2):
        print('Computador GANHOU')

elif(computador == 1): #Computador == papel
    if jogador == 0:
        print('Computador GANHOU')
    elif (jogador ==1):
        print('EMPATE')
    elif(jogador == 2):
        print('Jogador GANHOU')

elif(computador == 2): #Computador = tesoura
    if jogador == 0:
        print('Jogador GANHOU')
    elif (jogador ==1):
        print('Computador GANHOU')
    elif(jogador == 2):
        print('EMPATE')
