listaT = []
listaP = []
listaI = []
conti = ''
while True:
    n = int(input('Digite o valor: '))
    print(f'Numero {n} Adicionado.')
    print('==='*18)
    conti = str(input('''Deseja continuar
[S] - SIM
[N] - NÃO
>>''')).strip().upper()[0]
    print('===' * 18)
    listaT.append(n)
    if n % 2 == 0 and n != 0:
        listaP.append(n)
    elif n % 2 == 1:
        listaI.append(n)
    if conti == 'N':
        break
listaT.sort()
print(f'Os valores da lista são {listaT}')
print(f'Os valores pares digitados são {listaP}')
print(f'Os valores IMPARES digitados são {listaI}')
