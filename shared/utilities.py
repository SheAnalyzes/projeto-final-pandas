
def print_dataframe(df, table_name):
    print(df)
    print("Salvando " + table_name +" no csv.")
    df.to_csv('./reports/'+ table_name +'.csv', index=False)