# Importação das bibliotecas que utilizaremos:

from dash import Dash, html, dcc, Input, Output #importante para a criação do site e alguma coisa dos gráficos;
import plotly.express as px #Para funcionalidades do Plotly, assim criando nosso gráfico;
from pandas import read_csv # Para Leituras de bases de Dados, como excel, CSV, etc...

# Definindo um aplicativo (O nosso DashBoard) do Flask
DashBoard = Dash(__name__)

# O nosso DataFrame vai ler uma aquivo csv para criarmos o nosso gráfico
first = 1987
years = range(first, 2021)
continents = ['Africa', 'Asia', 'Europe', 'North America', 'Oceania', 'South America']
continentes = ['Áfica', 'Ásia', 'Europa', 'América do Norte', 'Oceania', 'América do Sul']

df = read_csv('https://raw.githubusercontent.com/Dashboard-Plotly/Dashboard-CO2/main/annual-co2-emissions-per-country.csv')
df_array = df.values

annual_emissions = {}
for year in years:
  annual_emissions[year] = []

for line in df_array:
  entity = line[0]
  year = line[2]
  emission= line[3]

  if year in annual_emissions and entity in continents:
      annual_emissions[year].append(emission)

FigPizza = px.pie(
        values=annual_emissions[first], 
        names=continentes
    )

#Criar os anos
opcoes = list(years)


# Criando o layout da página que será hospedada nosso gráfico
DashBoard.layout = html.Div(children=[
    html.H1(children='Porcentagem por continente emissor',), # Título
    html.H3(children='Gráfico com a emissão de CO2 por continentes'), #Explicativa
    html.Div(children='''
        Obs: Esse gráfico mostra a emissão em cada continente por ano.
    '''), #Observação

    #Cria uma lista radio para que o usuário escolha o ano a visualizar
    dcc.Dropdown(opcoes, value=first, id='Anos'),

    #Utilizamos esse comando para que o site/aplicativo insira nosso gráfico de pizza.
    dcc.Graph(
        id='Grafico_Pizza_CO2', #ID para chamarmos ele mais para frente
        figure= FigPizza #Qual gráfico será exibido na página web local do computador
    )
])
#-----------------------------------------------------------------------------------------------------------

# Parte - Botando o dropdown pra funcionar (A resolver)

'''
Função para que todo input/entrada inserido/alternado recebido do dropdawn,
faça um input/saída da informação que ele deseja.
'''
@DashBoard.callback(
    # ↓↓↓ Saída será a nova uma nova figura/gráfico com a filtragem do ano escolhido
    Output('Grafico_Pizza_CO2', 'figure'),
    Input('Anos', 'value') # Entrada será o value do ID "Anos", ou seja, o dcc.dropdawn.
)

#Sem uma função, o callback se torna inútil, pois isso:
def atualizar_output(value): #Difinindo uma função com o parâmetro value do input recebido
    annual_emission = annual_emissions[value]

    FigPizza = px.pie(
        values= annual_emission, 
        names=continentes
    )

    return FigPizza
        
'''
Utilizaremos essa parte do código para que, toda vez o qual o usuário mudar o ano desejável, a function
atualizará a FIGPIZZA com o ano filtrado da escolha do usuário.
'''
#-----------------------------------------------------------------------------------------------------------
# Colocando nossos gráficos pra rodar

if __name__ == '__main__':
    DashBoard.run_server(debug=True)