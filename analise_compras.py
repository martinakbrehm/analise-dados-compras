import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_json('dados_compras.json') #ler onde arquivo está
df.head() #ler linhas do arquivo

#analise de dados

usuario_valor_total = df.groupby(["Login"]).sum()["Valor"].rename("Valor Total de Compra")
usuario_valor_minimo = df.groupby(["Login"]).min()["Valor"].rename("Valor Minimo de Compra")
usuario_valor_maximo = df.groupby(["Login"]).max()["Valor"].rename("Valor Maximo de Compra")
usuario_quantidade_itens = df.groupby(["Login"]).count()["Item ID"].rename("Quantidade de itens")

dados_usuario_compra = pd.DataFrame({"Valor Total de Compra": usuario_valor_total, "Valor Minimo de Compra": usuario_valor_minimo, "Valor Maximo de Compra": usuario_valor_maximo, "Valor Medio de Compra": usuario_valor_total/usuario_quantidade_itens, "Quantidade de Itens": usuario_quantidade_itens})

#print(dados_usuario_compra)

media_gasta_por_compra = dados_usuario_compra["Valor Total de Compra"].mean()
min_gasto_por_compra = dados_usuario_compra["Valor Minimo de Compra"].min()
max_gasto_por_compra = dados_usuario_compra["Valor Maximo de Compra"].max()
analise_compras = pd.DataFrame({"Média gasta por compra": media_gasta_por_compra, "Minimo gasto por compra": min_gasto_por_compra, "Máximo gasto por compra": max_gasto_por_compra}, index=[0])

valor_produto_mais_caro = df["Valor"].max()
valor_produto_mais_barato = df["Valor"].min()
produto_mais_caro = df.loc[(df['Valor']==valor_produto_mais_caro), ['Item ID','Nome do Item','Valor']].drop_duplicates()
produto_mais_barato = df.loc[(df['Valor']==valor_produto_mais_barato), ['Item ID','Nome do Item','Valor']].drop_duplicates()

print(analise_compras)
print(produto_mais_caro)
print(produto_mais_barato)

#visualização de dados

fig = plt.figure(figsize =(15, 5))

plt.subplot(1, 3, 1)
plt.title('Valores das compras por usuário')
plt.xlabel('Valor')
plt.ylabel('Frequência absoluta')
plt.hist(dados_usuario_compra["Valor Total de Compra"], 8, rwidth=0.9, color='pink')


plt.subplot(1, 3, 2)
plt.title('Quantidade de itens comprados por usuário')
plt.xlabel('Quantidade')
plt.ylabel('Frequência absoluta')
plt.hist(dados_usuario_compra["Quantidade de Itens"], bins = 4, rwidth=0.9, color='orange')

plt.subplot(1, 3, 3)
plt.title('Valores dos itens')
plt.xlabel('Valores')
plt.ylabel('Frequência absoluta')
plt.hist(df["Valor"], bins = 30, rwidth=0.9, color='violet')

plt.show()

