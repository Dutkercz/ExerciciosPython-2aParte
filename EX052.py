print('Numeros PRIMOS')
cont = 0
num = int(input('Digite um número para saber se é PRIMO: '))
for c in range(1,num+1):
    if num % c == 0:
      print('\033[32m {}\033[m'.format(c), end='')
      cont += 1
    else:
        print('\033[31m {}\033[m'.format(c), end='')
if cont == 2:
    print('\nO número {} é Primo'.format(num))
else:
    print('\nO número {} NÃO é PRIMO'.format(num))