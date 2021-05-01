import mysql.connector

def principal():
    
    print("Sistema de gerenciamento de banco de dados")
    aux = int(input("Escolha a opção desejada escolhendo o número: (1)-Select / (2)-Insert / (3)-Update / (4)-Delete"))

    if aux == 1:
        select()
    if aux == 2:
        insert()
    if aux == 3:
        update()
    if aux == 4:
        delete()

def select():
    conexao = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = '',
        database = 'crud'
    )

    cursor = conexao.cursor()
    print(conexao)

    cursor.execute('SELECT * from pessoas')
    result = cursor.fetchall()
    for x in result:
        print(x)
    
    conexao.close()
    principal()

def insert():
    conexao = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = '',
        database = 'crud'
    )

    cursor = conexao.cursor()
    print(conexao)

    nome = str(input("Digite o nome completo: "))
    idade = int(input("Digite a idade: "))
    email = str(input("Digite o email: "))

    sql = 'INSERT into pessoas (nome, idade, email) values ( %s, %s, %s)'
    val = [nome, idade, email]
    cursor.execute(sql, val)
    conexao.commit()
    print(val)
    print(cursor.rowcount, 'registro(s) inserido(s)')

    aux = (input("Deseja inserir um novo registro? S/N"))
    if aux == 'S' or aux == 's':
        insert()
    else:
        conexao.close()
        principal()

def update():
    conexao = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = '',
        database = 'crud'
    )

    cursor = conexao.cursor()
    print(conexao)
    
    x = int(input("Digite o código do registro que deseja atualizar: "))
    nome = str(input("Digite o nome atualizado"))

    sql = 'UPDATE pessoas set nome = %s where cod_pess = %s'
    val = [nome, x]
    cursor.execute(sql, val)
    conexao.commit()
    print(cursor.rowcount, 'Registo(s) atualizado(s)')

    aux = (input("Deseja atualizar um novo registro? S/N"))
    if aux == 'S' or aux == 's':
        update()
    else:
        conexao.close()
        principal()

def delete():
    conexao = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = '',
        database = 'crud'
    )

    cursor = conexao.cursor()
    print(conexao)
    
    x = int(input("Digite o código do registro que deseja deletar: "))
    sql = 'DELETE from pessoas where cod_pess = %s'
    val = [x]
    
    cursor.execute(sql, val)
    conexao.commit()
    print(cursor.rowcount, 'Registo(s) deletado(s)')

    aux = (input("Deseja deletar um novo registro? S/N"))
    if aux == 'S' or aux == 's':
        delete()
    else:
        conexao.close()
        principal()

principal()