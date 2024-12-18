def fatorial (num, show = False):
    '''
    calcúla o fatorial de um número
    :param num: número que deseja saber o fatorial
    :param show: mostra  o cálculo se show = True, mostra apenas o resultado se show = False ou em branco.
    :return: retorna o print com o resultado, acompanhado ou não do cálculo.
    '''
    f = 1
    for c in range (num, 0, -1):
        f*=c
    if not show:
        print('-=-'*20)
        return print(f'O Fatorial de {num} é {f}')
    elif show:
        print('-=-'*20)
        print(f'{num} ', end='')
        for d in range (num, 1, -1):
            print(f'x {d-1}', end=' ')
        print(f' = {f}')

num_fat = int(input('Digite o numero para saber seu fatorial: '))
fatorial(num_fat, True)
help(fatorial)