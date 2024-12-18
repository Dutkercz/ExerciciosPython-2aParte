print('-=-'*20)
print('           Aumento anual de Salarios.')
print('-=-'*20)
print('10% para salários maiores que 1250.00')
print('15% para salários inferiores ou iguais a 1250.00')
sala=float(input('Digite o seu salário atual R$: '))

if sala<=1250:
    aumento=(sala*1.15)
else:
    aumento=(sala*1.10)
print('O seu salário passou de R$ {} para R$ {:.2f}'.format(sala,aumento))