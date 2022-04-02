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

# 1ª Parte

#Cria uma variável "list" com base nos valores do nosso DataFrame
df_array = df.values

# print(df_array)

# Criando um dicionário com variável "emissoes".
emissoes =	{
  'Africa': [], # Continentes/Key : valor(es) =(lista vazia)
  'Asia': [],
  'Europe': [],
  'North America': [],
  'Oceania': [],
  'South America': [],
}

# print(emissoes)

# Acrescentando na lista dos valores para cada key/continentes.
for linha in df_array: # para cada linha do df_array...:
  for emissao in emissoes: # E para cada linha/key do dicionário 'emissoes', faça:
    if linha[0] == emissao: # Se a linha sendo lida do df_array, no índice 0, ser o mesmo que a linha da "Emissões"...
      if 1987 <= linha[2]:  # E a linha do df_array, no índice 2, ser maior ou igual a 1987, faça:
        # ↓↓↓ Acrescente no dicionário, no índice da emissão/continente, o índice 3 do df_array.
        emissoes[emissao].append(linha[3])

# print(emissoes)

'''
O que queremos nessa parte é filtrar nossos dados somente para os continentes que o arquivo CSV possui,
caso contrário, em qualquer utilização do mesmo resultaria na saída de todas as informções de cada país,
continentes e o todo (World).

Já estamos dividindo os dados da variável para cada continente.
Vale lembrar que eles já estão em ordem, uma vez que a leitura dos dados já foi feita linha por linha
da variável.

É importante saber que essas informações estão sendo guardadas em um dicionário para cada continente cada continentes,
assim, usaremos ele futuramente.

Obs: Estão sendo guardados somente a emissão de CO2 dos continentes (linha[3]).

Depois que dividimos os dados para cada continentes, essa parte do código pega cada dado, em cada continente,
para pôr devidamente ao seu ano.
'''

#--------------------------------------------------------------------------------------------------------

# 2ª Parte

continentes = ['Áfica', 'Ásia', 'Europa', 'América do Norte', 'Oceania', 'América do Sul']

# ↓↓↓ Cria uma lista dos anos que utilizaremos para filtrar nossos dados e para fazer o dropdown.
Anos = list(range(1987,2021))

'''
Utilizaremos essa lista tanto para criarmos o corpo do nosso gráfico de pizza/torta, quanto para tradução
dos nossos continentes. 
'''
#---------------------------------------------------------------------------------------------------------------

# Parte - Layout da página

FigPizza = px.pie(
  names= continentes,
  values= continentes
)

# Ciando o layout da página que será hospedada nosso gráfico

DashBoard.layout = html.Div(children=[
    html.H1(children='Porcentagem por continente emissor',), # Título
    html.H3(children='Gráfico com a emissão de CO2 por continentes'), #Explicativa
    html.Div(children='''
        Obs: Esse gráfico mostra a emissão em cada continente por ano.
    '''), #Observação

    #Cria uma lista radio para que o usuário escolha o ano a visualizar
    dcc.Dropdown(Anos, value=1987, id='Anos'),

    #Utilizamos esse comando para que o site/aplicativo insira nosso gráfico de pizza.
    dcc.Graph(
        id='Grafico_Pizza_CO2', #ID para chamarmos ele mais para frente
        figure= FigPizza #Qual gráfico será exibido na página web local do computador
    )
])
#-----------------------------------------------------------------------------------------------------------

# Parte - Botando o dropdown pra funcionar

'''
Função para que todo input/entrada inserido/alternado recebido do dropdawn,
faça um input/saída da informação que ele deseja.
'''

@DashBoard.callback(
    # ↓↓↓ Saída será a nova uma nova figura/gráfico com a filtragem do ano escolhido
    Output('Grafico_Pizza_CO2', 'figure'),
    Input('Anos', 'value') # Entrada será o value do ID "Anos", ou seja, o dcc.dropdawn.
)

# Sem uma função, o callback se torna inútil, pois isso:
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
  return FigPizza #Retorne a nova FigPizza filtrada

'''
Utilizaremos essa parte do código para que, toda vez o qual o usuário mudar o ano desejável, a function
atualizará a FIGPIZZA com o ano filtrado da escolha do usuário.

Vale lembrar que a função está colocando posições dependendo do ano escolhido pelo usuário, dessa forma, na hora
da lista "ano" fazer append, estamos pegando todos os dados de emissão de cada continente pelo índice da posição
do ano escolhido.

Ao final da função, ele retornará a nova function.
'''
#-----------------------------------------------------------------------------------------------------------
# Colocando nossos gráficos pra rodar:

if __name__ == '__main__':
    DashBoard.run_server(debug=True)