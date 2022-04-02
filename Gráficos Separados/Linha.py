from pandas import read_csv #Importação do nosso arquivo CSV.
from dash import Dash, html, dcc
from dash.dependencies import Input, Output #Para usarmos no callback
import plotly.express as px

# Definindo um aplicativo (O nosso DashBoard) do Flask

DashBoard = Dash(__name__)

# O nosso DataFrame vai ler um aquivo csv para criarmos o nosso gráfico

df = read_csv("annual-co2-emissions-per-country.csv")

#===================================================================================================================
#Filtrando os dados CSV

#Cria uma variável "list" com base nos valores do nosso DataFrame

df_array = df.values

World = [] #List vazia

#Filtrando nossos dados
for linha in df_array: #Para cada linha do df_array, faça:
    if linha[0] == "World":
        World.append(linha[3])

# print(World):
anos = list(range(1750,2021))

# print(anos)

fig = px.line(
    x=anos,
    y=World
    )

fig.show()


# if __name__ == '__main__':
#      DashBoard.run_server(debug=True)