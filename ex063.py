print('Sequencia de Fibonacci')
total_seq = int(input('Digite o tamanho da sequencia: '))
primeir_t = 0
segundo_t = 1
soma = 0
cont = 2
print('~~'*20)
print('{} > {}'.format(primeir_t, segundo_t), end=' > ')
while not cont == total_seq:
    soma = primeir_t + segundo_t

    print('{}'.format(soma), end=' > ')
    primeir_t = segundo_t
    segundo_t = soma
    cont+=1
print('FIM')
print('~~'*20)
print(f'Foram mostrados {cont} termos')