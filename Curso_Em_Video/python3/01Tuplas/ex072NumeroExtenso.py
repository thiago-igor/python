cont = ('zero','um','dois','tres','quatro',
        'cinco','seis','sete','oito','nove','dez')

while True:
    num = int(input('Digite um numero entre 0-10:'))
    if 0 <= num <=20:
        break
    
    print('Tente novamente, ', end='')

print(f'O numero digitado foi {cont[num]}')