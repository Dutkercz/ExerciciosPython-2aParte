from tkinter import mainloop

print('Calcule a Média')
n1=float(input('Digite a primeira nota: '))
n2=float(input('Digite a segunda nota: '))
m= (n1+n2) / 2
print('A média entre {:.1f} e {:.1f} é {:.1f}:'.format (n1, n2, m))

