palavras = ('Aprender', 'programar', 'python', 'estudar')

print('-'*30)
print(f'{"Analizando vogais":^30}')
print('-'*30)

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ',end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end='')