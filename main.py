from readFile import ReadFile
from intercept import Intercept
from connectionDB import ConnectionDB

while True:
    print("Siga o passo a passo:")
    print("1 - Trantando arquivos csv")
    print("2 - Interceptar operações fraudulentas")
    print("3 - Gerar relatórios")
    print("4 - Salvar dados no Banco SQL")
    print("5 - Sair")
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
        clients_df.to_csv('./reports/clients.csv', header=False, index=False)
        transaction_in_df.to_csv('./reports/transaction_in.csv', header=False, index=False)
        transaction_out_df.to_csv('./reports/transaction_out.csv', header=False, index=False)
        print("-"*100)
        print("Criando csv dos arquivos encontrados")
        clients_fraud.to_csv('./reports/clients_fraud.csv', header=False, index=False)
        transaction_in_fraud.to_csv('./reports/transaction_in_fraud.csv', header=False, index=False)
        transaction_out_fraud.to_csv('./reports/transaction_out_fraud.csv', header=False, index=False)
        print("-"*100)
    if option == 4:
        print("-"*100)
        ConnectionDB.clientFraud()

    if option == 5:
        exit()