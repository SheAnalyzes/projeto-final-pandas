import pandas as pd
import pyodbc
# instalção do drive: https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver15
# Lendo o arquivo CSV usando o método read_csv

class ConnectionDB:
    def __init__(self):
        self.conn = None
        self.cursor = None
    
    def connectToDatabase(self):
        try:
            self.conn = pyodbc.connect("Driver={ODBC Driver 18 for SQL Server};Server=tcp:projetosfinalserver.database.windows.net,1433;Database=ProjetoFinal;Uid=projetosfinalserver;Pwd={paamforgbwirj423r%};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
            self.cursor = self.conn.cursor()
            return  self.conn, self.cursor
        
        except Exception as e:
            print(f"Erro de conexão com banco: {e}")
    
    def closeConnection(self):
        self.cursor.close()
        self.conn.close()

    def clients_fraud(self):
        conn, cursor = self.connectToDatabase()
        try:
            df = pd.read_csv("./reports/clients_fraud.csv")

            # Verifica se a tabela já existe        
            table_check_query = "IF OBJECT_ID('dbo.clients_fraud', 'U') IS NULL CREATE TABLE clients_fraud (id INT IDENTITY(1,1) PRIMARY KEY, cliente_id VARCHAR(100), nome VARCHAR(100), email VARCHAR(200), telefone VARCHAR(20), cliente_id_fraude_counts INT, valor INT);"
            cursor.execute(table_check_query)
            conn.commit()

            # Loop através de cada linha no DataFrame
            for index, linha in df.iterrows():
                # Inserindo uma linha na tabela
                cursor.execute("INSERT INTO clients_fraud ([cliente_id], [nome], [email], [telefone], [cliente_id_fraude_counts], [valor]) VALUES (?, ?, ?, ?, ?, ?);", linha[0], linha[1], linha[2], linha[3], linha[4], linha[5])
            conn.commit()
            print("Tabela clients_fraud criada com sucesso!")

        except Exception as e:
            print(f"Erro para criar a tabela clients_fraud ou inserir dados: {e}")


    def clients(self):
        conn, cursor = self.connectToDatabase()
        try:
            df = pd.read_csv("./reports/clients.csv")
           
            # Verifica se a tabela já existe        
            table_check_query = "IF OBJECT_ID('dbo.clients', 'U') IS NULL CREATE TABLE clients (id INT PRIMARY KEY, nome VARCHAR(100), email VARCHAR(200), data_cadastro DATETIMEOFFSET, telefone VARCHAR(20));"
            cursor.execute(table_check_query)
            conn.commit()

            # Loop através de cada linha no DataFrame
            for index, linha in df.iterrows():
                # Inserindo uma linha na tabela
                cursor.execute("INSERT INTO clients ([id], [nome], [email], [data_cadastro], [telefone]) VALUES (?, ?, ?, CONVERT(DATETIMEOFFSET, ?, 127), ?);", linha[0], linha[1], linha[2], linha[3], linha[4])
            conn.commit()
            print("Tabela clients criada com sucesso!")

        except Exception as e:
            print(f"Erro para criar a tabela clients ou inserir dados: {e}")


    def transactions(self):
        conn, cursor = self.connectToDatabase()
        try: 
            df = pd.read_csv("./reports/transactions.csv")

            # Verifica se a tabela já existe                                                    
            table_check_query = "IF OBJECT_ID('dbo.transactions', 'U') IS NULL CREATE TABLE transactions (id INT PRIMARY KEY, cliente_id INT, valor INT, data DATETIMEOFFSET);"
            cursor.execute(table_check_query)
            conn.commit()
            # Loop através de cada linha no DataFrame
            for index, linha in df.iterrows():
                # Inserindo uma linha na tabela
                cursor.execute("INSERT INTO transactions ([id], [cliente_id], [valor], [data]) VALUES (?, ?, ?, CONVERT(DATETIMEOFFSET, ?, 127));", linha[0], linha[1], linha[2], linha[3])
            conn.commit()
            print("Tabela transactions criada com sucesso!")

        except Exception as e:
            print(f"Erro para criar a tabela transactions ou inserir dados: {e}")


    def transaction_fraud(self):
        conn, cursor = self.connectToDatabase()
        try: 
            df = pd.read_csv("./reports/transaction_fraud.csv")

            # Verifica se a tabela já existe                                                    
            table_check_query = "IF OBJECT_ID('dbo.transaction_fraud', 'U') IS NULL CREATE TABLE transaction_fraud (id INT PRIMARY KEY, cliente_id INT, valor INT, data DATETIMEOFFSET, intervalo VARCHAR(20));"
            cursor.execute(table_check_query)
            conn.commit()
            # Loop através de cada linha no DataFrame
            for index, linha in df.iterrows():
                # Inserindo uma linha na tabela
                cursor.execute("INSERT INTO transaction_fraud ([id], [cliente_id], [valor], [data], [intervalo]) VALUES (?, ?, ?, CONVERT(DATETIMEOFFSET, ?, 127), ?);", linha[0], linha[1], linha[2], linha[3], linha[4])
            conn.commit()
            print("Tabela transaction_fraud criada com sucesso!")

        except Exception as e:
            print(f"Erro para criar a tabela transaction_fraud ou inserir dados: {e}")



    # def transaction_in_fraud(self):
    #     conn, cursor = self.connectToDatabase()
    #     try:
    #         df = pd.read_csv("./reports/transaction_in_fraud.csv")

    #         # Verifica se a tabela já existe                                                    
    #         table_check_query = "IF OBJECT_ID('dbo.transaction_in_fraud', 'U') IS NULL CREATE TABLE transaction_in_fraud (id INT PRIMARY KEY, cliente_id INT, valor INT, data DATETIMEOFFSET, intervalo VARCHAR(20));"
    #         cursor.execute(table_check_query)
    #         conn.commit()
    #         # Loop através de cada linha no DataFrame
    #         for index, linha in df.iterrows():
    #             # Inserindo uma linha na tabela
    #             cursor.execute("INSERT INTO transaction_in_fraud ([id], [cliente_id], [valor], [data], [intervalo]) VALUES (?, ?, ?, CONVERT(DATETIMEOFFSET, ?, 127), ?);", linha[0], linha[1], linha[2], linha[3], linha[4])
    #         conn.commit()
    #         print("Tabela transaction_in_fraud criada com sucesso!")

    #     except Exception as e:
    #         print(f"Erro para criar a tabela transaction_in_fraud ou inserir dados:  {e}")

    
    # def transaction_out_fraud(self):
    #     conn, cursor = self.connectToDatabase()
    #     try: 
    #         df = pd.read_csv("./reports/transaction_out_fraud.csv")

    #         # Verifica se a tabela já existe                                                    
    #         table_check_query = "IF OBJECT_ID('dbo.transaction_out_fraud', 'U') IS NULL CREATE TABLE transaction_out_fraud (id INT PRIMARY KEY, cliente_id INT, valor INT, data DATETIMEOFFSET, intervalo VARCHAR(20));"
    #         cursor.execute(table_check_query)
    #         conn.commit()
    #         # Loop através de cada linha no DataFrame
    #         for index, linha in df.iterrows():
    #             # Inserindo uma linha na tabela
    #             cursor.execute("INSERT INTO transaction_out_fraud ([id], [cliente_id], [valor], [data], [intervalo]) VALUES (?, ?, ?, CONVERT(DATETIMEOFFSET, ?, 127), ?);", linha[0], linha[1], linha[2], linha[3], linha[4])
    #         conn.commit()
    #         print("Tabela transaction_out_fraud criada com sucesso!")

    #     except Exception as e:
    #         print(f"Erro para criar a tabela transaction_out_fraud ou inserir dados:  {e}")


    # def transaction_in(self):
    #     conn, cursor = self.connectToDatabase()
    #     try:
    #         df = pd.read_csv("./reports/transaction_in.csv")

    #         # Verifica se a tabela já existe                                                    
    #         table_check_query = "IF OBJECT_ID('dbo.transaction_in', 'U') IS NULL CREATE TABLE transaction_in (id INT PRIMARY KEY, cliente_id INT, valor INT, data DATETIMEOFFSET);"
    #         cursor.execute(table_check_query)
    #         conn.commit()
    #         # Loop através de cada linha no DataFrame
    #         for index, linha in df.iterrows():
    #             # Inserindo uma linha na tabela
    #             cursor.execute("INSERT INTO transaction_in ([id], [cliente_id], [valor], [data]) VALUES (?, ?, ?, CONVERT(DATETIMEOFFSET, ?, 127));", linha[0], linha[1], linha[2], linha[3])
    #         conn.commit()
    #         print("Tabela transaction_in criada com sucesso!")

    #     except Exception as e:
    #         print(f"Erro para criar a tabela transaction_in ou inserir dados: {e}")


    # def transaction_out(self):
    #     conn, cursor = self.connectToDatabase()
    #     try: 
    #         df = pd.read_csv("./reports/transaction_out.csv")

    #         # Verifica se a tabela já existe                                                    
    #         table_check_query = "IF OBJECT_ID('dbo.transaction_out', 'U') IS NULL CREATE TABLE transaction_out (id INT PRIMARY KEY, cliente_id INT, valor INT, data DATETIMEOFFSET);"
    #         cursor.execute(table_check_query)
    #         conn.commit()
    #         # Loop através de cada linha no DataFrame
    #         for index, linha in df.iterrows():
    #             # Inserindo uma linha na tabela
    #             cursor.execute("INSERT INTO transaction_out ([id], [cliente_id], [valor], [data]) VALUES (?, ?, ?, CONVERT(DATETIMEOFFSET, ?, 127));", linha[0], linha[1], linha[2], linha[3])
    #         conn.commit()
    #         print("Tabela transaction_out criada com sucesso!")

    #     except Exception as e:
    #         print(f"Erro para criar a tabela transaction_out ou inserir dados: {e}")
