import math
from pickletools import float8

print('Faça um prog. que leia o comprimento do cateto oposto e do cateto adjacente\nde um triangulo retangulo, calcule e mostre\no comprimento da hipotenusa')
oposto=float(input('Digite o valor do cateto oposto: '))
adjc=float(input('Digite o valor do cateto adjacente :'))
hipot= math.hypot(oposto,adjc)
print('O comprimento da hipotenusa desse triangulo retangulo é {:.2f}'.format(hipot))
