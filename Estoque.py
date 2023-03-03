import pyodbc

dados_conexao = ('Driver={SQL Server};'
                             'Server=EDUARDO-META\SQLEXPRESS;'
                             'Database=estoque;')
conexao = pyodbc.connect(dados_conexao)
print("Conexão bem sucedida!")

cursor = conexao.cursor()

def consultar_estoque():
    comando = """SELECT nome_produto, COUNT(nome_produto) as Quantidade FROM dbo.produtos group by nome_produto"""
    select = cursor.execute(comando)
    tabela = select.fetchall()
    print("Equipamento | Quantidade")
    for linha in tabela :
        print(f"{linha}")

def adicionar_head():
    print('Insira o numero de serie do headset:')
    numero_serie = input()
    comando = f"""insert into dbo.produtos
           (nome_produto,numero_serie)
           values ('headset','{numero_serie}')"""
    comando_insert = cursor.execute(comando)
    cursor.commit()
    print("Equipamento adicionado com sucesso !")
def adicionar_equipamento():
    comando = f"""insert into dbo.produtos
           (nome_produto,numero_serie)
           values ('{equipamento}','{numero_serie}')"""
    insert = cursor.execute(comando)
    cursor.commit()
    print(f"{equipamento} adicionado com sucesso !")

def remover_equipamento():
    comando= f"""delete dbo.produtos where id_produtos in (
            select top 1 id_produtos
            from dbo.produtos where nome_produto = '{equipamento}')"""
    delete_equipamento = cursor.execute(comando)
    cursor.commit()
    print("Equipamento removido com sucesso !")

def remover_headset():
    print("Insira o numero de Serie do Headset")
    numero_de_serie_deletado = int(input())
    comando = f""" delete from dbo.produtos where numero_serie = '{numero_de_serie_deletado}' and nome_produto = 'headset' """
    delete_h7 = cursor.execute(comando)
    cursor.commit()
    print("Headset removido com Sucesso !")

print('Seja bem vindo ao Estoque Meta Positiva')

print('Para visualizar o estoque digite [1], Para adicionar algum equipamento ao estoque digite [2], para remover algum equipamento digite [3] e para sair digite [0]')

resposta1_usuario = int(input())
if resposta1_usuario == 1 :
    consultar_estoque()
    print("Para sair do estoque digite[1]")
    resposta_consulta = int(input())
    if resposta_consulta == 1:
        print("Obrigado por acessar o estoque ")

elif resposta1_usuario == 2 :
    print('se deseja adicionar um headset ao estoque [1], um mouse digite [2] , um monitor digite [3] ou um teclado digite[4]')
    resposta2_usuario = int(input())
    if resposta2_usuario == 1:
        adicionar_head()
        print("Para sair do estoque digite[1]")
        resposta_consulta = int(input())
        if resposta_consulta == 1:
            print("Obrigado por acessar o estoque ")
    elif resposta2_usuario == 2:
        equipamento = "mouse"
        numero_serie = "0"
        adicionar_equipamento()
        print("Para sair do estoque digite[1]")
        resposta_consulta = int(input())
        if resposta_consulta == 1:
            print("Obrigado por acessar o estoque ")
    elif resposta2_usuario == 3:
        equipamento = "monitor"
        numero_serie = "0"
        adicionar_equipamento()
        print("Para sair do estoque digite[1]")
        resposta_consulta = int(input())
        if resposta_consulta == 1:
            print("Obrigado por acessar o estoque ")
    elif resposta2_usuario == 4:
        equipamento = "teclado"
        numero_serie = "0"
        adicionar_equipamento()
        print("Para sair do estoque digite[1]")
        resposta_consulta = int(input())
        if resposta_consulta == 1:
            print("Obrigado por acessar o estoque ")
    else:
        print("Opcao invalida :/")

elif resposta1_usuario == 3 :
    print("Para remover um headset [1], Um mouse [2], um teclado [3] ou um monitor [4]")
    resposta2_usuario = int(input())
    if resposta2_usuario == 1:
        remover_headset()
        print("Para sair do estoque digite[1]")
        resposta_consulta = int(input())
        if resposta_consulta == 1:
            print("Obrigado por acessar o estoque ")
    elif  resposta2_usuario == 2:
        equipamento = "mouse"
        remover_equipamento()
        print("Para sair do estoque digite[1]")
        resposta_consulta = int(input())
        if resposta_consulta == 1:
            print("Obrigado por acessar o estoque ")
    elif resposta2_usuario == 3:
        equipamento = "teclado"
        remover_equipamento()
        print("Para remover mais 1 [1],Para sair do estoque digite[2]")
        resposta_continuar = int(input())
        if resposta_continuar == 1:
                remover_equipamento()
                print("Equipamento Removido ")
        elif resposta_continuar== 2:
            print("Você saiu do Estoque")
    elif resposta2_usuario == 4:
        equipamento = "monitor"
        remover_equipamento()
        print("Para sair do estoque digite[1]")
        resposta_consulta = int(input())
        if resposta_consulta == 1:
            print("Obrigado por acessar o estoque ")
    else:
        print("Opcao invalida :/")

elif resposta1_usuario == 0:
    print("Você optou por sair do Estoque :(")
else:
    print("Opcao invalida :/")