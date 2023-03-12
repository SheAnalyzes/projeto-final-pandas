import pandas as pd

class Intercept():

    def Transaction(df):
        df['data'] = pd.to_datetime(df['data'])
        df = df.sort_values(["cliente_id", "data"])
        grouped = df.groupby('cliente_id') 
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
        print(fraud_df)
        print("Salvando transaction_fraud no csv...")
        fraud_df.to_csv('./reports/transaction_fraud.csv', index=False)
        return fraud_df

    def Client(clients, fraudes):
        df = pd.merge(clients, fraudes, left_on='id', right_on='cliente_id')
        # Adiciona coluna com número de vezes que o id do cliente aparece em transações fraudulentas
        cliente_id_fraude_counts = df['cliente_id'].value_counts()
        df['cliente_id_fraude_counts'] = df['cliente_id'].map(cliente_id_fraude_counts).fillna(0).astype(int)
        # Agrupa as transações por cliente e soma os valores
        df = df.groupby(['cliente_id','nome', 'email', 'telefone', 'cliente_id_fraude_counts'])['valor'].sum().reset_index()
        print(df)
        print("Salvando clients_fraud no csv...")
        df.to_csv('./reports/clients_fraud.csv', header=False, index=False)
        return df
    