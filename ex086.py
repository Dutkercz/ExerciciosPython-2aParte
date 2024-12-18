list = [[0,0,0],[0,0,0],[0,0,0]]
for l in range (0,3):
    for c in range (0,3):
        list[l][c]=int(input(f'Digite um numero para a posição {l}x{c}: '))
for p in range (0,len(list)):
    for q in range (0, len(list)):
        print(f'[{list[p][q]:^5}]',end=' ')
print()
