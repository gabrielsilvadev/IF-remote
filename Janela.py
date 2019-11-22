from tkinter import *

from Banco import Banco
#from PIL import Image, ImageTk
from Usuarios import Usuarios


class Janela:
    
   def __init__(self, master=None):
        self.banco = Banco()
        self.usuarios = Usuarios()
        self.a = []

        #self.photo=PhotoImage(file="blank-profile-picture-973460_1280.png")
        #r=Label(master,image=self.photo)
        #r.pack()

        self.conteiner12 = Frame(master, background = '#4ABDAC')

        self.conteiner12['pady']=40
        self.conteiner12['padx']=300
        self.conteiner12.pack()

        

        self.text1=Label(self.conteiner12, text = 'IF remote', background = '#4ABDAC')
        self.text1['fg']='#DFDCE3'
        self.text1['font']=("Arial","25","bold",)
        self.text1['padx']=120
        self.text1.pack(side=TOP)

        self.auditorio=Frame(master)
        self.auditorio['pady'] = 0
        self.auditorio.place(x = 10, y = 150)

        self.miniauditorio=Frame(master)
        self.miniauditorio['pady'] = 0
        self.miniauditorio.place(x = 290, y = 150)

        self.lab1=Frame(master)
        self.lab1['pady'] = 0
        self.lab1.place(x = 10, y = 300)

        self.lab2=Frame(master)
        self.lab2['pady'] = 0
        self.lab2.place(x = 150, y = 300)
        
        self.lab3=Frame(master)
        self.lab3['pady'] = 0
        self.lab3.place(x = 290, y = 300)
         
        self.lab4=Frame(master)
        self.lab4['pady'] = 0
        self.lab4.place(x = 430, y = 300)

        self.lab5=Frame(master)
        self.lab5['pady'] = 0
        self.lab5.place(x = 570, y = 300)

        self.saladeleitura=Frame(master)
        self.saladeleitura['pady'] = 0
        self.saladeleitura.place(x = 430, y = 150)

        self.quadra=Frame(master)
        self.quadra['pady'] = 0
        self.quadra.place(x = 150, y = 150)
         
        self.laboratorio=Frame(master)
        self.laboratorio['pady'] = 0
        self.laboratorio.place(x = 570, y = 150)
         
        self.a = self.banco.return_salas()

        self.text1=Button(self.auditorio,background="#4ABDAC", text = self.a[0])
        self.text1['font']=("Arial","8")
        self.text1['fg']='#DFDCE3'
        self.text1["width"] = 20
        self.text1["height"] = 7
        self.text1.pack(side=TOP)

        self.text1=Button(self.miniauditorio,background="#4ABDAC", text = self.a[1])
        self.text1['font']=("Arial","8")
        self.text1['fg']='#DFDCE3'
        self.text1["width"] = 20
        self.text1["height"] = 7
        self.text1.pack()

        self.text1=Button(self.lab1,background="#4ABDAC", text = self.a[2])
        self.text1['font']=("Arial","8")
        self.text1['fg']='#DFDCE3'
        self.text1["width"] = 20
        self.text1["height"] = 7
        self.text1.pack(side=TOP)

        self.text1=Button(self.lab2,background="#4ABDAC", text = self.a[3])
        self.text1['font']=("Arial","8")
        self.text1["width"] = 20
        self.text1['fg']='#DFDCE3'
        self.text1["height"] = 7
        self.text1.pack(side=TOP)

        self.text1=Button(self.lab3, background="#4ABDAC",text = self.a[4])
        self.text1['font']=("Arial","8")
        self.text1["width"] = 20
        self.text1["height"] = 7
        self.text1['fg']='#DFDCE3'
        self.text1.pack(side=TOP)

        self.text1=Button(self.lab4, background="#4ABDAC",text = self.a[5])
        self.text1['font']=("Arial","8")
        self.text1["width"] = 20
        self.text1['fg']='#DFDCE3'
        self.text1["height"] = 7
        self.text1.pack(side=TOP)
        
        self.text1=Button(self.lab5,background="#4ABDAC", text = self.a[6])
        self.text1['font']=("Arial","8")
        self.text1["width"] = 20
        self.text1['fg']='#DFDCE3'
        self.text1["height"] = 7
        self.text1.pack(side=TOP)

        self.text1=Button(self.saladeleitura,background="#4ABDAC", text = self.a[7])
        self.text1['font']=("Arial","8")
        self.text1["width"] = 20
        self.text1['fg']='#DFDCE3'
        self.text1["height"] = 7
        self.text1.pack(side=TOP)

        self.text1=Button(self.quadra,background="#4ABDAC", text = self.a[8])
        self.text1['font']=("Arial","8")
        self.text1["width"] = 20
        self.text1['fg']='#DFDCE3'
        self.text1["height"] = 7
        self.text1.pack(side=TOP)

        self.text1=Button(self.laboratorio,background="#4ABDAC", text = self.a[9])
        self.text1['font']=("Arial","8")
        self.text1["width"] = 20
        self.text1['fg']='#DFDCE3'
        self.text1["height"] = 7
        self.text1.pack(side=TOP)

       

       
        


root = Tk()
Janela(root)
root['background']='#DFDCE3'
root.geometry('750x500+0+0')
root.mainloop()
