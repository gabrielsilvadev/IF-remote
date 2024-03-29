from tkinter import *
#from tkinter import ttk
#from PIL import Image
#from Tela_de_Registro import *
#from Janela import *
from Banco import *

chamarlogin = False
chamarcastro = False
print("Primeiro false")
      
def TelaLogin():
      corbg = "#321b4a"
      corbt = "#Cb6121"

      root = Tk() # Inicializa o Tkinter
      root.geometry("800x600+0+0") # Dimensão da tela 

      #IMAGEM
      logo = PhotoImage(file = r"lgr.png") # Importa imagem
      logo = logo.subsample(10,10) # Redimensiona o tamanho

      mini = PhotoImage(file = r"43091.png") # importa a imagem do auditorio 
      mini = mini.subsample(8,8)#faz o dimensionamento 

      usuario = PhotoImage(file = r"blank-profile-picture-973460_1280.png") # importa a imagem do usuario  
      usuario = usuario.subsample(18,18)#dimensiona 

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
            nomeu = login(ent1.get(), ent2.get())
            
            if nomeu:
                  global chamarlogin
                  chamarlogin = True
                  print("Recebeu True")
                  root.destroy()
                  
            else:
                  print("e")
            
      def cadastro():
            registro()

      
      
      # BOTÃO DE ENTRAR
      bt = Button(root, text = "ENTRAR", font = ("Times new roman", "10", "bold"), bg = corbt, command = verificar, foreground = "white") # Adiciona um botão
      bt.place(x = 400, y = 450) # Aloca o botão no espaço desejado na tela

      # BOTÃO DE REGISTRO
      bt = Button(root, text = "Registrar-se", font = ("Times new roman", "10", "bold"), bg = corbt, foreground = "white",command=cadastro) # Adiciona um botão
      bt.place(x = 390, y = 500) # Aloca o botão no espaço desejado na tela/
      root['background']="#321b4a"
      root.mainloop() # Roda a tela

      
