def fatorial (n = 0): #n é o inicio da fatorial, e ira multiplacando pelo seu num, antecessor
    f = 1 #var pra receber o valor da fatorial
    for c in range (n, 0, -1):
        f*=c # se n = 5, o 'c' começa no 5, mult. o 'f' que vale 1... então seria tipo... 1*5 * 1*4 * 1*3 * 1*2 * 1*1
    return f

fat1 = fatorial(5)
fat2 = fatorial(7)
fat3 = fatorial()
print()
print(f'Os valores de cada fatorial apresentada é {fat1}, {fat2} e {fat3}')

def par (n=0):
    if n % 2 == 0:
        return True
    else:
        return False
    return n

print(par(4))
print(par(3))
print('ou')
if par == True:
    print('É PAR')
else:
    print('É impar')