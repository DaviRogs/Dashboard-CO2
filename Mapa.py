# Importações
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
from pandas import read_csv


app = Dash(__name__)

df = read_csv("annual-co2-emissions-per-country.csv")
df_array = df.values


#filtro dos anos
anos = [] 
for linha in df_array:
    if linha[2] in range(1987,2021):
        if (linha[0] != 'Africa') and (linha[0] != 'Asia') and (linha[0] != 'Europe') and (linha[0] != 'North America') and (linha[0] != 'Oceania') and (linha[0] != 'South America') and (linha[0] != 'World'):
            anos.append(linha[2])

anos = sorted(anos)

#filtro dos países
paises = [] 
for linha in df_array:
    if linha[2] in anos:
        if (linha[0] != 'Africa') and (linha[0] != 'Asia') and (linha[0] != 'Europe') and (linha[0] != 'North America') and (linha[0] != 'Oceania') and (linha[0] != 'South America') and (linha[0] != 'World'):
            paises.append(linha[0])

#filtro dos códigos dos países
codigo = []
for linha in df_array:
    if linha[2] in anos:
        if (linha[0] != 'Africa') and (linha[0] != 'Asia') and (linha[0] != 'Europe') and (linha[0] != 'North America') and (linha[0] != 'Oceania') and (linha[0] != 'South America') and (linha[0] != 'World'):
            codigo.append(linha[1])

#filtro do nível
nivel = []
for linha in df_array:
    if linha[2] in anos:
        if (linha[0] != 'Africa') and (linha[0] != 'Asia') and (linha[0] != 'Europe') and (linha[0] != 'North America') and (linha[0] != 'Oceania') and (linha[0] != 'South America') and (linha[0] != 'World'):
            nivel.append(linha[3])

print(anos)
print(paises)

#Gráfico
fig = px.choropleth(
    locations=codigo, 
    color=nivel,
    hover_name=paises,
    animation_frame=anos,
    range_color=[0,1000000000],
    color_continuous_scale=px.colors.sequential.YlOrRd
)
fig.show()

if __name__ == '__main__':
    app.run_server(debug=True)

'''
Referências:
1. Vídeo em português que eu achei, mas que usa outras bibliotecas: https://www.youtube.com/watch?v=LPvchXRbstA
2. Vídeo que a Lena mandou: https://www.youtube.com/watch?v=hSPmj7mK6ng
3. Vídeo que faz o mapa, mas fiquei confuso nas importações
4. Trabalho do monitor: https://github.com/GustavoHenrique23/TrabalhoAPC/blob/master/app.py
5. Vídeo recomendado pelos monitores: https://www.youtube.com/watch?v=aS64PvDqCbU
6. Documentação dash.plotly: https://dash.plotly.com/layout
7. Documentação do plotly-express com o mapa: https://plotly.com/python/plotly-express/
'''