from tkinter import *
from Banco import *

corbg = "#321b4a"
corbt = "#Cb6121"

janela = Tk() # Inicializa o Tkinter

#FUNDO - BACKGROUND

janela.configure(background = "#321b4a") # Cor de fundo

#VARIÁVEIS NA TELA
lb1 = Label(janela, text = "Nome:", font =("Times New Roman", "15", "bold"), bg = corbg, foreground = "white") # Espaço para variáveis de nome
lb2 = Label(janela, text = "Email:", font =("Times New Roman", "15", "bold"), bg = corbg, foreground = "white") # Espaço para variáveis de nome
lb3 = Label(janela, text = "Confirmar email:", font =("Times New Roman", "15", "bold"), bg = corbg, foreground = "white") # Espaço para variáveis de nome
lb4 = Label(janela, text = "Senha:", font =("Times New Roman", "15", "bold"), bg = corbg, foreground = "white") # Espaço para variáveis de nome
lb5 = Label(janela, text = "Confirmar senha:", font =("Times New Roman", "15", "bold"), bg = corbg, foreground = "white") # Espaço para variáveis de nome
lb6 = Label(janela, text = "CRIAR CONTA RESERVE", font =("Times New Roman", "30", "bold"), bg = corbg, foreground = "white") # Espaço para variáveis de nome

#DIMENSIONAMENTO DAS VARIÁVEIS NA TELA
lb1.place(x = 150, y = 150) # Aloca os nomes no espaço desejado na tela
lb2.place(x = 150, y= 200) # Aloca os nomes no espaço desejado na tela
lb3.place(x = 150, y= 250) # Aloca os nomes no espaço desejado na tela
lb4.place(x = 150, y= 300) # Aloca os nomes no espaço desejado na tela
lb5.place(x = 150, y= 350) # Aloca os nomes no espaço desejado na tela
lb6.place(x = 180, y= 50) # Aloca os nomes no espaço desejado na tela

ent1 = Entry(janela, width = 50) # Dimensiona o tamanho da caixa de texto
ent2 = Entry(janela, width = 50) # Dimensiona o tamanho da caixa de texto
ent3 = Entry(janela, width = 50) # Dimensiona o tamanho da caixa de texto
ent4 = Entry(janela, width = 50,show="*") # Dimensiona o tamanho da caixa de texto
ent5 = Entry(janela, width = 50,show="*") # Dimensiona o tamanho da caixa de texto

ent1.place(x = 310, y = 155) # Aloca a caixa de texto no espaço desejado
ent2.place(x = 310, y = 205) # Aloca a caixa de texto no espaço desejado
ent3.place(x = 310, y = 255) # Aloca a caixa de texto no espaço desejado
ent4.place(x = 310, y = 300) # Aloca a caixa de texto no espaço desejado
ent5.place(x = 310, y = 355) # Aloca a caixa de texto no espaço desejado

def cadastro_usuario():
     if 
       cadastro_prof(ent1.get(), ent2.get(), ent4.get())
# BOTÃO
bt = Button(janela, text = "Registrar-se", font = ("Times new roman", "10", "bold"), bg = corbt, foreground = "white", command=cadastro_usuario) # Adiciona um botão
bt.place(x = 400, y = 450) # Aloca o botão no espaço desejado na tela

janela.geometry("800x600+0+0") # Dimensão da tela 
janela.mainloop() # Roda a tela
