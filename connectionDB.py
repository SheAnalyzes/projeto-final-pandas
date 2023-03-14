import pandas as pd
import pyodbc

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


    def clients(self):
        conn, cursor = self.connectToDatabase()
        try:
            df = pd.read_csv("./reports/clients.csv")
           
            # Verifica se a tabela já existe        
            table_check_query = "IF OBJECT_ID('dbo.clientes', 'U') IS NULL CREATE TABLE clientes (id INT PRIMARY KEY, nome VARCHAR(100), email VARCHAR(200), data_cadastro DATETIMEOFFSET, telefone VARCHAR(20));"
            cursor.execute(table_check_query)
            conn.commit()

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
            
            print("Tabela clientes criada com sucesso!")

        except Exception as e:
            print(f"Erro para criar a tabela clientes ou inserir dados: {e}")
            
        finally:
            self.closeConnection()


    def transactions(self):
        conn, cursor = self.connectToDatabase()
        try: 
            df = pd.read_csv("./reports/transactions_db.csv")

            # Verifica se a tabela já existe                                                    
            table_check_query = "IF OBJECT_ID('dbo.transacoes', 'U') IS NULL CREATE TABLE transacoes (id INT PRIMARY KEY, cliente_id INT, valor INT, data DATETIMEOFFSET, tipo VARCHAR(45), fraude INT);"
            cursor.execute(table_check_query)
            conn.commit()
            # Loop através de cada linha no DataFrame
            for index, linha in df.iterrows():
                # Verifica se o registro já existe
                check_query = "SELECT COUNT(*) FROM transacoes WHERE id = ?;"
                cursor.execute(check_query, linha[0])
                result = cursor.fetchone()[0]
                if result == 0:  # Se não existe, insere na tabela
                # Inserindo uma linha na tabela
                    cursor.execute("INSERT INTO transacoes ([id], [cliente_id], [valor], [data], [tipo], [fraude]) VALUES (?, ?, ?, CONVERT(DATETIMEOFFSET, ?, 127), ?, ?);", linha[0], linha[1], linha[2], linha[3], linha[4], linha[5])
                    conn.commit()
                    print(f"Registro com id={linha[0]} inserido com sucesso.")
                else:
                    print(f"Registro com id={linha[0]} já existe na tabela transacoes. Não foi inserido novamente.")

            print("Tabela transacoes criada com sucesso!")

        except Exception as e:
            print(f"Erro para criar a tabela transacoes ou inserir dados: {e}")

        finally:
            self.closeConnection()
