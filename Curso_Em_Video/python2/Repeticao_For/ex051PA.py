print('-='*12)
print('10 Primeiros termos de uma P.A')
print('-='*12)

p1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))

for p1 in range(p1,11, r):
    print(f'{p1}-> ', end='')
print('Acabou!')

