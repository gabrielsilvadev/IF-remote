from tkinter import*
from tkinter import ttk
from PIL import Image
corbg = "#321b4a"
corbt = "#Cb6121"

janela = Tk() # Inicializa o Tkinter
#IMAGEM
logo = PhotoImage(file = "Imagens\lgr.png") # Importa imagem
logo = logo.subsample(10,10) # Redimensiona o tamanho
logo1 = Label(janela, image = logo, background = "#321b4a") # Atribui um espaço para alocação da mesma na tela
logo1.place(x = 300, y = 50) # Aloca no espaço desejado na tela
logo.configure(background = "#321b4a") # Cor de fundo

#VARIÁVEIS NA TELA
lb1 = Label(janela, text = "Login:", font =("Times New Roman", "15", "bold"), bg = corbg, foreground = "white") # Espaço para variáveis de nome
lb2 = Label(janela, text = "Senha:", font =("Times New Roman", "15", "bold"), bg = corbg, foreground = "white") # Espaço para variáveis de nome

#DIMENSIONAMENTO DAS VARIÁVEIS NA TELA
lb1.place(x = 200, y = 350) # Aloca os nomes no espaço desejado na tela
lb2.place(x = 200, y= 400) # Aloca os nomes no espaço desejado na tela

ent1 = Entry(janela, width = 50) # Dimensiona o tamanho da caixa de texto
ent2 = Entry(janela, width = 50) # Dimensiona o tamanho da caixa de texto

ent1.place(x = 280, y = 355) # Aloca a caixa de texto no espaço desejado
ent2.place(x = 280, y = 405) # Aloca a caixa de texto no espaço desejado

# BOTÃO DE ENTRAR
bt = Button(janela, text = "ENTRAR", font = ("Times new roman", "10", "bold"), bg = corbt, foreground = "white") # Adiciona um botão
bt.place(x = 400, y = 450) # Aloca o botão no espaço desejado na tela


# BOTÃO DE REGISTRO
bt = Button(janela, text = "Registrar-se", font = ("Times new roman", "10", "bold"), bg = corbt, foreground = "white") # Adiciona um botão
bt.place(x = 390, y = 500) # Aloca o botão no espaço desejado na tela

janela.geometry("800x600+0+0") # Dimensão da tela 
janela.mainloop() # Roda a tela





