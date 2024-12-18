conti = True
numeros = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezeseis','dezessete','dezoito','dezenove','vinte')
while conti == True:
    escolha = int(input('Escolha um numero entre 0 e 20: '))
    if escolha >= 0 and escolha <= 20:
            print(f'Você digitou {numeros[escolha]}')
            conti = str(input('Deseja continuar S - N: ')).strip().upper()[0]
            if conti == 'S':
                conti = True
            else:
                print('\033[31mPROGRAMA FINALIZADO\033[m')
                break
    else:
        print('==='*16)
        print('\033[31mOpção inválida, Tente novamente!\033[m')
        print('===' * 16)



