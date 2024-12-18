'''conti = ''
lisAux = list()
pessoa = list()
gorda = list()
magra = list()
while True:
    lisAux.append(str(input('Digite seu nome: ')))
    lisAux.append((int(input(('Digite seu peso: ')))))
    pessoa.append(lisAux[:])
    print(f'{lisAux[0]} com {lisAux[1]} KGs, cadastrado(a) com sucesso')
    print('---'*20)
    conti = str(input('Deseja continuar [S/N]')).strip().upper()[0]
    print('---'*20)
    for pess in lisAux:
        if lisAux[1] >= 100:
            gorda.append(pess)
            lisAux.clear()
        else:
            magra.append(pess)
            lisAux.clear()
    if conti == 'N':
        break
    elif conti!= 'N':
        print('Digite informações validas')
print(f'Foram cadastradas {len(pessoa)} pessoas')
print(f'As pessoas mais pesadas são {gorda}')
print(f'As pessaos mais leves são {magra}')'''

temp = []
princ = []
maior = menor = ''
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        elif temp [1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    c = str(input('Continuar: ')).strip().upper()[0]
    if c == 'N':
        break
print(f'O total de pessoas cadastradas foi {len(princ)}')


print(f'O maior peso foi {maior}, de ', end='')
for p in princ:
    if p[1] == maior:
        print(f'{p[0]}', end=' ')
print(f'\nO menor peso foi {menor}, de ', end=', ')
for p in princ:
    if p[1] == menor:
        print(f'{p[0]}', end=' ')
