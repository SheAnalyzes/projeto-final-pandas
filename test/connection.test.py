import pyodbc

class Database:
    def __init__(self, server, port, database, username, password):
        self.server = server
        self.port = port
        self.database = database
        self.username = username
        self.password = password
        self.conn = None
        self.cursor = None

    def connectToDatabase(self):
        try:
            conn_string = f"Driver={{ODBC Driver 18 for SQL Server}};Server=tcp:{self.server},{self.port};Database={self.database};Uid={self.username};Pwd={self.password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"
            self.conn = pyodbc.connect(conn_string)
            self.cursor = self.conn.cursor()
            return self.conn, self.cursor 
        except Exception as e:
            print(f"Erro de conexão com banco: {e}")

    def testConnection(self):
        try:
            self.connectToDatabase()
            print("Conexão com o banco de dados estabelecida com sucesso.")
            self.closeConnection()
        except Exception as e:
            print(f"Não foi possível estabelecer conexão com o banco de dados: {e}")

    def closeConnection(self):
        self.conn.close()

db = Database('localhost', '1433', 'mydatabase', 'myusername', 'mypassword')
db.testConnection()
