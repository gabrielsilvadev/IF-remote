import sqlite3 # importando o banco 


def cadastro_prof(nome, email, senha):
        ini = conexao.cursor()
        ini.execute('''INSERT INTO cadastro(nome, email, senha)
                VALUES (?,?,?)''', (nome, email, senha))
        conexao.commit()
        print("ok")
        ini.close()
        return "usuario cadastrado com sucesso"

        
def login(email, senha):
        c = conexao.cursor()
        c.execute("select * from cadastro where email='" + email + "'")
        for linha in c:
                if senha == linha[3]:
                        return True                        
                else:
                        print("erro")
        c.close()
            

conexao = sqlite3.connect('banco.db') #conexao com o data base 
c = conexao.cursor() #iniciando a conexao da tabelas em si 
                                  # executa a criacão da tabelas se nao ouver outra com o mesmo nome 
                                  #cria um id autoingrementavel ouseja automaticamente para o usuario 
                                  #cria uma linhas da tabela com a tipagem 

c.execute("""create table if not exists cadastro (       
                  idusuario integer primary key autoincrement,
                  nome varchar(20),
                  email varchar(20),
                  senha varchar(20))""")
conexao.commit() # faz a aquisicao para o banco 
c.close() #fecha a conexao com o banco 

        # criando uma tabela
c = conexao.cursor()#iniciando a conexao da tabelas em si 
        # executa a criancao da tabelas se nao ouver outra com o mesmo nome 
        #cria um id autoingremtavel ouseja automaticamente para o usuario 
        #cria uma linhas da tabela com a tipagem 
c.execute("""create table if not exists salas (
                  idsalas integer primary key,
                  disponivel integer,
                  sala text)""")
conexao.commit() # faz a aquisicao para o banco 
c.close() #fecha a conexao com o banco
        
c = conexao.cursor()#iniciando a conexao da tabelas em si 
        # executa a criancao da tabelas se nao ouver outra com o mesmo nome 
        #cria um id autoingrementavel ouseja automaticamente para o usuario 
        #cria uma linhas da tabela com a tipagem 
c.execute("""create table if not exists reserva (
            idreserva integer primary key autoincrement,
            data text,
            idsala integer)""")
conexao.commit() # faz a aquisicao para o banco 
c.close()#fecha a conexao com o banco 

#retornando uma lista de salas      
salas = [] #cria uma lista
c = conexao.cursor() 
for sala in c.execute("select sala from salas"):  #esta percorrendo a coluna do banco e adicionando a uma lista 
   salas.append(sala) #adicionando  na lista 
c.close() #fechando uma conexao 

  

