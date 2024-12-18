print('Mais pesado e o mais leve')
lista = []
for c in range (1, 6):
    peso = float(input('Digite o peso da {}° pessoa: Kg '.format(c)))
    lista += [peso]
print('A pessoa mais pesada tem {} Kg, e a mais leve tem {} Kg'.format(max(lista), min(lista)))