from readFile import ReadFile
from intercept import Intercept
from connectionDB import ConnectionDB

while True:
    print("Digite a opção na ordem do passo a passo")
    print("1 - Lendo os arquivos csv")
    print("2 - Interceptar operações fraudulentas com python")
    print("3 - Gerar arquivos csv")
    print("4 - Salvar dados no Banco SQL")
    print("5 - Gerar relatórios em SQL")
    print("6 - Sair")
    print("-"*50)
    print("Digite o número da opção:")
    option = int(input())

    if option == 1:
        print("-"*100)
        print("Dataframe de clientes")
        clients_df = ReadFile.Clients()
        print("-"*100)
        print(clients_df)
        print("Transações de Entrada")
        transaction_in_df = ReadFile.TransactionIn()
        print("-"*100)
        print(transaction_in_df)
        print("Transações de Saida")
        transaction_out_df = ReadFile.TransactionOut()
        print("-"*100)
        print(transaction_out_df)

    if option == 2:
        print("-"*100)
        print("Interceptando transações de entrada fraudulentas")
        transaction_in_fraud = Intercept.Transaction(transaction_in_df)
        print(transaction_in_fraud)
        print("-"*100)
        print("Interceptando transações de saída fraudulentas")
        transaction_out_fraud = Intercept.Transaction(transaction_out_df)
        print(transaction_out_fraud)
        print("-"*100)
        print("Encontrando os clientes envolvidos")
        clients_fraud = Intercept.Client(clients_df, transaction_in_fraud, transaction_out_fraud )
        print(clients_fraud)
        print("-"*100)

    if option == 3:
        print("-"*100)
        print("Criando csv dos arquivos de carga ")
        clients_df.to_csv('./reports/clients.csv', index=False)
        transaction_in_df.to_csv('./reports/transaction_in.csv', index=False)
        transaction_out_df.to_csv('./reports/transaction_out.csv', index=False)
        print("-"*100)
        print("Criando csv dos arquivos encontrados")
        clients_fraud.to_csv('./reports/clients_fraud.csv', index=False)
        transaction_in_fraud.to_csv('./reports/transaction_in_fraud.csv', index=False)
        transaction_out_fraud.to_csv('./reports/transaction_out_fraud.csv', index=False)
        print("-"*100)

    if option == 4:
        print("-"*100)
        print("Aguarde... Salvando operações no Banco. ")
        conexao = ConnectionDB()
        conexao.clientFraud()
        conexao.transaction_in_fraud()
        conexao.transaction_out_fraud()
        conexao.closeConnection()
        print("-"*100)

    if option == 6:
        exit()