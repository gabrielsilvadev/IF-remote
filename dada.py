import sqlite3

conn = sqlite3.connect('banco.db') 
c = conn.cursor()

query = [
    "insert into salas (idsalas, disponivel, sala) values (1, 1, 'Auditório')",
    "insert into salas (idsalas, disponivel, sala) values (2, 1, 'Mini Auditório')",
    "insert into salas (idsalas, disponivel, sala) values (3, 1, 'Laboratório 1')",
    "insert into salas (idsalas, disponivel, sala) values (4, 1, ' Laboratório 2 ')",
    "insert into salas (idsalas, disponivel, sala) values (5, 1, 'Laboratório 3')",
    "insert into salas (idsalas, disponivel, sala) values (6, 1, 'Laboratório 4')",
    "insert into salas (idsalas, disponivel, sala) values (7, 1, 'Laboratório 5')",
    "insert into salas (idsalas, disponivel, sala) values (8, 1, 'Sala de Leitura')",
    "insert into salas (idsalas, disponivel, sala) values (9, 1, 'Quadra')",
    "insert into salas (idsalas, disponivel, sala) values (10, 1, 'Laboratório de Matématica')"
]

for q in query:
    c.execute(q)
    conn.commit()

conn.close()

print("Query Ok!")