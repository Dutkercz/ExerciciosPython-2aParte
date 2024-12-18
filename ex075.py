contPAR = 0
n1 = (int(input('Digite o 1° numero :')),
     int(input('Digite o 2° numero :')),
     int(input('Digite o 3° numero :')),
     int(input('Digite o 4° numero :')))
tuplaN = (n1)
print()
print(f'Os valores digitados foram {tuplaN}')
print('Os numeros PARES SÃO: ',end='')
for numero in tuplaN:
    if numero % 2 == 0:
        contPAR += 1
        print(f' {numero} ', end=' > ')
if contPAR > 0:
    print(f'Temos {contPAR} numero(s) PAR(ES)')
else:
    print('Não temos nenhum numero PAR')
print()
if 9 in n1:
    print(f'Você digitou o valor 9, {n1.count(9)} vez(es)')
else:
    print('Não foi digitado o valor 9')
print()
if 3 in n1:
    print(f'O valor 3 aparece pela primeira vez na posição {tuplaN.index(3)+1}')
else:
    print('O valor 3 não aparece nenhuma vez!')

