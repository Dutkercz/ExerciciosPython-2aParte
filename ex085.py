lista = []
lisP = []
lisI = []
for c in range (0,7):
    n = int(input(f'Digite o {c+1}° valor:'))
    if n % 2 == 0:
        lisP.append(n)
    elif n % 2 == 1:
        lisI.append(n)
lisI.sort()
lisP.sort()
lista.append(lisP)
lista.append(lisI)
print(lista)

