from readFile import ReadFile
from intercept import Intercept

clients = ReadFile.Clients()
df_transaction_In = ReadFile.TransactionIn()
df_transaction_out = ReadFile.TransactionOut()
# print(df_transaction_In)
# print(df_transaction_out)


fraud_transaction_in = Intercept.Transaction(df_transaction_In)
fraud_transaction_out = Intercept.Transaction(df_transaction_In)
print(fraud_transaction_in)
print(fraud_transaction_out)
fraud_client = Intercept.Client(clients, fraud_transaction_in )
# print(fraud_client)