maioridade = 0
nomevelho = ''
somaidade = 0

for c in range(1,5):
    print(f'----- {c} PESSOA ----- ')
    nome = str(input('Nome:')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade

    if c == 1:
        maioridade = idade
        nomevelho = nome

    if idade > maioridade:
        maioridade = idade
        nomevelho = nome
    
mediaidade = somaidade/4
print(f'A media das idades é de {mediaidade :.2f} anos')
print(f'{nomevelho} é mais velho(a) e possui {maioridade} anos')
