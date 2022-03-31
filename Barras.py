from pandas import read_csv #Importação do nosso arquivo CSV.
from dash import Dash, html, dcc, Input, Output #Integração com html 
import plotly.express as px #Gráfico

# Definindo um aplicativo (O nosso DashBoard) do Flask

DashBoard = Dash(__name__)


# O nosso DataFrame vai ler um aquivo csv para criarmos o nosso gráfico

df = read_csv("annual-co2-emissions-per-country.csv")

#--------------------------------------------------------------------------------------------------------------------

df_array = df.values #Importando todos os valores do DataFrame para um variável listável (df_array).

anos = range(1987,2021)
d_continentes = [] # Dados por continentes

#Filtrando nossos dados
for linha in df_array: #Para cada linha do df_array, faça:
    if linha[2] in range(1987,2021): #Se essa linha, no índice 2 ser 1987 pra frente, faça:
        if linha[0] == 'Africa': #Se essa mesma linha ter, no índice 0, a "Africa", faça:
            d_continentes.append(linha[3]) #Adicione (Append) um novo valor na variável d_continentes. 
        elif linha[0] == 'Asia': #Ou se essa mesma linha, no mesmo índice, ser "Asia", faça:
            d_continentes.append(linha[3])
        elif linha[0] == 'Europe':
            d_continentes.append(linha[3])
        elif linha[0] == 'North America':
            d_continentes.append(linha[3])
        elif linha[0] == 'Oceania':
            d_continentes.append(linha[3])
        elif linha[0] == 'South America':
            d_continentes.append(linha[3])

#print(d_continentes)

#--------------------------------------------------------------------------------------------------------------------
# 2ª Parte

#Criando uma nova lista filtrada para cada continente.
Africa = []
Asia = []
Europe = []
North_America = []
Oceania = []
South_America = []


for cont in range(0,34): #Contador de 0 a 33 (cont é uma variável criada para esse 'for') 
    Africa.append(d_continentes[cont]) #Acrescente, na variável "Africa", o valor de d_continentes, com base no índice.

for cont in range(34,68):
    Asia.append(d_continentes[cont])
   
for cont in range(68,102):
    Europe.append(d_continentes[cont])
    
for cont in range(102,136):
    North_America.append(d_continentes[cont])
    
for cont in range(136,170):
    Oceania.append(d_continentes[cont])
    
for cont in range(170,204):
    South_America.append(d_continentes[cont])
   
# print(Africa)
# print(Asia) 
# print(Europe)
# print(North_America)
# print(Oceania)
# print(South_America)

#---------------------------

#Criamos uma variável dos continentes para usarmos futuramente no dropdown (caixa de opções) e no nosso gráfico (FigBarras)
continentes = ['África', 'Ásia', 'Europa', 'América do Norte', 'Oceania', 'América do Sul']

#--------------------------------------------------------------------------------------------------------------------
# Parte - Layout da página

#Criando o gráfico de barras na variável "FigBarras"
FigBarras = px.bar(
            x=anos, 
            y=Africa)

# Criando o layout da página que será hospedada nosso gráfico
DashBoard.layout = html.Div(children=[
    html.H1(children='Porcentagem por continente emissor',), # Título
    html.H3(children='Gráfico com a emissão de CO2 por continentes'), #Explicativa
    html.Div(children='''
        Obs: Esse gráfico mostra a emissão em cada continente por ano.
    '''), #Observação

    #Cria uma caixa de seleção para que o usuário escolha o continente a visualizar
    dcc.Dropdown(continentes, value='África' , id='continentes'),

    #Utilizamos esse comando para que o site/aplicativo insira nosso gráfico de barras.
    dcc.Graph(
        id='Grafico_Barras_CO2', #ID para chamarmos ele mais para frente
        figure= FigBarras #Qual gráfico será exibido na página web local do computador
    )
])
#-------------------------------------------------------------------------------------------------------------------

@DashBoard.callback(
    # ↓↓↓ Saída será a nova uma nova figura/gráfico com a filtragem do continente escolhido
    Output('Grafico_Barras_CO2', 'figure'),
    Input('continentes', 'value') # Entrada será o value do ID "continentes", ou seja, o dcc.dropdown.
)

#Sem uma função, o callback se torna inútil, para isso:
def atualizar_output(value): #Definindo uma função com o parâmetro value do input recebido
    if value == 'África': # Cada vez que o value do input ser mudado para África, faça:
        FigBarras = px.bar(
            x = anos,
            y = Africa
        )
        
        '''
        Nesta parte estamos reconstruido o gráfico "FigBarras" somente para o continente específico o qual o usuário
        selecionou.
        Nesse exemplo, o gráfico filtrou somente para os dados da África, pois o usuário selecionou esse continente
        na caixa de opções.
        '''
        
    elif value == 'Ásia': # Cada vez que o value do input ser mudado para Ásia, faça:
        FigBarras = px.bar(
            x = anos,
            y = Asia
        )
    elif value == 'Europa': # Cada vez que o value do input ser mudado para Europa, faça:
        FigBarras = px.bar(
            x = anos,
            y = Europe
        )
    elif value == 'América do Norte': # Cada vez que o value do input ser mudado para América do Norte, faça:
        FigBarras = px.bar(
            x = anos,
            y = North_America
        )
    elif value == 'Oceania': # Cada vez que o value do input ser mudado para Oceania, faça:
        FigBarras = px.bar(
            x = anos,
            y = Oceania
        )
    elif value == 'América do Sul': # Cada vez que o value do input ser mudado para América do Sul, faça:
        FigBarras = px.bar(
            x = anos,
            y = South_America
        )
        
    return FigBarras #retorna o novo gráfico filtrado com o continente selecionado no dropdown.

#-----------------------------------------------------------------------------------------------------------

# Colocando servidor pra rodar
if __name__ == '__main__':
     DashBoard.run_server(debug=True)