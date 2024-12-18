from itertools import count

lanche = ('banana','cafe','feijao','tomate', 'batata frita') #4 espaços [0 1 2 3 4] = AS TULPAS SÃO IMUTAVEIS =
print(len(lanche),lanche[-2]) #TUPLAS NÃO PRECISAM DE PARENTESES
print(lanche[1:3]) #desconsidera o ultimo numero
print(lanche[-2:])#começa no penultimo e vai até o final
#lembrando que tuplas nao podem receber novos valores

print()
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print()


for comida in lanche:
    print(f'eu vou comer {comida}')
print()

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print(sorted(lanche)) #ordenado por alfabeto (tranformou em lista)
print(lanche) #a tupla continua imutavel

tuplaA = (2,5,4)
tuplaB = (3,5,7,1)
tuplaC = tuplaA+tuplaB
print(tuplaC)
print(len(tuplaC))
print(tuplaC.count(5))#conta a quantidade de Num. 5
print(tuplaC.index(7))#começando do 0, posição do numero

#tuplas aceitam dados de tipos diferentes
pessoa = ('Cristian', 32, 'M', 110.2)
print(pessoa)
del(pessoa) #deleta uma variavel
print(pessoa)