import pandas as pd
from shared.utilities import print_dataframe, read_csv_file


class Intercept():

    def transactions_fraud():
        df = read_csv_file("./reports/transactions.csv")

        df['data'] = pd.to_datetime(df['data'])
        # ordenado por cliente_id e por data
        df = df.sort_values(["cliente_id", "data"])
        # agrupando por id dos clientes
        grouped = df.groupby('cliente_id') 
        # gerando um dataframe das fraudes com as colunas das transações
        fraud_df = pd.DataFrame(columns=df.columns)
        intervalos = []
        for _, group in grouped:
            # Ordenando as transações pelo horário
            group = group.sort_values(by='data')
            # Calculando o intervalo de tempo entre as transações
            time_diff = group['data'].diff().fillna(pd.Timedelta(minutes=2))
            # Adicionando os intervalos de tempo ao dataframe de transações
            group['intervalo'] = time_diff
            intervalos.append(group)
            # Verificando se há algum intervalo menor que 2 segundos
            is_fraud = time_diff < pd.Timedelta(minutes=2)
            # Adicionando as transações fraudulentas ao dataframe de fraudes
            frauds = group[is_fraud]
            fraud_df = pd.concat([fraud_df, frauds])     
        print_dataframe(fraud_df, "transaction_fraud")    
    

    def client_fraud():
        clients = read_csv_file("./reports/clients.csv")
        transaction_fraud = read_csv_file("./reports/transaction_fraud.csv")

        df = pd.merge(clients, transaction_fraud, left_on='id', right_on='cliente_id')
        # Adiciona coluna com número de vezes que o id do cliente aparece em transações fraudulentas
        cliente_id_fraude_counts = df['cliente_id'].value_counts()
        df['cliente_id_fraude_counts'] = df['cliente_id'].map(cliente_id_fraude_counts).fillna(0).astype(int)
        # Agrupa as transações por cliente e soma os valores
        df = df.groupby(['cliente_id','nome', 'email', 'telefone', 'cliente_id_fraude_counts'])['valor'].sum().reset_index()
        print_dataframe(df, "clients_fraud")    


    # tabela transações com formato solicitado para armazenamento no Banco de dados
    def transactions_db():
        df = read_csv_file("./reports/transactions.csv")
        # Convertendo a coluna 'data' para o tipo datetime
        df['data'] = pd.to_datetime(df['data'])
        # Ordenando as transações por cliente e por data
        df = df.sort_values(["cliente_id", "data"])
        # Adicionando a coluna "tipo"
        df['tipo'] = df['valor'].apply(lambda x: 'entrada' if x > 0 else 'saida')
         # Criando uma coluna para armazenar a informação de fraude
        df['fraude'] = 0
        # agrupando por id dos clientes
        grouped = df.groupby('cliente_id') 
        # Verificando as transações de cada cliente em busca de fraudes
        for _, group in grouped:
            # Ordenando as transações pelo horário
            group = group.sort_values(by='data')
            # Calculando o intervalo de tempo entre as transações
            time_diff = group['data'].diff().fillna(pd.Timedelta(minutes=2))
            # Verificando se há algum intervalo menor que 2 minutos
            is_fraud = time_diff < pd.Timedelta(minutes=2)
            # Marcando as transações fraudulentas na coluna 'fraude'
            df.loc[group.index[is_fraud], 'fraude'] = 1
        print_dataframe(df, "transactions_db")