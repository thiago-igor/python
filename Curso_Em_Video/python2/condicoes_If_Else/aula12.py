nome = str(input('Qual é seu nome?'))

if nome == 'Gustavo':
    print('Que nome feio')
elif nome == 'pedro' or nome == 'maria' or nome == 'lucas':
    print('Seu nome é bem comum no brasil')

elif nome in 'Ana Claudia Jessica Julia': #se nome estiver em alguma dessas palavras
    print('Belo nome feminino')
else:
    print('Que nome bonito!')

print(f'Tenha um bom dia {nome}')