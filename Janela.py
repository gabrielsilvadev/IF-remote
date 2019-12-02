from tkinter import *

from Banco import Banco
#from Pillow import Image, ImageTk
from Usuarios import Usuarios

root = Tk()

banco = Banco()
usuarios = Usuarios()
a = [] 
a = banco.return_salas()


text1=Label(root, text = 'Reserve', background = '#321B4A')
text1['fg']='#DFDCE3'
text1['font']=("Arial","30","bold")
text1['padx']=120
text1.place(x=200,y=50)



mini = PhotoImage(file = r"43091.png") 
mini = mini.subsample(8,8)



usuario = PhotoImage(file = r"blank-profile-picture-973460_1280.png") 
usuario = usuario.subsample(18,18)

text1=Button(root,background="#CB6121",image=usuario)
text1['font']=("Arial","8")
text1['fg']='#DFDCE3'
text1["width"] = 120
text1["height"] = 100
text1.place(x = 15, y = 15)

text=Label(root,text="usuario",background="#321B4A",foreground='white')
text['padx']=20
text['pady']=3
text['font']=("Arial","8",'bold')
text.place(x = 30, y = 120)

button1=Button(root,background="#CB6121", image=mini)
button1['font']=("Arial","8")
button1['fg']='#DFDCE3'
button1["width"] = 120
button1["height"] = 100
button1.place(x = 10, y = 150)

text=Label(root,text=a[1],background="#CB6121",foreground='white')
text['padx']=20
text['pady']=3
text['font']=("Arial","7",'bold')
text.place(x = 17, y = 232)

auditorio= PhotoImage(file = r"palestra-de-professores-em-frente-a-um-auditorio.png") 
auditorio= auditorio.subsample(10,10)

button2=Button(root,background="#CB6121", image=auditorio)
button2['font']=("Arial","8")
button2['fg']='#DFDCE3'
button2["width"] = 120
button2["height"] = 100
button2.place(x = 290, y = 150)


text=Label(root,text=a[0],background="#CB6121",foreground='white')
text['padx']=20
text['pady']=3
text['font']=("Arial","8",'bold')
text.place(x = 307, y = 230)



quadra = PhotoImage(file = r"quadra-de-futebol.png") 
quadra = quadra.subsample(7,7)

button3=Button(root,background="#CB6121", image=quadra)
button3['font']=("Arial","8")
button3["width"] = 120
button3['fg']='#DFDCE3'
button3["height"] = 100
button3.place(x = 430, y = 150)

text2=Label(root,text=a[8],background="#CB6121",foreground='white')
text2['padx']=10
text2['pady']=3
text2['font']=("Arial","8",'bold')
text2.place(x = 460, y = 230)



pi = PhotoImage(file = r"pi-simbolo-constante-matematica.png") 
pi = pi.subsample(10,10)

text1=Button(root,background="#CB6121",image=pi)
text1['font']=("Arial","8")
text1["width"] = 120
text1['fg']='#DFDCE3'
text1["height"] = 100
text1.place(x = 150, y = 150)

text2=Label(root,text=a[9],background="#CB6121",foreground='white')
text2['padx']=10
text2['pady']=3
text2['font']=("Arial","5",'bold')
text2.place(x = 152, y = 237)

photo = PhotoImage(file = r"livros.png") 
photo = photo.subsample(10,10)

text1=Button(root,background="#CB6121", image=photo)
text1['font']=("Arial","8")
text1["width"] = 120
text1['fg']='#DFDCE3'
text1["height"] = 100
text1.place(x = 570, y = 150)

text2=Label(root,text=a[7],background="#CB6121",foreground='white')
text2['padx']=10
text2['pady']=3
text2['font']=("Arial","8",'bold')
text2.place(x = 575, y = 231)

lab = PhotoImage(file = r"computer.png") 
lab = lab.subsample(10,10)

text1=Button(root,background="#CB6121", image =lab)
text1['font']=("Arial","8")
text1['fg']='#DFDCE3'
text1["width"] = 120
text1["height"] = 100
text1.place(x = 10, y = 300)

text2=Label(root,text=a[2],background="#CB6121",foreground='white')
text2['padx']=10
text2['pady']=3
text2['font']=("Arial","8",'bold')
text2.place(x =18 , y = 380)


text1=Button(root,background="#CB6121",image = lab)
text1['font']=("Arial","8")
text1["width"] = 120
text1['fg']='#DFDCE3'
text1["height"] = 100
text1.place(x = 150, y = 300)


text2=Label(root,text=a[3],background="#CB6121",foreground='white')
text2['padx']=10
text2['pady']=3
text2['font']=("Arial","8",'bold')
text2.place(x = 158, y = 380)


text1=Button(root, background="#CB6121",image=lab)
text1['text']="lab"
text1["width"] = 120
text1["height"] = 100
text1['fg']='#DFDCE3'
text1.place(x = 290, y = 300)

text2=Label(root,text=a[4],background="#CB6121",foreground='white')
text2['padx']=10
text2['pady']=3
text2['font']=("Arial","8",'bold')
text2.place(x = 298, y = 380)


text1=Button(root, background="#CB6121",image=lab)
text1['font']=("Arial","8")
text1["width"] = 120
text1['fg']='#DFDCE3'
text1["height"] = 100
text1.place(x = 430, y = 300)

text2=Label(root,text=a[5],background="#CB6121",foreground='white')
text2['padx']=10
text2['pady']=3
text2['font']=("Arial","8",'bold')
text2.place(x = 437, y = 380)
        

text1=Button(root,background="#CB6121",image=lab)
text1['font']=("Arial","8")
text1["width"] = 120
text1['fg']='#DFDCE3'
text1["height"] = 100
text1.place(x = 570, y = 300)

text2=Label(root,text=a[6],background="#CB6121",foreground='white')
text2['padx']=10
text2['pady']=3
text2['font']=("Arial","8",'bold')
text2.place(x = 577, y = 380)


root['background']='#321b4a'
root.geometry('750x500+0+0')
root.mainloop()

