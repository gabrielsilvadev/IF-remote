from Banco import Banco

class Usuarios(object):
    
    def __init__(self, idusuario = 0, nome = '', telefone = '', email = '', senha = ''):
        self.idusuario = idusuario
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.senha = senha

    def cadastro(self, nome, telefone, email, senha):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("insert into cadastro (nome, telefone, email, senha) values ('"+nome+"','"+telefone+"','"+email+"','"+senha+"')" )
            banco.conexao.commit()
            c.close()
            return "usuario cadastrado com sucesso"
        except:
            return "o correu um erro"
    
    def login(self, email, senha):
        banco = Banco()
        user  = Usuarios()
        try:
            c = banco.conexao.cursor()
            c.execute("select * from cadastro where email = '" + email + "' and senha = '" + senha + "'")
            for linha in c:
                user.email=linha[2]
                user.senha=linha[3]
            c.close()
            print('acesso ativo')
            return user
        except:
            return 'acesso negado'
