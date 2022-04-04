#Importação das bibliotecas

from pandas import read_csv
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

app = Dash(__name__, title='Emissão de CO2')

df = read_csv("annual-co2-emissions-per-country.csv")
df_array = df.values

#---------------------------------------------------------------------------------------------------------
#Grafico1

world = []

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

anos = [] 
for linha in df_array:
    if linha[2] in range(1750,2021):
        if (linha[0] != 'Africa') and (linha[0] != 'Asia') and (linha[0] != 'Europe') and (linha[0] != 'North America') and (linha[0] != 'Oceania') and (linha[0] != 'South America') and (linha[0] != 'World'):
            anos.append(linha[2])
anos = sorted(anos)

paises = [] 
for linha in df_array:
    if linha[2] in anos:
        if (linha[0] != 'Africa') and (linha[0] != 'Asia') and (linha[0] != 'Europe') and (linha[0] != 'North America') and (linha[0] != 'Oceania') and (linha[0] != 'South America') and (linha[0] != 'World'):
            paises.append(linha[0])

paises_ordenados = []
ano_come = 1750
ano_fim = 2021
while ano_fim != ano_come:
    for linha in df_array:
        if linha[2] == ano_come:
            if (linha[0] != 'Africa') and (linha[0] != 'Asia') and (linha[0] != 'Europe') and (linha[0] != 'North America') and (linha[0] != 'Oceania') and (linha[0] != 'South America') and (linha[0] != 'World'):
                paises_ordenados.append(linha[0])
    ano_come += 1

codigo = []
for linha in df_array:
    if linha[2] in anos:
        if (linha[0] != 'Africa') and (linha[0] != 'Asia') and (linha[0] != 'Europe') and (linha[0] != 'North America') and (linha[0] != 'Oceania') and (linha[0] != 'South America') and (linha[0] != 'World'):
            codigo.append(linha[1])

codigo_ordenado = []
ano_come = 1750
ano_fim = 2021
while ano_fim != ano_come:
    for linha in df_array:
        if linha[2] == ano_come:
            if (linha[0] != 'Africa') and (linha[0] != 'Asia') and (linha[0] != 'Europe') and (linha[0] != 'North America') and (linha[0] != 'Oceania') and (linha[0] != 'South America') and (linha[0] != 'World'):
                codigo_ordenado.append(linha[1])
    ano_come += 1

nivel = []
for linha in df_array:
    if linha[2] in anos:
        if (linha[0] != 'Africa') and (linha[0] != 'Asia') and (linha[0] != 'Europe') and (linha[0] != 'North America') and (linha[0] != 'Oceania') and (linha[0] != 'South America') and (linha[0] != 'World'):
            nivel.append(linha[3])

nivel_ordenado = []
ano_come = 1750
ano_fim = 2021
while ano_fim != ano_come:
    for linha in df_array:
        if linha[2] == ano_come:
            if (linha[0] != 'Africa') and (linha[0] != 'Asia') and (linha[0] != 'Europe') and (linha[0] != 'North America') and (linha[0] != 'Oceania') and (linha[0] != 'South America') and (linha[0] != 'World'):
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

emissoes =	{
  'Africa': [], # Continentes/Key : valor(es) =(lista vazia)
  'Asia': [],
  'Europe': [],
  'North America': [],
  'Oceania': [],
  'South America': [],
}

for linha in df_array: # para cada linha do df_array...:
  for emissao in emissoes: # E para cada linha/key do dicionário 'emissoes', faça:
    if linha[0] == emissao: # Se a linha sendo lida do df_array, no índice 0, ser o mesmo que a linha da "Emissões"...
      if 1987 <= linha[2]:  # E a linha do df_array, no índice 2, ser maior ou igual a 1987, faça:
        # ↓↓↓ Acrescente no dicionário, no índice da emissão/continente, o índice 3 do df_array.
        emissoes[emissao].append(linha[3])

Anos = list(range(1987,2021))

continents = ['Africa', 'Asia', 'Europe', 'North America', 'Oceania', 'South America'] #Original do CSV
continentes = ['África', 'Ásia', 'Europa', 'América do Norte', 'Oceania', 'América do Sul'] # Traduzido

#----------------------------
#Grafico3

fig3 = px.bar(
            x=anos, 
            y=anos)

#----------------------------
#Grafico4

fig4 = px.pie(
  names= continentes,
  values= continentes
)

#---------------------------------------------------------------------------------------------------------
#HTML

app.layout = html.Main(id='graphs', className='container',
    children = [
        html.H1(className = 'title', children='CO2'),
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
#Callback

@app.callback(
    Output('Grafico_Barras_CO2', 'figure'),
    Input('continentes', 'value')
)

def atualizar_output(value): #Definindo uma função com o parâmetro value do input recebido
    if value == value:

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

@app.callback(
    # ↓↓↓ Saída será a nova uma nova figura/gráfico com a filtragem do ano escolhido
    Output('Grafico_Pizza_CO2', 'figure'),
    Input('Anos', 'value') # Entrada será o value do ID "Anos", ou seja, o dcc.dropdawn.
)

def update_output(value):
  ano_especifico = [] #Lista vazia

  if value == value: # Toda vez que o usuário mudar o input (caixa de opções)
    i = 0 
    while i < 34: #Enquanto 'i' for menor de 34, faça:
      if value == Anos[i]: # Se o value for igual que o índice 'i' da lista 'Anos', faça:
        posição = i # A Posição (que utilizaremos para adicionar somente as emissões do ano específico)
        break # Quebra do looping
      i += 1 # i = i + 1

    for continente in emissoes: # Para cada linha dentro do dicionário 'emissoes', faça:
      # ↓↓↓ Acrescente somente os dados de emissão, de cada continente, da posição do ano específico
      ano_especifico.append(emissoes[continente][posição])

    fig4 = px.pie(
    names= continentes,
    values= ano_especifico
    )

    '''
    Criando o novo gráfico filtrado somente com os anos escolhido pelo usuário.
    '''
  return fig4
  
#---------------------------------------------------------------------------------------------------------
#
if __name__ == '__main__':
    app.run_server(debug=True)