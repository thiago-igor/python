#print -> saida de dados
#input -> entrada de dados 
#conseito fprint
var = input('Ola, Qual o seu nome?: ')
print(f'Que legal, prazer em lhe conhecer {var}.')


#cast -> converter um tipo de dado:
num1 = int(input('Me informe um numero inteiro: '))
num2 = int(input('Me informe outro numero inteiro: '))
soma = num1+num2
print(f'{num1} + {num2} = {soma}')


# if else

escolha = "banana"
if(escolha == "banana"):
    print('voce comprou bananas!')

elif(escolha == "abacate"):
    print('Voce comprou abacates!')
else:
    print('Voce Não comprou nada')
