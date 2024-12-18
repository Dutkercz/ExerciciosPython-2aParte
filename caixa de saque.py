saque = int(input('Digite o valor do saque: R$ '))
total = saque
cedula = 100
contador = 0
while True:
    if total >= cedula:
        total -= cedula
        contador += 1
    else:
        if contador > 0:
            print(f'{contador} cedulas de R$ {cedula} ')
        if cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        contador = 0
        if total == 0:
            break