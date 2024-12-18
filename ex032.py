from datetime import date
print('-=-'*20)
print('      Vamos descobrir se o ano digitado é Bissexto?')
print('-=-' *20)
ano=int(input('Digite um ano qualquer ou 0 para saber sobre ano atual: '))
if ano==0:
    ano=date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('o ano {} é BISSEXTO'.format(ano))
else:
    \033[0;33;44mprint('o ano {} não é BISSEXTO'.format(ano))