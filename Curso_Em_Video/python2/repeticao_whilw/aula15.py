# Utilizando o BREAK
n = s = 0
while n != 999:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s += n
print(f'A soma dos numeros é {s}')