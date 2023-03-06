frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split() # Separando frase em string separadas
junto = ''.join(palavra) # Substitui o espaço por nenhum espaço 
print(f'Você digitou a frase {frase}')

inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)

if(junto == inverso):
        print('Temos Um Palíndromo')


else:
    print('Nao temos um Palíndromo')

