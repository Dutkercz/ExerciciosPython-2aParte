print('\033[32m-==\033[m'*20)
print('\033[32m                     GERADOR DE PA\033[m')
print('\033[32m-==\033[m'*20)
num=int(input('Digite o primeiro termo da PA: '))
razao=int(input('Digite a razão da PA: '))
cont=0
mais=10
totalT=0
print('-=='*20)
while not mais == 0:
    totalT += mais
    while not cont == totalT :
        print('{}'.format(num), end=" ")
        num += razao
        cont+=1
    print('pausa')
    print('-=='*20)
    mais=int(input('Quantos termos mais deseja ver? '))
print('O total de termos apresentados foi {}'.format(cont))
print('FIM')