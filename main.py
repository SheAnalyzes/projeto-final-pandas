from readFile import ReadFile
from intercept import Intercept
from connectionDB import ConnectionDB

while True:
    print("Digite a opção na ordem do passo a passo")
    print("1 - Juntando os arquivos csv")
    print("2 - Interceptar operações fraudulentas com python")
    print("3 - Salvar todos os dados no Banco")
    print("4 - Sair")
    print("-"*50)
    print("Digite o número da opção:")
    option = int(input())

    if option == 1:
        print("-"*100)
        print("Dataframe de clientes")
        clients_df = ReadFile.Clients()
        print("-"*100)
        print("Dataframe de todas as transações realizadas")
        transaction_df = ReadFile.Transaction()
        print("-"*100)

    if option == 2:
        print("-"*100)
        print("Interceptando todas as transações fraudulentas")
        Intercept.Transaction(transaction_df)
        print("-"*100)
        print("Encontrando os clientes envolvidos")
        Intercept.Client(clients_df, transaction_df)
        print("-"*100)

    if option == 3:
        print("-"*100)
        print("Aguarde... Conectando com o banco de dados. ")
        conexao = ConnectionDB()
        print("Salvando dados dos clientes...")
        conexao.clients()
        print("Salvando dados dos clientes fraudulentos...")
        conexao.clients_fraud()
        print("Salvando todas as transações")
        conexao.transactions()
        print("Salvando as transações com fraude...")
        conexao.transaction_fraud()
        print("Fechando conexão.")
        conexao.closeConnection()
        print("-"*100)

    if option == 4:
        exit()