# Importações
from pandas import read_csv #Importação do nosso arquivo CSV.
from dash import Dash, html, dcc, Input, Output #Integração com html 
import plotly.express as px #Gráfico
import plotly.graph_objects as go #Mapa

# Definindo um aplicativo (O nosso DashBoard) do Flask
app = Dash(__name__)

# O nosso DataFrame vai ler um aquivo csv para criarmos o nosso gráfico
df = read_csv("annual-co2-emissions-per-country.csv")
#Importando todos os valores do DataFrame para um variável listável (df_array)
df_array = df.values

#Coletando dados dos anos
anos = [] 
for linha in df_array:
    if linha[2] in range(1750,2021):
        if (linha[0] != 'Africa') and (linha[0] != 'Asia') and (linha[0] != 'Europe') and (linha[0] != 'North America') and (linha[0] != 'Oceania') and (linha[0] != 'South America') and (linha[0] != 'World'):
            anos.append(linha[2])
#Colocando anos em ordem crescente
anos = sorted(anos)

#Coletando dados dos países
paises = [] 
for linha in df_array:
    if linha[2] in anos:
        if (linha[0] != 'Africa') and (linha[0] != 'Asia') and (linha[0] != 'Europe') and (linha[0] != 'North America') and (linha[0] != 'Oceania') and (linha[0] != 'South America') and (linha[0] != 'World'):
            paises.append(linha[0])

#Colocando países na mesma ordem que anos
paises_ordenados = []
ano_come = 1750
ano_fim = 2021
while ano_fim != ano_come:
    for linha in df_array: #Para cada linha do df_array, faça:
        if linha[2] == ano_come:
            if (linha[0] != 'Africa') and (linha[0] != 'Asia') and (linha[0] != 'Europe') and (linha[0] != 'North America') and (linha[0] != 'Oceania') and (linha[0] != 'South America') and (linha[0] != 'World'):
                paises_ordenados.append(linha[0])
    ano_come += 1

#Coletando dados dos código
codigo = []
for linha in df_array:
    if linha[2] in anos:
        if (linha[0] != 'Africa') and (linha[0] != 'Asia') and (linha[0] != 'Europe') and (linha[0] != 'North America') and (linha[0] != 'Oceania') and (linha[0] != 'South America') and (linha[0] != 'World'):
            codigo.append(linha[1])

#Colocando codigo na mesma ordem que anos
codigo_ordenado = []
ano_come = 1750
ano_fim = 2021
while ano_fim != ano_come:
    for linha in df_array: #Para cada linha do df_array, faça:
        if linha[2] == ano_come:
            if (linha[0] != 'Africa') and (linha[0] != 'Asia') and (linha[0] != 'Europe') and (linha[0] != 'North America') and (linha[0] != 'Oceania') and (linha[0] != 'South America') and (linha[0] != 'World'):
                codigo_ordenado.append(linha[1])
    ano_come += 1

#Coletando dados do nível
nivel = []
for linha in df_array:
    if linha[2] in anos:
        if (linha[0] != 'Africa') and (linha[0] != 'Asia') and (linha[0] != 'Europe') and (linha[0] != 'North America') and (linha[0] != 'Oceania') and (linha[0] != 'South America') and (linha[0] != 'World'):
            nivel.append(linha[3])

#Colocando nível na mesma ordem que anos
nivel_ordenado = []
ano_come = 1750
ano_fim = 2021
while ano_fim != ano_come:
    for linha in df_array: #Para cada linha do df_array, faça:
        if linha[2] == ano_come:
            if (linha[0] != 'Africa') and (linha[0] != 'Asia') and (linha[0] != 'Europe') and (linha[0] != 'North America') and (linha[0] != 'Oceania') and (linha[0] != 'South America') and (linha[0] != 'World'):
                nivel_ordenado.append(linha[3])
    ano_come += 1

#Gráfico
fig = px.choropleth(
    locations=codigo_ordenado, #Posição do país no mapa
    color=nivel_ordenado, #Nível de CO2
    hover_name=paises_ordenados, #Nome do país ao deixar o mouse encima
    animation_frame=anos, #Régua
    range_color=[0,2000000000], #Intervalo de CO2
    color_continuous_scale=px.colors.sequential.Reds #Variação de cor
)
fig.show()

if __name__ == '__main__':
    app.run_server(debug=True)

'''
Referências:
1. Vídeo em português que eu achei, mas que usa outras bibliotecas: https://www.youtube.com/watch?v=LPvchXRbstA
2. Vídeo que a Lena mandou: https://www.youtube.com/watch?v=hSPmj7mK6ng
3. Vídeo que faz o mapa, mas fiquei confuso nas importações: por algum motivo eu perdi o link
4. Trabalho do monitor: https://github.com/GustavoHenrique23/TrabalhoAPC/blob/master/app.py
5. Vídeo recomendado pelos monitores: https://www.youtube.com/watch?v=aS64PvDqCbU
6. Documentação dash.plotly: https://dash.plotly.com/layout
7. Documentação do plotly-express com o mapa: https://plotly.com/python/plotly-express/
8. Davi: Valeu de verdade
9. Gustavera: tamo junto
'''
