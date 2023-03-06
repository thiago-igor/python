print('========== Nova Alternativa Veiculos ==========')

preco = float(input('Preço das compras R$: '))

print('''FORMAS DE PAGAMENTOS:
[1] A VISTA DINHEIRO/ PIX
[2] A VISTA CARTÃO
[3] 2X NO CARTÃO
[4] 3X OU MAIS NO CARTÃO''')

opcao = int(input('Qual opçao? '))

if(opcao == 1):
    nvpreco = preco - 0.10*preco
    print(f'''Sua compra sera a vista e terá um desconto de R${0.10*preco :.2f} 
    Preço final de R$:{nvpreco :.2f}''')

elif(opcao ==2):
    nvpreco = preco + 0.02*preco
    print(f'''Sua compra sera a vista no cartao e terá um juros de R${0.02*preco :.2f} 
    Preço final de R$:{nvpreco :.2f}''')

elif(opcao == 3):
    nvpreco = preco + 0.02*preco
    print(f'''Sua compra sera a parcelada no cartao e terá um juros de R${0.04*preco :.2f} 
    Preço da parcela R$:{nvpreco/2 :.2f} / Preço final de R$:{nvpreco :.2f}''')

elif(opcao ==4):
    parcelas = int(input('Quantas parcelas deseja? '))
    nvpreco = preco + 0.015*parcelas*preco
    print(f'''Sua compra sera a parcelada no cartao em {parcelas} vezes e terá um juros de R${0.015*parcelas*preco :.2f} 
    Preço da parcela R$:{nvpreco/parcelas :.2f} / Preço final de R$:{nvpreco :.2f}''')

else:
    print('Opção INVALIDA!')

