import pandas as pd
import pyodbc
import os
from dotenv import load_dotenv
from shared.utilities import read_csv_file

class ConnectionDB:

    def __init__(self):
        self.conn = None
        self.cursor = None
        load_dotenv()  # carrega as variáveis do arquivo .env

        self.server = os.getenv('DB_SERVER')
        self.database = os.getenv('DB_NAME')
        self.username = os.getenv('DB_USERNAME')
        self.password = os.getenv('DB_PASSWORD')
        self.port = os.getenv('DB_PORT')
    
    def connectToDatabase(self):
        try:
            
            conn_string = f"Driver={{ODBC Driver 18 for SQL Server}};Server=tcp:{self.server},{self.port};Database={self.database};Uid={self.username};Pwd={self.password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"
            
            self.conn = pyodbc.connect(conn_string)
            self.cursor = self.conn.cursor()
            return self.conn, self.cursor 
               
        except Exception as e:
            print(f"Erro de conexão com banco: {e}")
    

    def closeConnection(self):
        self.cursor.close()
        self.conn.close()


    def create_clients_table(self):
        conn, cursor = self.connectToDatabase()
        try:
            # Verifica se a tabela já existe
            table_check_query = "IF OBJECT_ID('dbo.clientes', 'U') IS NULL CREATE TABLE clientes (id INT PRIMARY KEY, nome VARCHAR(100), email VARCHAR(200), data_cadastro DATETIMEOFFSET, telefone VARCHAR(20));"
            cursor.execute(table_check_query)
            conn.commit()

            print("Tabela clientes criada com sucesso!")
        except Exception as e:
            print(f"Erro para criar a tabela clientes: {e}")
        finally:
            self.closeConnection()


    def insert_clients_data(self):
        conn, cursor = self.connectToDatabase()
        try:
            df = read_csv_file('./reports/clients.csv')

            # Loop através de cada linha no DataFrame
            for index, linha in df.iterrows():
                # Verifica se o registro já existe
                check_query = "SELECT COUNT(*) FROM clientes WHERE id = ?;"
                cursor.execute(check_query, linha[0])
                result = cursor.fetchone()[0]
                if result == 0:  # Se não existe, insere na tabela
                    # Inserindo uma linha na tabela
                    cursor.execute("INSERT INTO clientes ([id], [nome], [email], [data_cadastro], [telefone]) VALUES (?, ?, ?, CONVERT(DATETIMEOFFSET, ?, 127), ?);", linha[0], linha[1], linha[2], linha[3], linha[4])
                    conn.commit()
                    print(f"Registro com id={linha[0]} inserido com sucesso.")
                else:
                    print(f"Registro com id={linha[0]} já existe na tabela clientes. Não foi inserido novamente.")

        except Exception as e:
            print(f"Erro para inserir dados na tabela clientes: {e}")
        finally:
            self.closeConnection()


    def create_transactions_table(self):
        conn, cursor = self.connectToDatabase()
        try:
            # Verifica se a tabela já existe
            table_check_query = "IF OBJECT_ID('dbo.transacoes_db', 'U') IS NULL CREATE TABLE transacoes_db (id INT PRIMARY KEY, cliente_id INT, valor FLOAT, data DATETIMEOFFSET, tipo VARCHAR(45), fraude INT);"
            cursor.execute(table_check_query)
            conn.commit()

            print("Tabela transacoes_db criada com sucesso!")
        except Exception as e:
            print(f"Erro para criar a tabela transacoes_db: {e}")
        finally:
            self.closeConnection()


    def insert_transactions_data(self):
        conn, cursor = self.connectToDatabase()
        try: 
            df = read_csv_file("./reports/transactions_db.csv")

            # Loop através de cada linha no DataFrame
            for index, linha in df.iterrows():
                # Verifica se o registro já existe
                check_query = "SELECT COUNT(*) FROM transacoes_db WHERE id = ?;"
                cursor.execute(check_query, linha[0])
                result = cursor.fetchone()[0]
                if result == 0:  # Se não existe, insere na tabela
                    # Inserindo uma linha na tabela
                    cursor.execute("INSERT INTO transacoes_db ([id], [cliente_id], [valor], [data], [tipo], [fraude]) VALUES (?, ?, ?, CONVERT(DATETIMEOFFSET, ?, 127), ?, ?);", linha[0], linha[1], linha[2], linha[3], linha[4], linha[5])
                    conn.commit()
                    print(f"Registro com id={linha[0]} inserido com sucesso.")
                else:
                    print(f"Registro com id={linha[0]} já existe na tabela transacoes_db. Não foi inserido novamente.")
        except Exception as e:
            print(f"Erro para inserir dados na tabela transacoes_db: {e}")
        finally:
            self.closeConnection()