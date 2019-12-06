from tkinter import *
from tkinter import ttk
#from PIL import Image

from Janela import *

import Banco

corbg = "#321b4a"
corbt = "#Cb6121"

root = Tk() # Inicializa o Tkinter
root.geometry("800x600+0+0") # Dimensão da tela 

#IMAGEM
logo = PhotoImage(file = r"lgr.png") # Importa imagem
logo = logo.subsample(10,10) # Redimensiona o tamanho

#logo.configure(background = "#321b4a") # Cor de fundo
logo1 = Label(root, image = logo, background = "#321b4a") # Atribui um espaço para alocação da mesma na tela
logo1.place(x = 300, y = 50) # Aloca no espaço desejado na tela

#VARIÁVEIS NA TELA
lb1 = Label(root, text = "Login:", font =("Times New Roman", "15", "bold"), bg = corbg, foreground = "white") # Espaço para variáveis de nome
lb2 = Label(root, text = "Senha:", font =("Times New Roman", "15", "bold"), bg = corbg, foreground = "white") # Espaço para variáveis de nome

#DIMpedro@ENSIONAMENTO DAS VARIÁVEIS NA TELA
lb1.place(x = 200, y = 350) # Aloca os nomes no espaço desejado na tela
lb2.place(x = 200, y= 400) # Aloca os nomes no espaço desejado na tela

ent1 = Entry(root, width = 50) # Dimensiona o tamanho da caixa de texto
ent2 = Entry(root, width = 50, show="*") # Dimensiona o tamanho da caixa de texto

ent1.place(x = 280, y = 355) # Aloca a caixa de texto no espaço desejado
ent2.place(x = 280, y = 405) # Aloca a caixa de texto no espaço 

def verificar():
      if Banco.login(ent1.get(), ent2.get()):
            test(root)
            root.destroy()
      else:
            print("e")
      
# BOTÃO DE ENTRAR
bt = Button(root, text = "ENTRAR", font = ("Times new roman", "10", "bold"), bg = corbt, command = verificar, foreground = "white") # Adiciona um botão
bt.place(x = 400, y = 450) # Aloca o botão no espaço desejado na tela

# BOTÃO DE REGISTRO
bt = Button(root, text = "Registrar-se", font = ("Times new roman", "10", "bold"), bg = corbt, foreground = "white") # Adiciona um botão
bt.place(x = 390, y = 500) # Aloca o botão no espaço desejado na tela/
root['background']="#321b4a"
root.mainloop() # Roda a tela
