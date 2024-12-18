n1=float(input('\033[31m Escreva o primeiro número:\033[m '))
n2=float(input('\033[32m Escreva o segunda número:\033[m '))
n3=float(input('\033[33m Escreva a terceira nota:\033[m '))
n4=float(input('\033[34m Escreva a nota final:\033[m '))
m=(((n1+n2+n3)*2)+(n4*4))/10

if m>= 7:
    print('Parabens sua média é {}, você está \033[32mAPROVADO!\033[m'.format(m))
elif m>=5 and m<7:
    print('Você está em \033[33mRECUPERÇÃO\033[m, sua nota foi {}'.format(m))
else:
    print('Você está \033[31mREPROVADO\033[m. Sua média foi {}'.format(m))