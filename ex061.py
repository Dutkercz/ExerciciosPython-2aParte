num = int(input('Digite o 1° termo da PA: '))
razao = int(input('Digite a razão da PA: '))
numI = num
cont = 0
while not cont == 10:
    print('{}'.format(numI), end=' ')
    numI += razao
    cont += 1
print('FIM')
