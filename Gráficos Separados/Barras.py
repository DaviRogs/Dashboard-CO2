from pandas import read_csv #Importação do nosso arquivo CSV.
from dash import Dash, html, dcc, Input, Output #Integração com html 
import plotly.express as px #Gráfico

# Definindo um aplicativo (O nosso DashBoard) do Flask

DashBoard = Dash(__name__)


# O nosso DataFrame vai ler um aquivo csv para criarmos o nosso gráfico

df = read_csv("annual-co2-emissions-per-country.csv")

'''
Estamos importando as bibliotecas essenciais para o funcionamento dos nossos gráficos e o site a ser
executado.

Além disso, já colocamos nosso código para ler o arquivo CSV o qual apresenta todos os dados necessários
para realizarmos os gráficos.
'''

#--------------------------------------------------------------------------------------------------------------------

# 1ª Parte

df_array = df.values #Importando todos os valores do DataFrame para um variável listável (df_array).

# print(df_array)

anos = range(1987,2021)

# print(anos)

#Criando uma nova lista filtrada com o que queremos
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

# print(Africa)
# print(Asia)
# print(Europe)
# print(North_America)
# print(Oceania)
# print(South_America)


'''
O que queremos nessa parte é filtrar nossos dados somente para os continentes que o arquivo CSV possui,
caso contrário, em qualquer utilização do mesmo resultaria na saída de todas as informções de cada país,
continentes e o todo (World).

Já estamos dividindo os dados da variável para cada continente.
Vale lembrar que eles já estão em ordem, uma vez que a leitura dos dados já foi feita linha por linha
da variável.

É importante saber que essas informações estão sendo guardadas em uma lista de variável de cada continentes,
assim, usaremos ele futuramente.

Obs: Estão sendo guardados somente a emissão de CO2 dos continentes (linha[3]).

'''
#-------------------------
continentes = ['Áfica', 'Ásia', 'Europa', 'América do Norte', 'Oceania', 'América do Sul']
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
        
    return FigBarras #retorna o novo gráfico filtrado com o continente selecionado no dropdown

'''
Utilizaremos essa parte do código para que, toda vez o qual o usuário mudar o continente desejável, a function
atualizará/sobrescreverá a FIGBARRA com o continente filtrado da escolha do usuário.
'''
#-----------------------------------------------------------------------------------------------------------

# Colocando servidor pra rodar
if __name__ == '__main__':
     DashBoard.run_server(debug=True)