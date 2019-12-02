from tkinter import *
#from Pillow import Image, ImageTk

root = Tk()


text1=Label(root, text = 'Reserve', background = '#321B4A')
text1['fg']='#DFDCE3'
text1['font']=("Arial","25","bold")
text1['padx']=120
text1.pack()

pi = PhotoImage(file = r"pi-simbolo-constante-matematica.png") 
pi = pi.subsample(7,7)

text1=Button(root,background="#CB6121", image=pi)
text1['font']=("Arial","8")
text1['fg']='#DFDCE3'
text1["width"] = 120
text1["height"] = 100
text1.place(x = 10, y = 150)




auditorio= PhotoImage(file = r"palestra-de-professores-em-frente-a-um-auditorio.png") 
auditorio= auditorio.subsample(7,7)

text1=Button(root,background="#CB6121", image=auditorio)
text1['font']=("Arial","8")
text1['fg']='#DFDCE3'
text1["width"] = 120
text1["height"] = 100
text1.place(x = 290, y = 150)

lab = PhotoImage(file = r"computer.png") 
lab = lab.subsample(7,7)

text1=Button(root,background="#CB6121", image =lab)
text1['font']=("Arial","8")
text1['fg']='#DFDCE3'
text1["width"] = 120
text1["height"] = 100
text1.place(x = 10, y = 300)

text1=Button(root,background="#CB6121",image = lab)
text1['font']=("Arial","8")
text1["width"] = 120
text1['fg']='#DFDCE3'
text1["height"] = 100
text1.place(x = 150, y = 300)

text1=Button(root, background="#CB6121",image=lab)
text1['text']="lab"
text1["width"] = 120
text1["height"] = 100
text1['fg']='#DFDCE3'
text1.place(x = 290, y = 300)

text1=Button(root, background="#CB6121",image=lab)
text1['font']=("Arial","8")
text1["width"] = 120
text1['fg']='#DFDCE3'
text1["height"] = 100
text1.place(x = 430, y = 300)
        
text1=Button(root,background="#CB6121",image=lab)
text1['font']=("Arial","8")
text1["width"] = 120
text1['fg']='#DFDCE3'
text1["height"] = 100
text1.place(x = 570, y = 300)

quadra = PhotoImage(file = r"quadra-de-futebol.png") 
quadra = quadra.subsample(7,7)

text1=Button(root,background="#CB6121", image=quadra)
text1['font']=("Arial","8")
text1["width"] = 120
text1['fg']='#DFDCE3'
text1["height"] = 100
text1.place(x = 430, y = 150)

pi = PhotoImage(file = r"pi-simbolo-constante-matematica.png") 
pi = pi.subsample(7,7)

text1=Button(root,background="#CB6121",image=pi)
text1['font']=("Arial","8")
text1["width"] = 120
text1['fg']='#DFDCE3'
text1["height"] = 100
text1.place(x = 150, y = 150)
a = banco.return_salas()

photo = PhotoImage(file = r"livros.png") 
photo = photo.subsample(7,7)
text1=Button(root,background="#CB6121", image=photo)
text1['font']=("Arial","8")
text1["width"] = 120
text1['fg']='#DFDCE3'
text1["height"] = 100
text1.place(x = 570, y = 150)

root['background']='#321B4A'
root.geometry('750x500+0+0')
root.mainloop()

