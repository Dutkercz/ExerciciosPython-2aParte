lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    conti = str=input('''Deseja continuar? 
[S] - sim
[N] - não
>> ''').strip().lower()[0]
    if conti == 'n':
        break
print(f'Você digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f' A lista em valores descrescentes é {lista}')
if 5 in lista:
    print('O numero 5 faz parte da lista')
else:
    print('O numero 5 NÃO faz parte da lista!')
