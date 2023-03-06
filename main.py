# Lendo um arquivo csv
import pandas as pd
import os
  
# df = pd.read_csv('arquivos_carga_csv/clients-001.csv', header=None)
# print(df)

diretorio = 'arquivos_carga_csv'  # caminho para o diretório onde estão os arquivos CSV
lista_de_dfs_clientes = []

for arquivo in os.listdir(diretorio):
    if arquivo.startswith('clients-') and arquivo.endswith('.csv'):  # verifica se o arquivo é um CSV e tem o prefixo correto
        caminho = os.path.join(diretorio, arquivo)  # constrói o caminho completo para o arquivo
        df = pd.read_csv(caminho, names=["id", "nome", "email", "data_cadastro", "telefone"], delimiter=';', header=None)
        if df.loc()[0]['nome'] == 'nome' and df.loc()[0]['email'] == 'email' :
            print(df.loc()[0]['nome'])
            continue
        else:
            lista_de_dfs_clientes.append(df)  # adiciona o DataFrame à lista

try:
    df_final = pd.concat(lista_de_dfs_clientes, ignore_index=True)  # combina todos os DataFrames em um único DataFrame
    print(df_final)
except ValueError:
    print('Nenhum arquivo CSV encontrado ou todos os arquivos estão vazios')