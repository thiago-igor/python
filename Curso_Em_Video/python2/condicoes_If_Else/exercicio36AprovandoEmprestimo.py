print('Financiamento Imobiliario:')

valor= int(input('Valor Da Casa R$: '))
salario = int(input('Quanto você ganha por mes: '))
anos = int(input('Em Quantos anos deseja financiar? '))

parcela = valor / (anos*12)

if(parcela >0):
    print(f'Para pagar uma casa de R$:{valor:.2f} em {anos:.2f} anos, a prestação sera de R$:{parcela:.2f} ao mes')
if(parcela <= salario):
    print('Emprestimo concedido')
elif(parcela > salario):
    print('Salario imcompativel!')
else:
    print('[Erro!!] Tente novamente por favor!')
