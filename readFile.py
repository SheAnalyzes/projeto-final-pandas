# Lendo um arquivo csv
import pandas as pd
import glob
import os
from shared.utilities import print_dataframe

class ReadFile(): 

    def clients():
        diretorio = './arquivos_carga_csv'
        all_files = glob.glob(os.path.join(diretorio, "clients*.csv"))
        # ler o primeiro arquivo CSV com cabeçalho
        df = pd.read_csv(all_files[0], names=["id", "nome", "email", "data_cadastro", "telefone"], delimiter=';', header=0)
        # iterar sobre os arquivos restantes e concatená-los ao dataframe
        for f in all_files[1:]:
            temp_df = pd.read_csv(f, names=["id", "nome", "email", "data_cadastro", "telefone"], delimiter=';', header=None)
            df = pd.concat([df, temp_df])

        df['data_cadastro'] = pd.to_datetime(df['data_cadastro'])
        print_dataframe(df, 'clients' )


    def transactions():
        diretorio = './arquivos_carga_csv'

        ## Lendo as transações de entrada
        all_files_in = glob.glob(os.path.join(diretorio, "transaction-in*.csv"))
        # ler o primeiro arquivo CSV com cabeçalho
        df_in = pd.read_csv(all_files_in[0], names=["id", "cliente_id", "valor", "data"], delimiter=';', header=0)
        # iterar sobre os arquivos restantes e concatená-los ao dataframe
        for f in all_files_in[1:]:
            temp_df_in = pd.read_csv(f, names=["id", "cliente_id", "valor", "data"], delimiter=';', header=None)
            df_in = pd.concat([df_in, temp_df_in])

        ## Lendo as transações de saida
        all_files_out = glob.glob(os.path.join(diretorio, "transaction-out*.csv"))
        # ler o primeiro arquivo CSV com cabeçalho
        df_out = pd.read_csv(all_files_out[0], names=["id", "cliente_id", "valor", "data"], delimiter=';', header=0)
        # iterar sobre os arquivos restantes e concatená-los ao dataframe
        for f in all_files_out[1:]:
            temp_df_out = pd.read_csv(f, names=["id", "cliente_id", "valor", "data"], delimiter=';', header=None)
            df_out = pd.concat([df_out, temp_df_out])
        
        df = pd.concat([df_in, df_out])
        print_dataframe(df, 'transactions' )
    

    def transaction_in():
        diretorio = './arquivos_carga_csv'

        all_files = glob.glob(os.path.join(diretorio, "transaction-in*.csv"))
        # ler o primeiro arquivo CSV com cabeçalho
        df = pd.read_csv(all_files[0], names=["id", "cliente_id", "valor", "data"], delimiter=';', header=0)
        # iterar sobre os arquivos restantes e concatená-los ao dataframe
        for f in all_files[1:]:
            temp_df = pd.read_csv(f, names=["id", "cliente_id", "valor", "data"], delimiter=';', header=None)
            df = pd.concat([df, temp_df])
        
        df['data'] = pd.to_datetime(df['data'])
        print_dataframe(df, "transaction_in")


    def transaction_out():
        diretorio = './arquivos_carga_csv'

        all_files = glob.glob(os.path.join(diretorio, "transaction-out*.csv"))
        # ler o primeiro arquivo CSV com cabeçalho
        df = pd.read_csv(all_files[0], names=["id", "cliente_id", "valor", "data"], delimiter=';', header=0)
        # iterar sobre os arquivos restantes e concatená-los ao dataframe
        for f in all_files[1:]:
            temp_df = pd.read_csv(f, names=["id", "cliente_id", "valor", "data"], delimiter=';', header=None)
            df = pd.concat([df, temp_df])
        
        df['data'] = pd.to_datetime(df['data'])
        print_dataframe(df, "transaction_out")




