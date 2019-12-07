from tkinter import *
import sqlite3
from freserva import *

def telareserva():

    #funções

    def reservarhorario():
        if ent1.get():
            sala = ent1.get()
            data = ent2.get()
            hora = ent3.get()
            a = verificar(sala, data, hora)
        ent1.delete(0,END)
        ent2.delete(0,END)
        ent3.delete(0,END)
        print('passou por aqui')

        if(a):
            print('Deu certo')
            lb5['text']="Reserva feita com sucesso!"
        else:
            lb5['text']="Este horário já está reservado, consulte a lista!"
               

    corbg = "#321b4a"
    corbt = "#Cb6121"

    janela = Tk()
    frame1 = Frame(janela, bg=corbg, width="40", height="600")
    frame2 = Frame(janela, bg=corbg, width="800", height="600")
    #frame3 = Frame(janela, bg=corbg)

    #frame3.pack(side=TOP, fill = X)
    frame1.pack(side=LEFT)
    frame2.pack(side=LEFT)
    


    lb1 = Label(frame2, text="Reserve uma sala!",font=("Times New Roman", "40", "bold"), bg=corbg, foreground='white')
    lb2 = Label(frame2, text="Sala:",font=("Arial", "15", "bold"), bg=corbg, foreground='white')
    lb3 = Label(frame2, text="Data:",font=("Arial", "15", "bold"), bg=corbg, foreground='white')
    lb4 = Label(frame2, text="Horário:",font=("Arial", "15", "bold"), bg=corbg, foreground='white')
    lb5 = Label(frame2, text="", font=("Arial", "15", "bold"), bg=corbg, foreground='white')

    lb1.place(x=145, y=90)
    lb2.place(x=10, y=250)
    lb3.place(x=10,y=300)
    lb4.place(x=10, y=350)
    lb5.place(x=100, y=500)


    ent1 = Entry(frame2, width=40)
    ent2 = Entry(frame2, width=40)
    ent3 = Entry(frame2, width=40)

    ent1.place(x=100, y=255)
    ent2.place(x=100, y=305)
    ent3.place(x=100, y=355)


    bt1 = Button(frame2, text="Reservar", font=("Arial", "10", "bold"), bg=corbt, foreground='white', width=20, height=2, command=reservarhorario)
    bt2 = Button(frame2, text="Lista de salas reservadas", font=("Arial", "10", "bold"), bg=corbt, foreground='white', width=20, height=2, command=listarr)

    bt1.place(x=130, y=400)
    bt2.place(x=130, y=450)

    janela.geometry('800x600+0+0')
    janela.resizable(width=0, height=0)
    janela.mainloop()

telareserva()
