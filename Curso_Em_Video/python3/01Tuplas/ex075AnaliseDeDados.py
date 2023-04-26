num = (int(input('Digite um numero: ')), 
       int(input('Digite outro numero: ')),
       int(input('Digite outro numero: ')),
       int(input('Digite outro numero: ')),
       int(input('Digite outro numero: ')))
print('=-'*30)
print(num)

print('=-'*30)
print(f'O Valor 9 apareceu {num.count(9)} vezes') #FUnção para contar quantos '9' tem na tupula

print('=-'*30)
if 3 in num:
    print(f'O valor 3 apareceu primeiro na posição {num.index(3)+1}') 
else:
    print('O valor 3 nao foi digitado')

print('=-'*30)
for n in num:
    if n % 2 == 0:
        print(f'{n} é divisivel por 2')

print('=-'*30)