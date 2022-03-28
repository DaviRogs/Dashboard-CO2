# Importações
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
from pandas import read_csv


# ======================================================================================================
# Backend
app = Dash(__name__) #Código padrão do Dash

df = read_csv("annual-co2-emissions-per-country.csv") #Utilização do pandas para ler o csv
df_array = df.values

anos = []
for linha in df_array:
    if linha[2] in range (1987,2021):
        try:
            anos.append(int(linha[2]))
        except:
            continue

total_ano = 0 # Conta a quantidade de países
anos_filtro = [] # Criar array em que cada item vai ser quantos jogos foram lançados em cada ano
todos = [] # Todos é uma array para guardar todos os anos analisados

for i in range(1987, 2021):
    total_ano = anos.count(i)
    anos_filtro.append(total_ano)
    todos.append(i)

print(todos)

    # Gráfico
fig = px.choropleth(
    data_frame=df, 
    locations="Code", 
    color="Annual CO2 emissions", 
    hover_name="Entity",
    animation_frame=sorted(df["Year"]),
    range_color=[0,1000000000],
    color_continuous_scale=px.colors.sequential.YlOrRd
)
fig.show()

# ======================================================================================================
# Frontend



# ======================================================================================================
#

if __name__ == '__main__': # Código padrão do Dash
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