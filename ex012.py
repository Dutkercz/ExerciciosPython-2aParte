print('Calcular o preço final de um produto em promoção de ?%')
prod= float(input('Qual o preço do produto? R$ '))
desc1= float(input('Quanto consigo de desconto? em % '))
total= (100-desc1)/100 *prod
print('O valor desse produto com desconto de {}% é de RS {:.2f}'.format(desc1, total))

print('='*60)

prod2=float(input('Usando outra formula, diga novamente o preço do produto? R$'))
desc=float(input('Quanto tem de desconto? em % '))
total2= prod2 - (prod2*desc/100)
print('O valor do seu produto com {}% de desconto, usando outra formula é {:.2f}'.format(desc, total2))