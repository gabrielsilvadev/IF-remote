import sqlite3 # importando o banco 

class Banco(): #objeto onde contem os atribultos ouseja funcoes que contem tabelas dentyro do banco 
    
    def __init__(self): #funcao principal que inicia a conexao com o banco alem de iniciar todas as outras funcoes que contem tabelas de dados 
        self.conexao = sqlite3.connect('banco.db') #conexao com o data base 
        self.cadastro() #chamndo a funcao 
        self.salas() #chamndo a funcao 
        self.reserva() #chamada da funcao 

    def cadastro(self):  # criando uma tabela
        c = self.conexao.cursor() #iniciando a conexao da tabelas em si 
        # executa a criancao da tabelas se nao ouver outra com um mesmo nome 
        #cria um id autoingremtavel ouseja automaticamente para o usuario 
        #cria uma linhas da tabela com a tipagem 

        c.execute("""create table if not exists cadastro (       
                  idusuario integer primary key autoincrement,
                  nome text,
                  email text,
                  senha text)""")
        self.conexao.commit() # faz a aquisicao para o banco 
        c.close() #fecha a conexao com o banco 

    def salas(self):# criando uma tabela
        c = self.conexao.cursor()#iniciando a conexao da tabelas em si 
        # executa a criancao da tabelas se nao ouver outra com um mesmo nome 
        #cria um id autoingremtavel ouseja automaticamente para o usuario 
        #cria uma linhas da tabela com a tipagem 
        c.execute("""create table if not exists salas (
                  idsalas integer primary key,
                  disponivel integer,
                  sala text)""")
        self.conexao.commit() # faz a aquisicao para o banco 
        c.close() #fecha a conexao com o banco 

    def reserva(self):
        c = self.conexao.cursor()#iniciando a conexao da tabelas em si 
        # executa a criancao da tabelas se nao ouver outra com um mesmo nome 
        #cria um id autoingremtavel ouseja automaticamente para o usuario 
        #cria uma linhas da tabela com a tipagem 
        c.execute("""create table if not exists reserva (
                  idreserva integer primary key autoincrement,
                  data text,
                  idsala integer)""")
        self.conexao.commit() # faz a aquisicao para o banco 
        c.close()#fecha a conexao com o banco 

    def return_salas(self):#retornando uma lista de salas      
        salas = [] #cria uma lista 
        try: #inicia os comandos e casso de errado o except
            c = self.conexao.cursor() #aqtribui uma variavel a conexao 
            for sala in c.execute("select sala from salas"):  #esta percorrendo a coluna do banco e adicionando a uma lista 
                salas.append(sala) #adiconando  na lista 
            c.close() #fechando uma conexao 
            
            return salas # retornado as salas 
        except: # caso o comando de cima nao de certo executa esse comando 
            return 'acesso negado'

    def cadastro_prof(self, nome, email, senha):
        try:
            ini = self.conexao.cursor()
            ini.execute("INSERT INTO cadastro(nome, email, senha)"
                        "values ('" + nome + '\n' "',"
                                 '' + email + '\n' "','"
                                 '' + senha + '\n' "'"
                                ")")
            self.conexao.commit()
            print("ok")
            ini.close()
            return "usuario cadastrado com sucesso"
        except:
            return "o correu um erro"
        
    def login(self, email, senha):
        user=[]
        try:
            c = self.conexao.cursor()
            c.execute("select * from cadastro where email = '" + email + "' and senha = '" + senha + "'")
            for linha in c:
                user.append(linha[2])
                user.append(linha[3])
            c.close()
            print('acesso ativo')
            return user
        except:
            return 'acesso negado'