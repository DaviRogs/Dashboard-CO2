# Importação das bibliotecas que utilizaremos:

from dash import Dash, html, dcc, Input, Output #importante para a criação do site e alguma coisa dos gráficos;
import plotly.express as px #Para funcionalidades do Plotly, assim criando nosso gráfico;
from pandas import read_csv #Para Leituras de bases de Dados, como excel, CSV, etc...

# Definindo um aplicativo (O nosso DashBoard) do Flask

DashBoard = Dash(__name__)


# O nosso DataFrame vai ler uma aquivo csv para criarmos o nosso gráfico

df = read_csv("annual-co2-emissions-per-country.csv")

'''
Estamos importando as bibliotecas essenciais para o funcionamento dos nossos gráficos e o site a ser
executado.

Além disso, já colocamos nosso código para ler o arquivo CSV o qual apresenta todos os dados necessários
para realizarmos os gráficos.
'''

#----------------------------------------------------------------------------------------------------------

# 1º Gráfico

#Cria uma variável "list" com base nos valores do nosso DataFrame

df_array = df.values

World = [] #List vazia 'World'.

#Filtrando somente os dados da linha "World" no arquivo SCV
for linha in df_array: #Para cada linha do df_array, faça:
    if linha[0] == "World":
        World.append(linha[3])

# print(World):

#Criando uma lista com anos de 1750 até 2020.
anos = list(range(1750,2021))

# print(anos)

# FifLinha será nossa variável o qual mostrará gráfico de linhas
FigLinha = px.line(x=anos, y=World)

# FigLinha.show()

#----------------------------------------------------------------------------------------------------------

# 2º Gráfico

