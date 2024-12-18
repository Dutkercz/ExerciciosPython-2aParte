soma = n = contador = 0
while True:
    n = int(input('Digite um numero: '))
    if n < 999:
        soma += n
        contador += 1
    else:
        break
print(f'A soma dos {contador} digitados foi {soma}')