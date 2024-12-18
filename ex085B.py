num = [[],[]]
for c in range (1,8):
    n = int(input(f'Digite o {c}° da lista: '))
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)
num[0].sort()
num[1].sort()
print(f'A lista dos PARES É {num[0]}')
print(f'A lista dos IMPARES É {num[1]}')