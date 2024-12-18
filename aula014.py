'''Estrutura de laços
estrutura de repetição  WHILE = enquanto
estrutura de repetição com teste logico'''

#enquanto não maçã
    #passo
#pago

'''while not maçã:
    passo
pega'''

'''while not maça:
    if chão:
        passo   
    if buraco:
        pule
    if moeda:
        pegue
pegue'''
'''for c in range (1,10):
    print(c)
print('ACABOU!')'''
'''c=1
while c < 10:
    print(c)
    c = c + 1
print('fim')'''
'''n = 1
while n !=0:
    n = int(input('Digite um valor:'))
print(n)'''
'''n = 1
r = 'S'
while r == 'S':
    n = int(input('Digite um valor:'))
    r = str(input('Deseja continuar? [S] [N]')).upper().strip()
print('FIM')'''
n = 1
contI = 0
contP = 0
while n != 0 :
    n = int(input('Digite um numero: '))
    if n % 2 == 0 and not n == 0:
        contP += 1
    elif n % 2 == 1:
        contI += 1
print('São {} ímpares e {} pares'.format(contI, contP))