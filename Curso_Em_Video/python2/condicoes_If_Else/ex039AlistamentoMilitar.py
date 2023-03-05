from datetime import date
atual = date.today().year

nascimento = int(input('Em que ano você nasceu?'))

anos = atual - nascimento

if(anos >= 18):
    print(f'Parabens, voce tem {anos} anos, precisa se alistar!')

else:
    print(f'Voce tem a penas {anos} anos, ainda nao pode se alistar ')