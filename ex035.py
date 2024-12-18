print('Digite 3 valores para saber se eles podem formar um triangulo')
l1=float(input('Digite o primeiro valor: '))
l2=float(input('Digite o segundo valor: '))
l3=float(input('Digite o terceiro valor: '))
if l1<l2+l3 and l2<l1+l3 and l3<l1+l2:
    print('Como o valores de {}, {} e {} podemos formar um triangulo'.format(l1,l2,l3))
else:
    print('Com os valores de {}, {} e {} não é possivel formar um triangulo.'.format(l1,l2,l3))
