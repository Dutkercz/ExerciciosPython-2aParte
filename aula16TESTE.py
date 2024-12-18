valor = list(range(0,11))
print(valor)
print()
numeros = []
numeros.append(5)
numeros.append(3)
numeros.append(7)
print(numeros)
for con in range(0,5):
    numeros.append(int(input('Digite um valor: ')))
for indice, elemento in enumerate(numeros):
    print(f'Na posição {indice} encontrei o valor {elemento}...')
print('CHEGUEI AO FIM DA LISTA')

a = [3,5,7]
b = a # cria uma ligação entre a lista A e B
#se eu alterar o valor em uma, vai alterar o da outra tambem
print(f'a lita a é {a} e a lista b é {b}')
b[1] = 9 #mesmo que o comando seja para a lista B, vai alterar nas duas.
print(f'lista {a} e lista {b}')
'''a não ser que faça uma cópia 
exemplo'''
b = a[:]
b[1] = 11 #ira trocar o item na posição 1 pelo valor 5
print(f'LISTA {a} e LISTA {b}')#TROCOU APENAS NA LISTA B