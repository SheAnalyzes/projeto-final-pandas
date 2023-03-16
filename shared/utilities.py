import pandas as pd


def print_dataframe(df, table_name):
    print(df)
    print("Salvando " + table_name +" no csv.")
    df.to_csv('./reports/'+ table_name +'.csv', index=False)


def read_csv_file(csv_path):
    try:
        df = pd.read_csv(csv_path)
        print(f'O arquivo {csv_path} foi aberto com sucesso.')
        return df
    except FileNotFoundError:
        print(f'O arquivo {csv_path} não foi encontrado.')
    except:
        print(f'Erro ao abrir o arquivo {csv_path}.')