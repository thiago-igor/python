for i in range(0,4,1): #começa em 0, vai ate 4 e pula de 1 em 1
    print(i)

cont = 0
while(cont <4):
    print(cont)
    cont +=1

#boolean:

entrada = ""

while(not entrada == "uva"):
    print('Adivinhe a fruta para ganhar')
    entrada = input('--->   ')

    if (entrada == 'uva'):
        print('Parabens voce acertou!!!')