'''''('Manipulando cadeia de textos')
print('(Curso em video python < cadeia de caracters') / string'''
frase=str('Curso em Video Python')
'''Fatiamento'''
print(frase[:5])
print(frase[1:15:2])
print(frase[15:])
print(frase[9::3])
'''analise len=lenght'''
print(len(frase))
print(frase.count('o',0,15))
print(frase.find('deo'))
print(frase.find('android'))
print('Curso'in frase)
'''Transformação'''
print(frase.replace('Python','Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
'''frase(variavel).strip = remove os espaços sobrando no inicio da frase
lstrip tira os espaços da esquerda
rtrip tira os espaços da direita'''
'''Divisão e Junção'''
print(frase.split())
print('-'.join(frase))

#O replace só muda a frase se isso for atribuido a variavel, caso o contrario
#a frase continuara igual, ex:
frase = frase.replace('Curso','Aula')
print(frase)

dividido = frase.split()
print(dividido[0][1])