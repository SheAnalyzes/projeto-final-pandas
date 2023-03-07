import pandas as pd

class Intercept():

    def Transaction(df):
        df['data'] = pd.to_datetime(df['data'])
        df = df.sort_values(by='data')
        df['intervalo'] = df['data'].diff().dt.total_seconds()
        print(df)
        fraudes = pd.DataFrame(columns=df.columns)
        for index, row in df.iterrows():
            if row['intervalo'] < 2 and index > 0:
                fraudes = fraudes.append(row, ignore_index=True)
        return fraudes

    def Client(clients, fraudes):
        # fraudes['intervalo'] = fraudes.groupby('cliente_id')['data'].diff().dt.total_seconds()
        df = pd.merge(clients, fraudes, left_on='id', right_on='cliente_id')
        # Adiciona coluna com número de vezes que o id do cliente aparece em transações fraudulentas
        cliente_id_fraude_counts = df['cliente_id'].value_counts()
        df['cliente_id_fraude_counts'] = df['cliente_id'].map(cliente_id_fraude_counts).fillna(0).astype(int)
        # Agrupa as transações por cliente e soma os valores
        df = df.groupby(['cliente_id','nome', 'email', 'telefone', 'cliente_id_fraude_counts'])['valor'].sum().reset_index()        
        return df