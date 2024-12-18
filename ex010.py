
din=float(input('Quanto dinheiro você tem na carteira? R$ '))
dol=din/5.54
eu=din/6.08
lib=din/7.25
iene=din/0.03727
print('Com R$ {}, você pode comprar U$$ {:.2f}'.format(din, dol))
print('Com R$ {}, você pode comprar EU$ {:.2f}'.format(din,eu))
print('Com R$ {}, você pode comprar £ {:.2f}'.format(din,lib))
print('Com R${}, você pode comprar JP¥   {:.2f}'.format(din,iene))

