print('='*30)
print('Banco BB')
print('='*30)

valor = int(input('Qual valor deseja sacar? R$:'))
sedula50 = sedula20 = sedula1 = 0

while valor != 0:
    if valor >= 50:
        sedula50 += 1
        valor = valor - 50

    elif valor >= 20:
        sedula20 += 1
        valor = valor - 20

    else:
        sedula1 += 1
        valor = valor - 1

print(f'''Total de {sedula50} sedulas de R$:50,00
Total de {sedula20} sedulas de R$:20,00
Total de {sedula1} sedulas de R$:1,00''')