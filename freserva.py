import sqlite3
from tkinter import *

conexão = sqlite3.connect("banco1.db")

cursor = conexão.cursor()
cursor.execute('''
    create table if not exists reservar(
        sala varchar,
        data varchar,
        hora varchar)       
    ''')
conexão.commit()
print("certo")
cursor.close()
conexão.close()

def reservar(sala, data, hora):
    conexão = sqlite3.connect("banco1.db")
    cursor = conexão.cursor()
    cursor.execute('''
        insert into reservar (sala, data, hora)
        values(?, ?, ?)
        ''', (sala, data, hora))
    conexão.commit()
    print("ok")
    cursor.close()
    conexão.close()

def verificar(sala, data, hora):
    conexão = sqlite3.connect("banco1.db")
    cursor = conexão.cursor()
    cursor.execute("select * from reservar")
    consulta=cursor.fetchall()
    horario = (sala, data, hora)
    a = 0
    for linha in consulta:
        if(horario == linha):
            print('Error')
            return False
        
    reservar(sala, data, hora)

    cursor.close()
    conexão.close()
    return True

def listarr():
    janela = Tk()
    conexão = sqlite3.connect('banco1.db')
    cursor = conexão.cursor()
    cursor.execute("""
    SELECT * FROM reservar;
    """)    

    corbg = "#321b4a"
    corbt = "#Cb6121"

    janela['bg']=corbg
    
    linhas = 1

    lb_lista = Label(janela,text='SALA', font=("Arial", "15", "bold"), bg=corbg, foreground='white')
    lb_lista.grid(row=0,column=0)

    lb_lista = Label(janela,text='DATA', font=("Arial", "15", "bold"), bg=corbg, foreground='white')
    lb_lista.grid(row=0,column=1)

    lb_lista = Label(janela,text='HORA', font=("Arial", "15", "bold"), bg=corbg, foreground='white')
    lb_lista.grid(row=0,column=2)
    
    for linha in cursor.fetchall():

        lb_lista = Label(janela,text=linha[0],font=("Arial", "10", "bold"), bg=corbg, foreground='white')
        lb_lista.grid(row=linhas,column=0)

        lb_lista = Label(janela,text=linha[1],font=("Arial", "10", "bold"), bg=corbg, foreground='white')
        lb_lista.grid(row=linhas,column=1)

        lb_lista = Label(janela,text=linha[2],font=("Arial", "10", "bold"), bg=corbg, foreground='white')
        lb_lista.grid(row=linhas,column=2)
        
        linhas +=1

    cursor.close()
    conexão.close()
    janela.geometry('200x300+0+0')
    janela.resizable(width=0, height=0)
    janela.mainloop()

