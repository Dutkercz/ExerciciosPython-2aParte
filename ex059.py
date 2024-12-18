from time import sleep

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))


escolha = ''
sair = False
while sair == False:
    print('O que deseja fazer com esses valores:')
    escolha = int(input('''    [1]SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4]NOVOS NUMEROS
    [5] SAIR DO PROGRAMA
    :> '''))
    if escolha == 1:
        soma = n1 + n2
        print('==-' * 20)
        print('O resultado da soma: {} + {} é {}'.format(n1, n2 , soma))
        print('==-'*20)
        sleep(2)
    if escolha == 2:
        multiplica = n1 * n2
        print('==-' * 20)
        print('O resultado da multiplicação: {} x {} é {}'.format(n1, n2, multiplica))
        print('==-'*20)
        sleep(2)
    if escolha == 3:
        if n1 == n2:
            print('Os 2 valores são IGUAIS!')
        else:
            print('==-' * 20)
            print('O maior valor entre {} e {} é \033[32m{}\033[m'.format(n1, n2, (max(n1,n2))))
            print('==-' * 20)
        sleep(2)
    if escolha == 4:
        print('==-' * 20)
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
        print('==-' * 20)
    if escolha == 5:
        sair = True
    if escolha > 5:
        print('==-'*19)
        print('                \033[31mOPÇÃO INVÁLIDA\033[m')
        print('==-'*19)
        sleep(2)
print('=='*20)
print('       \033[31mENCERRANDO O SISTEMA.\033[m')
sleep(1)
print('             \033[35mAGUARDE...\033[m')
sleep(2)
print('         \033[31mFIM DO PROGRAMA.\033[m')
print('=='*20)