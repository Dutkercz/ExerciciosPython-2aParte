print('GERADOR DE PA')

num = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
cont = 0
mais_termos = 10
termos = 0
while not mais_termos == 0:
    termos+= mais_termos #variavel atualiza com a a entrada de novos termos, mas ja sai mostrando os 1°s 10
    while not cont == termos: #variavel atualizada, na primeira mostra os 10 primeiros, nas outras se atualiza
        print('{} '.format(num), end='')
        num += razao
        cont+=1
    print('PAUSA')
    mais_termos = int(input('\nGostaria de ver mais termos? Quantos? : '))#ira atualizar o valor da variavel.
print('ACABOU')
print('O total de termos apresentados foi {}'.format(cont))
