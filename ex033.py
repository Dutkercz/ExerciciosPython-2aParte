print('Ler 3 numeros e mostrar qual o MAIOR  e qual o MENOR entre eles')
print('=-='*20)
print('DIGITE 3 NUMEROS DIFERENTES')
print('--'*10)
n1=int(input('Diga o primeiro numero: '))
n2=int(input('Diga o segundo numero: '))
n3=int(input('Diga o terceiro numero: '))
lista=[n1,n2,n3]
maior=max(lista)
menor=min(lista)
print('O MAIOR número é {}\nO MENOR número é {}'.format(maior,menor))

