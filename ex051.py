
cont = 0
termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
decimo = termo + 10 * razao
for c in range(termo, decimo, razao):
    #termo = termo + razao
    print('{}'.format(c), end=' -> ')
print('ACABOU!')