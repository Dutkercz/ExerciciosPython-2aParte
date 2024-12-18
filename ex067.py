from time import sleep

resultado : 0
while True:
    n = int(input('Quer ver a tabuada de qual valor: '))
    if n > 0:
        for c in range (1, 11):
            resultado = n * c
            print(f'{n} x {c} = {resultado}')
        print('\033[32m===\033[m' * 18)
    elif n < 0 :
        print('Numero INVÁLIDO!')
        sleep(2)
        print('\033[31mPROGRAMA FINALIZADO!\033[m')
        break

