import requests
from tkinter import*
janela=tk()
janela.title('Sua média aqui')
print('Calcule sua média')
n1=int(input('Sua nota na 1a prova:'))
n2=int(input('Sua nota na 2a prova:'))
n3=int(input('Sua nota na prova discursiva:'))
n4=int(input('Sua nota na prova Final:'))
m1=n1*2
m2=n2*2
m3=n3*2
m4=n4*4
t=(m1+m2+m3+m4)/10
print('Sua nota final é {}'.format(t))

janela = Tk()
janela.title('Média Uniasselvi')




janela.mainloop()