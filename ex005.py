n1=int(input('Digite um valor:'))
n2=int(input('Agora diga outro valor:'))
s=n1+n2
d=n1/n2
m=n1*n2
di=n1//n2
p=n1**n2
print('A soma vale {} \n o produto {:.3f} e a multiplicação vale{}'.format(s, d, m), end=' ')
print('a divisão inteira é{} e a potencia é'.format(di, p))
