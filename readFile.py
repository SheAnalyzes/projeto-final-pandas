# Lendo um arquivo csv
import pandas as pd
import glob
import os
  
class ReadFile(): 

    def Clients():
        diretorio = 'arquivos_carga_csv'  # caminho para o diretório onde estão os arquivos CSV
        all_files = glob.glob(os.path.join(diretorio, "clients*.csv"))
        # ler o primeiro arquivo CSV com cabeçalho
        df = pd.read_csv(all_files[0], names=["id", "nome", "email", "data_cadastro", "telefone"], delimiter=';', header=0)
        # iterar sobre os arquivos restantes e concatená-los ao dataframe
        for f in all_files[1:]:
            temp_df = pd.read_csv(f, names=["id", "nome", "email", "data_cadastro", "telefone"], delimiter=';', header=None)
            df = pd.concat([df, temp_df])
        
        # salvar o dataframe combinado em um arquivo CSV
        df.to_csv('./reports/clients.csv', index=False)
        return df


    def TransactionIn():
        diretorio = './arquivos_carga_csv'  # caminho para o diretório onde estão os arquivos CSV
        all_files = glob.glob(os.path.join(diretorio, "transaction-in*.csv"))
        # ler o primeiro arquivo CSV com cabeçalho
        df = pd.read_csv(all_files[0], names=["id", "cliente_id", "valor", "data"], delimiter=';', header=0)
        # iterar sobre os arquivos restantes e concatená-los ao dataframe
        print(df)
        for f in all_files[1:]:
            temp_df = pd.read_csv(f, names=["id", "cliente_id", "valor", "data"], delimiter=';', header=None)
            df = pd.concat([df, temp_df])
        
        # salvar o dataframe combinado em um arquivo CSV
        df.to_csv('./reports/transaction_in.csv', index=False)
        return df
     

    def TransactionOut():
        diretorio = 'arquivos_carga_csv'  # caminho para o diretório onde estão os arquivos CSV
        all_files = glob.glob(os.path.join(diretorio, "transaction-out*.csv"))
        # ler o primeiro arquivo CSV com cabeçalho
        df = pd.read_csv(all_files[0], names=["id", "cliente_id", "valor", "data"], delimiter=';', header=0)
        # iterar sobre os arquivos restantes e concatená-los ao dataframe
        for f in all_files[1:]:
            temp_df = pd.read_csv(f, names=["id", "cliente_id", "valor", "data"], delimiter=';', header=None)
            df = pd.concat([df, temp_df])
        
        # salvar o dataframe combinado em um arquivo CSV
        df.to_csv('./reports/transaction_out.csv', index=False)
        return df