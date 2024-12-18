print('Crie um algoritimo que leia um numero e mostre seu dobro, triplo e raiz quandrada')
n1=int(input('Digite um numero:'))
dobro=n1*2
triplo=n1*3
raiz=pow(n1,(1/2))
print('O dobro de {} é {}, seu triplo é {} \n E a sua raiz quadrada é {:.4f}'.format(n1, dobro, triplo, raiz))
