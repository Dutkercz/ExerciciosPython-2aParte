from math import factorial

print('CALCULO DE FATORIAL')
n = int(input('Digite um número para saber seu resultado fatorial: '))
c = n
fatorial = 1
print('Calculando fatorial de {}!'.format(n), end='= ')
while c > 0:
    print('{}'.format(c), end=' ')
    print('X' if c>1 else ' = ', end=' ')
    fatorial *= c
    c -= 1
print('{}'.format(fatorial))

