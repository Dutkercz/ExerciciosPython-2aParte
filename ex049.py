print('Tabuada')
num = int(input('''Digite um numero para saber a sua tabuada!
:> '''))
for c in range (1,11):
    print('{} x {} = {}'.format(num, c, (num*c)))
