#Importação das bibliotecas

from pandas import read_csv
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

app = Dash(__name__, title='Emissão de CO2')

df = read_csv("annual-co2-emissions-per-country.csv")

df_array = df.values #Tranformando tudo o que estiver no df em uma lista para parar de usar a extensão Pandas no código.

#---------------------------------------------------------------------------------------------------------
#Grafico1

world = []

# Colocando os dados do mundo na lista vazia
for linha in df_array:
    if linha[0] == "World":
        world.append(linha[3])

anos = list(range(1750,2021))

fig1 = px.line(
    x=anos,
    y=world
)

fig1.update_layout(
    title="Emissão no mundo ao longo do tempo",
    xaxis_title="Anos",
    yaxis_title="Emissão",
    )

#---------------------------------------------------------------------------------------------------------
#Grafico2

# Acrescentando os dados para por no gráfico de mapa
anos = []
paises_ordenados = []
nivel_ordenado = []
codigo_ordenado = []
ano_come = 1750
ano_fim = 2021
while ano_fim != ano_come:
    for linha in df_array:
        if linha[2] == ano_come:
            if (linha[0] != 'Africa') and (linha[0] != 'Asia') and (linha[0] != 'Europe') and (linha[0] != 'North America') and (linha[0] != 'Oceania') and (linha[0] != 'South America') and (linha[0] != 'World'):
                paises_ordenados.append(linha[0])
                codigo_ordenado.append(linha[1])
                anos.append(linha[2])
                nivel_ordenado.append(linha[3])
    ano_come += 1


fig2 = px.choropleth(
    locations=codigo_ordenado, #Posição do país no mapa
    color=nivel_ordenado, #Nível de CO2
    hover_name=paises_ordenados, #Nome do país ao deixar o mouse encima
    animation_frame=anos, #Régua
    range_color=[0,2000000000], #Intervalo de CO2
    color_continuous_scale=px.colors.sequential.Reds #Variação de cor
)

#---------------------------------------------------------------------------------------------------------
#Dados para Gráficos 3 e 4.

# Dicionário com os continentes
emissoes =	{
  'Africa': [], # Continentes/Key : valor(es) = (lista vazia)
  'Asia': [],
  'Europe': [],
  'North America': [],
  'Oceania': [],
  'South America': [],
}

# Adicionando os dados de emissão para cada lista de continentes do dicionário
for linha in df_array:
  for emissao in emissoes:
    if linha[0] == emissao: # continente sendo lido no momento no df == 'key' do dicionário.
      if linha[2] >= 1987: # Não queremos todos os anos, filtramos ele.
        emissoes[emissao].append(linha[3])

Anos = list(range(1987,2021))

continents = ['Africa', 'Asia', 'Europe', 'North America', 'Oceania', 'South America'] #Original do CSV
continentes = ['África', 'Ásia', 'Europa', 'América do Norte', 'Oceania', 'América do Sul'] # Traduzido

#----------------------------
#Grafico3

fig3 = px.bar(
    x=Anos, 
    y=Anos)

#----------------------------
#Grafico4

fig4 = px.pie(
  names= continentes,
  values= continentes)

#---------------------------------------------------------------------------------------------------------
#HTML - Esqueleto da página Dash

app.layout = html.Main(id='graphs', className='container',
    children = [
        html.Div(
            children= [
                html.Img(id='logo',
                    src='assets\Logo.jpg')
                ]
            ),
        html.Div(className='graficos',
            children=[
                html.Div(className='grafico_1',
                            children = [
                                dcc.Graph(
                                    className='g1',
                                    figure=fig1),
                            ]
                        ),
                        html.Div(className='grafico_2',
                            children = [
                                dcc.Graph(figure=fig2)
                            ]
                        ),
                        html.Div(className='grafico_3',
                            children = [
                                dcc.Dropdown(continents, value='Africa' , id='continentes'),
                                dcc.Graph(
                                    id='Grafico_Barras_CO2',
                                    figure=fig3
                                )
                            ]
                        ),
                        html.Div(className='grafico_4',
                            children = [
                                dcc.Dropdown(Anos, value=1987, id='Anos'),
                                dcc.Graph(
                                    id='Grafico_Pizza_CO2',
                                    figure=fig4
                        )
                    ]
                )
            ]
        )
    ]
)        

#-------------------------------------------------------------------------------------------------------------------
#Callback's

# Callback do gráfico de barras (intermediário entre a função o dropdown)
@app.callback(
    # ↓↓↓ Saída será a nova uma nova figura/gráfico com a filtragem do continente escolhido
    Output('Grafico_Barras_CO2', 'figure'),
    Input('continentes', 'value') # Entrada será o value do ID "continentes", ou seja, o dcc.dropdown.
)

# Função o G.Barras para processar o novo gráfico filtrado
def atualizar_output(value): #Definindo uma função com o parâmetro value do input recebido de callback


    for continent in continents:
        for emissao in emissoes:
            if continent == emissao:
                if value == continent:
                    fig3 = px.bar(
                        x = Anos,
                        y = emissoes[continent]
                    )

    fig3.update_layout(
    title="Emissão por continente",
    xaxis_title="Anos",
    yaxis_title="Emissão",
    )

    return fig3

# Callback do Gráfico de Pizza (intermediário entre a função o dropdown)
@app.callback(
    Output('Grafico_Pizza_CO2', 'figure'),
    Input('Anos', 'value')
)

# Função o G.Pizza para processar o novo gráfico filtrado
def update_output(value):
    ano_especifico = []

    i = 0 
    while i < 34: # 33 anos entre 1987 à 2020
        if value == Anos[i]:
            posição = i # Marca a posição do ano que o usuário escolheu
            break # Quebra do looping
        i += 1 # i = i + 1

    for continente in emissoes:
      # ↓↓↓ Acrescentando somente os dados de emissão, de cada continente, no índice/posição do ano específico
      ano_especifico.append(emissoes[continente][posição])

    fig4 = px.pie(
    names= continentes,
    values= ano_especifico
    )

    return fig4
  
#---------------------------------------------------------------------------------------------------------

# Colocando a 'app' pra rodar no Dash
if __name__ == '__main__':
    app.run_server(debug=True)