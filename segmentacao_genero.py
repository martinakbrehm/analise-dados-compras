import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_json('dados_compras.json') #ler onde arquivo está
df.head() #ler linhas do arquivo

informacoes_compradores = df.loc[:, ["Sexo", "Login", "Idade"]]
informacoes_compradores.head()

informacoes_compradores = informacoes_compradores.drop_duplicates()
contagem_compradores = informacoes_compradores.count()[0]



total_gasto_por_genero = df.groupby(["Sexo"]).sum()["Valor"].rename("Valor Total Gasto em Compras")

print(total_gasto_por_genero)
legenda_total_por_genero = ["Feminino", "Masculino", "Outro / Não Divulgado"]
fig = plt.figure(figsize =(7, 7))
plt.subplot(1, 2, 1)
plt.pie(total_gasto_por_genero, labels = total_gasto_por_genero)
plt.legend(legenda_total_por_genero)
plt.title("Valores gastos por genero")


contagem_genero = informacoes_compradores["Sexo"].value_counts()
porcentagem_genero = (contagem_genero / contagem_compradores) * 100

porcentagem_genero = round(porcentagem_genero, 2)

informacoes_compradores = pd.DataFrame({"Número de compradores" : contagem_genero, "%" : porcentagem_genero})

plt.subplot(1, 2, 2)
print(informacoes_compradores)


legenda_porcentagem_genero = ["Masculino", "Feminino", "Outro / Não Divulgado"]
plt.pie(porcentagem_genero, labels = porcentagem_genero)
plt.legend(legenda_porcentagem_genero)
plt.title("Porcentagem de compradores por genero (%)")
plt.show()





