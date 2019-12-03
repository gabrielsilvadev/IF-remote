from Banco import Banco

def cadastro(nome, email, senha):
    banco = Banco()
    try:
        c = banco.conexao.cursor()
        c.execute("insert into cadastro(nome, email, senha) values ('"+nome+"','"+email+"','"+senha+"')" )
        banco.conexao.commit()
        c.close()
        return "usuario cadastrado com sucesso"
    except:
        return "o correu um erro"
    
def login( email, senha):
    banco = Banco()
    user=[]
    try:
        c = banco.conexao.cursor()
        c.execute("select * from cadastro where email = '" + email + "' and senha = '" + senha + "'")
        for linha in c:
            apend.email=linha[2]
            user.senha=linha[3]
        c.close()
        print('acesso ativo')
        return user
    except:
        return 'acesso negado'
