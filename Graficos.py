from turtle import width
from pandas import read_csv
from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import plotly.graph_objects as go

app = Dash(__name__)

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
#Grafico3

anos = range(1987,2021)

Africa = []
Asia = []
Europe = []
North_America = []
Oceania = []
South_America = []

ano_começo = 1987
ano_fim = 2021

while ano_começo != ano_fim:
    for linha in df_array: #Para cada linha do df_array, faça:
        if linha[2] == ano_começo: #Se essa linha, no índice 2 ser o ano_começo pra frente, faça:
            if linha[0] == 'Africa': #Se essa mesma linha ter, no índice 0, a "Africa", faça:
                Africa.append(linha[3]) #Adicione (Append) um novo valor na variável Africa. 
            elif linha[0] == 'Asia': #Ou se essa mesma linha, no mesmo índice, ser "Asia", faça:
                Asia.append(linha[3])
            elif linha[0] == 'Europe':
                Europe.append(linha[3])
            elif linha[0] == 'North America':
                North_America.append(linha[3])
            elif linha[0] == 'Oceania':
                Oceania.append(linha[3])
            elif linha[0] == 'South America':
                South_America.append(linha[3])
    ano_começo +=1

continentes = ['África', 'Ásia', 'Europa', 'América do Norte', 'Oceania', 'América do Sul']

fig3 = px.bar(
            x=anos, 
            y=Africa)

#---------------------------------------------------------------------------------------------------------
#Grafico4

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

continentes = ['África', 'Ásia', 'Europa', 'América do Norte', 'Oceania', 'América do Sul']

Anos = list(range(1987,2021))

fig4 = px.pie(
  names= continentes,
  values= continentes
)



#---------------------------------------------------------------------------------------------------------
#HTML

app.layout = html.Main(id='graphs', className='graficos',
    children = [
        html.Div(className='grafico_1',
            children = [
                dcc.Graph(figure=fig1),
            ]
        ),
        html.Div(className='grafico_2',
            children = [
                dcc.Graph(figure=fig2)
            ]
        ),
        html.Div(className='grafico_3',
            children = [
                dcc.Dropdown(continentes, value='África' , id='continentes'),
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

#-------------------------------------------------------------------------------------------------------------------
#Callback

@app.callback(
    Output('Grafico_Barras_CO2', 'figure'),
    Input('continentes', 'value')
)

def atualizar_output(value): #Definindo uma função com o parâmetro value do input recebido
    if value == 'África': # Cada vez que o value do input ser mudado para África, faça:
        fig3 = px.bar(
            x = anos,
            y = Africa
        )
    elif value == 'Ásia': # Cada vez que o value do input ser mudado para Ásia, faça:
        fig3 = px.bar(
            x = anos,
            y = Asia
        )
    elif value == 'Europa': # Cada vez que o value do input ser mudado para Europa, faça:
        fig3 = px.bar(
            x = anos,
            y = Europe
        )
    elif value == 'América do Norte': # Cada vez que o value do input ser mudado para América do Norte, faça:
        fig3 = px.bar(
            x = anos,
            y = North_America
        )
    elif value == 'Oceania': # Cada vez que o value do input ser mudado para Oceania, faça:
        fig3 = px.bar(
            x = anos,
            y = Oceania
        )
    elif value == 'América do Sul': # Cada vez que o value do input ser mudado para América do Sul, faça:
        fig3 = px.bar(
            x = anos,
            y = South_America
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

    FigPizza = px.pie(
    names= continentes,
    values= ano_especifico
    )

    '''
    Criando o novo gráfico filtrado somente com os anos escolhido pelo usuário.
    '''
  return FigPizza
  
#---------------------------------------------------------------------------------------------------------
#
if __name__ == '__main__':
    app.run_server(debug=True)