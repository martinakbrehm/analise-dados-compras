import pandas as pd


df = pd.read_json('dados_compras.json') #ler onde arquivo está
df.head() #ler linhas do arquivo
df.to_csv('compras.csv', index=False) #

print("Presença de valores faltantes:")
print(df.isnull().any()) #verificar valores faltantes

total_itens_comprados = df["Item ID"].count()
print("Total de itens comprados: ")
print(total_itens_comprados)
total_compras = df["Login"].nunique() #entendi que uma compra compreende vários itens, e é realizada pelo mesmo usuário uma unica vez
print("Total de compras realizadas:")
print(total_compras)