def janela():
    
    janela = Tk()
    a = ["Mini auditorio","Auditorio","Lab 1","Lab 2","Lab 3","Lab 4","Lab 5 ","Sala de leitura","Quadra","Matematica"] # cria lista 
    #a = banco.return_salas() #retorna a lista de salas do banco 

    #cria o titulo 
    text1=Label(janela, text = 'Reserve', background = '#321B4A')
    text1['fg']='#DFDCE3'
    text1['font']=("Arial","30","bold")
    text1['padx']=120
    text1.place(x=200,y=50)

    mini = PhotoImage(file = r"43091.png") # importa a imagem do auditorio 
    mini = mini.subsample(8,8)#faz o dimensionamento 

    usuario = PhotoImage(file = r"blank-profile-picture-973460_1280.png") # importa a imagem do usuario  
    usuario = usuario.subsample(25,25)#dimensiona 

    button_do_usuario=Button(janela,background="#CB6121",image=usuario)#butao do usuario que esta recebendo  a imagem 
    button_do_usuario['font']=("Arial","8")# regulando a fonte 
    button_do_usuario['fg']='#DFDCE3'# cor da fonte 
    button_do_usuario["width"] = 120 # largura do botao 
    button_do_usuario["height"] = 100 # altura do botao 
    button_do_usuario.place(x = 15, y = 15)# dimensionamento do butao 

    #texto que fica sobre o butao 
    text2=Label(janela,text=nome,background="#321B4A",foreground='white')
    text2['padx']=20
    text2['pady']=3
    text2['font']=("Arial","8",'bold')
    text2.place(x = 30, y = 120)
    # button do auditorio esta recebendo a imagem do mesmo 
    button1=Button(janela,background="#CB6121", image=mini)
    button1['font']=("Arial","8")#tamanho da letra 
    button1['fg']='#DFDCE3' #cor da fonte 
    button1["width"] = 120
    button1["height"] = 100
    button1.place(x = 35, y = 150)

    # caixa de texto que esta recebendo o nome do auditorio atravez do indice 
    text3=Label(janela,text=a[1],background="#CB6121",foreground='white')
    text3['padx']=20
    text3['pady']=3
    text3['font']=("Arial","8",'bold')
    text3.place(x = 41, y = 230)

    auditorio= PhotoImage(file = r"palestra-de-professores-em-frente-a-um-auditorio.png") # importando a imagem 
    auditorio= auditorio.subsample(10,10) #dimensionando 

    #butao do auditorio esta revcendo uma imagem 
    button2=Button(janela,background="#CB6121", image=auditorio)
    button2['font']=("Arial","8")
    button2['fg']='#DFDCE3'
    button2["width"] = 120
    button2["height"] = 100
    button2.place(x = 340, y = 150)

    # caixa de texto esta recendo o nome do mini auditorio atravez do indice 
    text4=Label(janela,text=a[0],background="#CB6121",foreground='white')
    text4['padx']=20
    text4['pady']=3
    text4['font']=("Arial","8",'bold')
    text4.place(x = 345, y = 230)

    #importando a imagem quadra 
    quadra = PhotoImage(file = r"quadra-de-futebol.png") 
    quadra = quadra.subsample(7,7)

    #criando button onde vai receber a imagem auditorio 
    button3=Button(janela,background="#CB6121", image=quadra)
    button3['font']=("Arial","8")
    button3["width"] = 120
    button3['fg']='#DFDCE3'
    button3["height"] = 100
    button3.place(x = 490, y = 150)

    #caqixa de texto esta recendo o nome da quadra atravez do indice 
    text5=Label(janela,text=a[8],background="#CB6121",foreground='white')
    text5['padx']=10
    text5['pady']=3
    text5['font']=("Arial","8",'bold')
    text5.place(x = 510, y = 230)

    #importando a imagem 
    pi = PhotoImage(file = r"pi-simbolo-constante-matematica.png") 
    pi = pi.subsample(10,10)

    # cirando botao que recebe a imagem  
    button4=Button(janela,background="#CB6121",image=pi)
    button4['font']=("Arial","8")
    button4["width"] = 120
    button4['fg']='#DFDCE3'
    button4["height"] = 100
    button4.place(x = 190, y = 150)

    #caixa de texto que recebe o nome da sala de estudo atraves do indice 
    text6=Label(janela,text=a[9],background="#CB6121",foreground='white')
    text6['padx']=10
    text6['pady']=3
    text6['font']=("Arial","8",'bold')
    text6.place(x = 199, y = 230)
    #importando a imagem 
    sala_de_leitura = PhotoImage(file = r"livros.png") 
    sala_de_leitura = sala_de_leitura.subsample(10,10)
    #criando um botao que recebe a imagem 
    button5=Button(janela,background="#CB6121", image=sala_de_leitura)
    button5['font']=("Arial","8")
    button5["width"] = 120
    button5['fg']='#DFDCE3'
    button5["height"] = 100
    button5.place(x = 640, y = 150)
    #caixa de   texto que recebe  o nome atraves do indice 
    text7=Label(janela,text=a[7],background="#CB6121",foreground='white')
    text7['padx']=10 
    text7['pady']=3
    text7['font']=("Arial","8",'bold')
    text7.place(x = 645, y = 231)
    #importando a imagem dos laboratorios 
    lab = PhotoImage(file = r"computer.png") 
    lab = lab.subsample(10,10)

    # criando button  que recebe a foto lab
    button7=Button(janela,background="#CB6121",image = lab)
    button7['font']=("Arial","8")
    button7["width"] = 120
    button7['fg']='#DFDCE3'
    button7["height"] = 100
    button7.place(x = 35, y = 300)

    # criando caixa de texto que acessa pelo indice o nome do lab1
    text8=Label(janela,text=a[2],background="#CB6121",foreground='white')
    text8['padx']=10
    text8['pady']=3
    text8['font']=("Arial","8",'bold')
    text8.place(x =36 , y = 380)


    #criando button que vai receber a imagem 
    button=Button(janela, background="#CB6121",image=lab)
    button['text']="lab"
    button["width"] = 120
    button["height"] = 100
    button['fg']='#DFDCE3'
    button.place(x = 340, y = 300)

    button=Button(janela, background="#CB6121",image=lab)
    button['text']="lab"
    button["width"] = 120
    button["height"] = 100
    button['fg']='#DFDCE3'
    button.place(x = 195, y = 300)
    # criando caixa de texto que acessa o nome do lab atraqvs do indice da lista 
    text9=Label(janela,text=a[3],background="#CB6121",foreground='white')
    text9['padx']=10
    text9['pady']=3
    text9['font']=("Arial","8",'bold')
    text9.place(x = 200, y = 380)

    #criando caixa de texto que vai receber o nome atarves do indice 
    text10=Label(janela,text=a[4],background="#CB6121",foreground='white')
    text10['padx']=10
    text10['pady']=3
    text10['font']=("Arial","8",'bold')
    text10.place(x = 355, y = 380)

    #criando button que vai receber a imagem 
    button9=Button(janela, background="#CB6121",image=lab)
    button9['font']=("Arial","8")
    button9["width"] = 120
    button9['fg']='#DFDCE3'
    button9["height"] = 100
    button9.place(x = 490, y = 300)
    #criando caixa de texto que vai receber indice 
    text11=Label(janela,text=a[5],background="#CB6121",foreground='white')
    text11['padx']=10
    text11['pady']=3
    text11['font']=("Arial","8",'bold')
    text11.place(x = 500, y = 380)
            
    #criando button que vai receber a imagem 
    button10=Button(janela,background="#CB6121",image=lab)
    button10['font']=("Arial","8")
    button10["width"] = 120
    button10['fg']='#DFDCE3'
    button10["height"] = 100
    button10.place(x = 640, y = 300)
    #criando t5exto que acessa o nome ataves do indice 
    text12=Label(janela,text=a[6],background="#CB6121",foreground='white')
    text12['padx']=10
    text12['pady']=3
    text12['font']=("Arial","8",'bold')
    text12.place(x = 642, y = 380)

    janela.geometry('800x600+0+0')#dimensionando na tela 
    janela['background']='#321b4a'#configurando a cor de fundo 
    janela.mainloop()# criando laco para manter a tela aberta


