from time import sleep


def lin ():
    print('=='*20)


def manual(msg):
    while True:
        ajuda = input(f'{msg}').strip().lower()
        if ajuda != 'fim':
            sleep(1)
            lin()
            print(f'\033[46mAcessando o manual de {ajuda}\033[m')
            lin()
            sleep(1)
            print(f'\033[42m{help(ajuda)}\033[m')
        elif ajuda == 'fim':
            print('\033[31mENCERRANDO O PROGRAMA\033[m')
            sleep(1)
            print('\033[41mFIM\033[m')
            break

manual('Digite a função ou Biblioteca >> ')