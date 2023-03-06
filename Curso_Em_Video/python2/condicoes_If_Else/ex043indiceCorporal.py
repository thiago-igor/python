peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura**2)

print(f'Seu IMC é de {imc :.1f}')

if(imc < 18.5):
    print('Você esta ABAIXO do peso normal!')

elif( 18.5 <=imc <25 ):
    print('PARABENS, você esta na faixa de peso ideal!')

else:
    print('Você está ACIMA do peso ideal!')
