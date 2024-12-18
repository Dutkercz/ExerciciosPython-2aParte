'''cont = 0
n = 0
soma = 0
while not n == 999:
    n = int(input('Digite quantos numeros quiser para saber sua soma OU [999] - PARAR: '))
    cont += 1
    soma += n
print('Foram somados {} números, e o total é {}'.format(cont-1,soma-999))'''





'''cont = n = soma = 0
n = int(input('numeros quiser para somar ou 999 para sair: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite quantos numeros quiser para somar ou 999 para sair: '))
print('Foram somados {} números, e o total é {}'.format(cont,soma))'''





soma = cont = n = 0
while True:
    n = int(input('Quais numeros deseja soma - 999 para sair: '))
    if n >= 999:
        break
    soma += n
    cont += 1
print('total da soma ',soma,' foram somados ',cont,' numeros')
print('fim')
