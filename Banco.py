import sqlite3

class Banco():
    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.cadastro() 
        self.salas()
        self.reserva()

    def cadastro(self):
        c = self.conexao.cursor()
        c.execute("""create table if not exists cadastro (
                  idusuario integer primary key autoincrement,
                  nome text,
                  telefone text,
                  email text,
                  senha text)""")
        self.conexao.commit()
        c.close()

    def salas(self):
        c = self.conexao.cursor()
        c.execute("""create table if not exists salas (
                  idsalas integer primary key,
                  disponivel integer,
                  sala text)""")
        self.conexao.commit()
        c.close()

    def reserva(self):
        c = self.conexao.cursor()
        c.execute("""create table if not exists reserva (
                  idreserva integer primary key autoincrement,
                  data text,
                  idsala integer)""")
        self.conexao.commit()
        c.close()

    def return_salas(self):      
        salas = []
        try:
            c = self.conexao.cursor()
            for sala in c.execute("select sala from salas"):
                salas.append(sala)
            c.close()
            print(salas)
            print('acesso ativo')
            return salas
        except:
            return 'acesso negado'