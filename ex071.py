print('==='*16)
print(f'{'BANCO MADRUGA':=^48}')
print('==='*16)

saque = int(input('Quanto deseja sacar R$ : '))
total = saque
ced_atual = 50
cont_ced = 0
while True:
    if total >= ced_atual:
        total -= ced_atual
        cont_ced +=1
    else:
        if cont_ced>0:
            print(f'O total de cédulas de R$ {ced_atual} é de {cont_ced} cédulas')
        if ced_atual == 50:
            ced_atual = 20
        elif ced_atual == 20:
            ced_atual = 10
        elif ced_atual == 10:
            ced_atual = 1
        cont_ced = 0
        if total == 0:
            break

