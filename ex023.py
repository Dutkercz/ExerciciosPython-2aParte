
print('Digite um numero de 0 a 9999')
num=str(input('Digite seu numero escolhido: '))
print('Analisando seu numero...')
print('{} Unidade(s)'.format(num[3]))
print('{} Dezena(s)'.format(num[2]))
print('{} Centena(s)'.format(num[1]))
print('{} Milhar(es)'.format(num[0]))

n=int(input('Digite novamente o numero entre 0 e 9999 '))
u= n//1 % 10
d = n // 10 % 10
c = n //100 % 10
m = n // 1000 % 10
print('Unidade {}'.format(u))
print('Dezena {}'.format(d))
print('Centena {}'.format(c))
print('Milhar {}'.format(m))