def registro():
      corbg = "#321b4a"
      corbt = "#Cb6121"

      janela = Tk() # Inicializa o Tkinter

      #FUNDO - BACKGROUND

      janela.configure(background = "#321b4a") # Cor de fundo

    #VARIÁVEIS NA TELA
      lb1 = Label(janela, text = "Nome:", font =("Times New Roman", "15", "bold"), bg = corbg, foreground = "white") # Espaço para variáveis de nome
      lb2 = Label(janela, text = "Email:", font =("Times New Roman", "15", "bold"), bg = corbg, foreground = "white") # Espaço para variáveis de nome
      lb3 = Label(janela, text = "Senha:", font =("Times New Roman", "15", "bold"), bg = corbg, foreground = "white") # Espaço para variáveis de nome
      lb4 = Label(janela, text = "CRIAR CONTA RESERVE", font =("Times New Roman", "30", "bold"), bg = corbg, foreground = "white") # Espaço para variáveis de nome

      #DIMENSIONAMENTO DAS VARIÁVEIS NA TELA
      lb1.place(x = 150, y = 150) # Aloca os nomes no espaço desejado na tela
      lb2.place(x = 150, y= 200) # Aloca os nomes no espaço desejado na tela
      lb3.place(x = 150, y= 250) # Aloca os nomes no espaço desejado na tela
      lb4.place(x = 180, y= 50) # Aloca os nomes no espaço desejado na tela

      ent1 = Entry(janela, width = 50) # Dimensiona o tamanho da caixa de texto
      ent2 = Entry(janela, width = 50) # Dimensiona o tamanho da caixa de texto
      ent3 = Entry(janela, width = 50,show="*") # Dimensiona o tamanho da caixa de texto

      ent1.place(x = 310, y = 155) # Aloca a caixa de texto no espaço desejado
      ent2.place(x = 310, y = 205) # Aloca a caixa de texto no espaço desejado
      ent3.place(x = 310, y = 255) # Aloca a caixa de texto no espaço desejado

      def sigan_in():
            janela.destroy()

      def cadastro_usuario():
            nome  = ent1.get()
            email = ent2.get()
            senha = ent3.get()

            if nome and email and senha:
                  cadastro_prof(ent1.get(), ent2.get(), ent3.get())
                
                
            else:
                  msn = Label(janela, text = "preencha todos os dados")
                  msn.pack(side=TOP)

      bt = Button(janela, text = "Registrar-se", font = ("Times new roman", "10", "bold"), bg = corbt, foreground = "white", command=cadastro_usuario) # Adiciona um botão
      bt.place(x = 400, y = 300) # Aloca o botão no espaço desejado na tela

      bt = Button(janela, text = "Entrar", font = ("Times new roman", "10", "bold"), bg = corbt, foreground = "white",command=sigan_in) # Adiciona um botão
      bt.place(x = 400, y = 350) # Aloca o botão no espaço desejado na tela

      janela.geometry("800x600+0+0") # Dimensão da tela 
      janela.mainloop() # Roda a tela


TelaLogin()
if chamarlogin:
      print('chegou aqui')
      janela()
      print('é rapaz')
if chamarcadastro:
      print('chegou aqui')
      janela()
      print('é rapaz')
