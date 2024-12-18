import unidecode
print('Escreva uma frase e veja quantas vezes a letra A aparece, e a sua primeira e ultima posição')
frase=str(input('Digite uma frase, por gentileza: ')).strip().lower()
frase=(unidecode.unidecode(frase))
print('A letra "A" aparece {} vezes. '.format(frase.count('a')))
print('A primeira letra A aparece na posição {}'.format(frase.find('a')+1))
print('E a ultima letra A aparece na posição {}'.format(frase.rfind('a')+1))