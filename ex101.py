from datetime import date

def voto(ano):
    print('-==-'*10)
    ano_atual = date.today().year
    idade = ano_atual - ano
    if idade >= 18 and idade < 65:
        return print(f'Com {idade} anos, o voto é obrigatório.')
    elif idade >= 16 or idade >= 65:
        return print(f'Com {idade} anos, o voto é opcional')
    else:
        return print(f'Com {idade} não é possivel votar')



nasc = int(input('Qual o seu ano de Nascimento: '))
voto(nasc)
print('-==-'*10)