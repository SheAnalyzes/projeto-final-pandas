import pandas as pd
import pyodbc
# instalção do drive: https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver15
# Lendo o arquivo CSV usando o método read_csv

class ConnectionDB:

    def clientFraud():
        df = pd.read_csv("./reports/clients_fraud.csv")
        print(df)
        # Criando uma conexão com o SQL Server
        # conn = pyodbc.connect("Driver={ODBC Driver 18 for SQL Server};Server=tcp:projetosfinalserver.database.windows.net,1433;Database=ProjetoFinal;Uid=projetosfinalserver;Pwd={paamforgbwirj423r%};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
        # cursor = conn.cursor()

        # # Verifica se a tabela já existe
        # table_check_query = "IF OBJECT_ID('dbo.clientFraud', 'U') IS NULL CREATE TABLE clientFraud (id INT, cliente_id VARCHAR(100), nome VARCHAR(100), email , telefone , cliente_id_fraude_counts , valor );"
        # cursor.execute(table_check_query)
        # conn.commit()
        # # Loop através de cada linha no DataFrame
        # for index, row in df.iterrows():
        #     # Inserindo uma linha na tabela
        #     linha = row[0].split(";")
        #     cursor.execute("INSERT INTO clientFraud ([id], [nome], [obs]) VALUES (?, ?, ?);", linha[0], linha[1], linha[2])
        # conn.commit()
        # # Exibir clientFraud inseridos na tabela
        # select_query = "SELECT * FROM clientFraud"
        # cursor.execute(select_query)
        # rows = cursor.fetchall()
        # for row in rows:
        #     print(row)
        # # Fechando a conexão
        # conn.close()
        # cursor.close()
        return

    def clients_fraud():
        df = pd.read_csv("./arquivos_carga_csv/clients-002.csv")
        # Criando uma conexão com o SQL Server
        conn = pyodbc.connect("Driver={ODBC Driver 18 for SQL Server};Server=tcp:projetosfinalserver.database.windows.net,1433;Database=ProjetoFinal;Uid=projetosfinalserver;Pwd={paamforgbwirj423r%};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
        cursor = conn.cursor()

        # Verifica se a tabela já existe
        table_check_query = "IF OBJECT_ID('dbo.dados', 'U') IS NULL CREATE TABLE dados (id INT, nome VARCHAR(100), obs VARCHAR(100));"
        cursor.execute(table_check_query)
        conn.commit()
        # Loop através de cada linha no DataFrame
        for index, row in df.iterrows():
            # Inserindo uma linha na tabela
            linha = row[0].split(";")
            cursor.execute("INSERT INTO dados ([id], [nome], [obs]) VALUES (?, ?, ?);", linha[0], linha[1], linha[2])
        conn.commit()
        # Exibir dados inseridos na tabela
        select_query = "SELECT * FROM dados"
        cursor.execute(select_query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        # Fechando a conexão
        conn.close()
        cursor.close()
        return






























