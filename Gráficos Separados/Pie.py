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

#--------------------------------------------------------------------------------------------------------

# 2ª Parte

#-------------------------
continentes = ['Áfica', 'Ásia', 'Europa', 'América do Norte', 'Oceania', 'América do Sul']
#-------------------------

# Definindo as anos para cada variável.

D_1987 = []
D_1988 = []
D_1989 = []
D_1990 = []
D_1991 = []
D_1992 = []
D_1993 = []
D_1994 = []
D_1995 = []
D_1996 = []
D_1997 = []
D_1998 = []
D_1999 = []
D_2000 = []
D_2001 = []
D_2002 = []
D_2003 = []
D_2004 = []
D_2005 = []
D_2006 = []
D_2007 = []
D_2008 = []
D_2009 = []
D_2010 = []
D_2011 = []
D_2012 = []
D_2013 = []
D_2014 = []
D_2015 = []
D_2016 = []
D_2017 = []
D_2018 = []
D_2019 = []
D_2020 = []

D_cont = 0
contn = 0

while contn < 34: #Enquanto o contn ser menor que 34, faça:
    if contn == 0: #se o contador for 0, significa que ele pegará as informações do ano 1987, em cada continente
        D_1987.append(Africa[D_cont])
        D_1987.append(Asia[D_cont])
        D_1987.append(Europe[D_cont])
        D_1987.append(North_America[D_cont])
        D_1987.append(Oceania[D_cont])
        D_1987.append(South_America[D_cont])

        '''
        Estamos acrescentando os dados de emisão no índice 0 de cada variável dos continentes,
        pois a partir dessa variável, sempre atualizaremos os anos de acordo com que o usuário
        deseje visualizar o ano específico.
        '''
    elif contn == 1: #se o contador for 1, significa que ele pegará as informações do ano 1988, em cada continente
        D_1988.append(Africa[D_cont])
        D_1988.append(Asia[D_cont])
        D_1988.append(Europe[D_cont])
        D_1988.append(North_America[D_cont])
        D_1988.append(Oceania[D_cont])
        D_1988.append(South_America[D_cont])
    elif contn == 2:
        D_1989.append(Africa[D_cont])
        D_1989.append(Asia[D_cont])
        D_1989.append(Europe[D_cont])
        D_1989.append(North_America[D_cont])
        D_1989.append(Oceania[D_cont])
        D_1989.append(South_America[D_cont])
    elif contn == 3:
        D_1990.append(Africa[D_cont])
        D_1990.append(Asia[D_cont])
        D_1990.append(Europe[D_cont])
        D_1990.append(North_America[D_cont])
        D_1990.append(Oceania[D_cont])
        D_1990.append(South_America[D_cont])
    elif contn == 4:
        D_1991.append(Africa[D_cont])
        D_1991.append(Asia[D_cont])
        D_1991.append(Europe[D_cont])
        D_1991.append(North_America[D_cont])
        D_1991.append(Oceania[D_cont])
        D_1991.append(South_America[D_cont])
    elif contn == 5:
        D_1992.append(Africa[D_cont])
        D_1992.append(Asia[D_cont])
        D_1992.append(Europe[D_cont])
        D_1992.append(North_America[D_cont])
        D_1992.append(Oceania[D_cont])
        D_1992.append(South_America[D_cont])
    elif contn == 6:
        D_1993.append(Africa[D_cont])
        D_1993.append(Asia[D_cont])
        D_1993.append(Europe[D_cont])
        D_1993.append(North_America[D_cont])
        D_1993.append(Oceania[D_cont])
        D_1993.append(South_America[D_cont])
    elif contn == 7:
        D_1994.append(Africa[D_cont])
        D_1994.append(Asia[D_cont])
        D_1994.append(Europe[D_cont])
        D_1994.append(North_America[D_cont])
        D_1994.append(Oceania[D_cont])
        D_1994.append(South_America[D_cont])
    elif contn == 8:
        D_1995.append(Africa[D_cont])
        D_1995.append(Asia[D_cont])
        D_1995.append(Europe[D_cont])
        D_1995.append(North_America[D_cont])
        D_1995.append(Oceania[D_cont])
        D_1995.append(South_America[D_cont])
    elif contn == 9:
        D_1996.append(Africa[D_cont])
        D_1996.append(Asia[D_cont])
        D_1996.append(Europe[D_cont])
        D_1996.append(North_America[D_cont])
        D_1996.append(Oceania[D_cont])
        D_1996.append(South_America[D_cont])
    elif contn == 10:
        D_1997.append(Africa[D_cont])
        D_1997.append(Asia[D_cont])
        D_1997.append(Europe[D_cont])
        D_1997.append(North_America[D_cont])
        D_1997.append(Oceania[D_cont])
        D_1997.append(South_America[D_cont])
    elif contn == 11:
        D_1998.append(Africa[D_cont])
        D_1998.append(Asia[D_cont])
        D_1998.append(Europe[D_cont])
        D_1998.append(North_America[D_cont])
        D_1998.append(Oceania[D_cont])
        D_1998.append(South_America[D_cont])
    elif contn == 12:
        D_1999.append(Africa[D_cont])
        D_1999.append(Asia[D_cont])
        D_1999.append(Europe[D_cont])
        D_1999.append(North_America[D_cont])
        D_1999.append(Oceania[D_cont])
        D_1999.append(South_America[D_cont])
    elif contn == 13:
        D_2000.append(Africa[D_cont])
        D_2000.append(Asia[D_cont])
        D_2000.append(Europe[D_cont])
        D_2000.append(North_America[D_cont])
        D_2000.append(Oceania[D_cont])
        D_2000.append(South_America[D_cont])
    elif contn == 14:
        D_2001.append(Africa[D_cont])
        D_2001.append(Asia[D_cont])
        D_2001.append(Europe[D_cont])
        D_2001.append(North_America[D_cont])
        D_2001.append(Oceania[D_cont])
        D_2001.append(South_America[D_cont])
    elif contn == 15:
        D_2002.append(Africa[D_cont])
        D_2002.append(Asia[D_cont])
        D_2002.append(Europe[D_cont])
        D_2002.append(North_America[D_cont])
        D_2002.append(Oceania[D_cont])
        D_2002.append(South_America[D_cont])
    elif contn == 16:
        D_2003.append(Africa[D_cont])
        D_2003.append(Asia[D_cont])
        D_2003.append(Europe[D_cont])
        D_2003.append(North_America[D_cont])
        D_2003.append(Oceania[D_cont])
        D_2003.append(South_America[D_cont])
    elif contn == 17:
        D_2004.append(Africa[D_cont])
        D_2004.append(Asia[D_cont])
        D_2004.append(Europe[D_cont])
        D_2004.append(North_America[D_cont])
        D_2004.append(Oceania[D_cont])
        D_2004.append(South_America[D_cont])
    elif contn == 18:
        D_2005.append(Africa[D_cont])
        D_2005.append(Asia[D_cont])
        D_2005.append(Europe[D_cont])
        D_2005.append(North_America[D_cont])
        D_2005.append(Oceania[D_cont])
        D_2005.append(South_America[D_cont])
    elif contn == 19:
        D_2006.append(Africa[D_cont])
        D_2006.append(Asia[D_cont])
        D_2006.append(Europe[D_cont])
        D_2006.append(North_America[D_cont])
        D_2006.append(Oceania[D_cont])
        D_2006.append(South_America[D_cont])
    elif contn == 20:
        D_2007.append(Africa[D_cont])
        D_2007.append(Asia[D_cont])
        D_2007.append(Europe[D_cont])
        D_2007.append(North_America[D_cont])
        D_2007.append(Oceania[D_cont])
        D_2007.append(South_America[D_cont])
    elif contn == 21:
        D_2008.append(Africa[D_cont])
        D_2008.append(Asia[D_cont])
        D_2008.append(Europe[D_cont])
        D_2008.append(North_America[D_cont])
        D_2008.append(Oceania[D_cont])
        D_2008.append(South_America[D_cont])
    elif contn == 22:
        D_2009.append(Africa[D_cont])
        D_2009.append(Asia[D_cont])
        D_2009.append(Europe[D_cont])
        D_2009.append(North_America[D_cont])
        D_2009.append(Oceania[D_cont])
        D_2009.append(South_America[D_cont])
    elif contn == 23:
        D_2010.append(Africa[D_cont])
        D_2010.append(Asia[D_cont])
        D_2010.append(Europe[D_cont])
        D_2010.append(North_America[D_cont])
        D_2010.append(Oceania[D_cont])
        D_2010.append(South_America[D_cont])
    elif contn == 24:
        D_2011.append(Africa[D_cont])
        D_2011.append(Asia[D_cont])
        D_2011.append(Europe[D_cont])
        D_2011.append(North_America[D_cont])
        D_2011.append(Oceania[D_cont])
        D_2011.append(South_America[D_cont])
    elif contn == 25:
        D_2012.append(Africa[D_cont])
        D_2012.append(Asia[D_cont])
        D_2012.append(Europe[D_cont])
        D_2012.append(North_America[D_cont])
        D_2012.append(Oceania[D_cont])
        D_2012.append(South_America[D_cont])
    elif contn == 26:
        D_2013.append(Africa[D_cont])
        D_2013.append(Asia[D_cont])
        D_2013.append(Europe[D_cont])
        D_2013.append(North_America[D_cont])
        D_2013.append(Oceania[D_cont])
        D_2013.append(South_America[D_cont])
    elif contn == 27:
        D_2014.append(Africa[D_cont])
        D_2014.append(Asia[D_cont])
        D_2014.append(Europe[D_cont])
        D_2014.append(North_America[D_cont])
        D_2014.append(Oceania[D_cont])
        D_2014.append(South_America[D_cont])
    elif contn == 28:
        D_2015.append(Africa[D_cont])
        D_2015.append(Asia[D_cont])
        D_2015.append(Europe[D_cont])
        D_2015.append(North_America[D_cont])
        D_2015.append(Oceania[D_cont])
        D_2015.append(South_America[D_cont])
    elif contn == 29:
        D_2016.append(Africa[D_cont])
        D_2016.append(Asia[D_cont])
        D_2016.append(Europe[D_cont])
        D_2016.append(North_America[D_cont])
        D_2016.append(Oceania[D_cont])
        D_2016.append(South_America[D_cont])
    elif contn == 30:
        D_2017.append(Africa[D_cont])
        D_2017.append(Asia[D_cont])
        D_2017.append(Europe[D_cont])
        D_2017.append(North_America[D_cont])
        D_2017.append(Oceania[D_cont])
        D_2017.append(South_America[D_cont])
    elif contn == 31:
        D_2018.append(Africa[D_cont])
        D_2018.append(Asia[D_cont])
        D_2018.append(Europe[D_cont])
        D_2018.append(North_America[D_cont])
        D_2018.append(Oceania[D_cont])
        D_2018.append(South_America[D_cont])
    elif contn == 32:
        D_2019.append(Africa[D_cont])
        D_2019.append(Asia[D_cont])
        D_2019.append(Europe[D_cont])
        D_2019.append(North_America[D_cont])
        D_2019.append(Oceania[D_cont])
        D_2019.append(South_America[D_cont])
    elif contn == 33:
        D_2020.append(Africa[D_cont])
        D_2020.append(Asia[D_cont])
        D_2020.append(Europe[D_cont])
        D_2020.append(North_America[D_cont])
        D_2020.append(Oceania[D_cont])
        D_2020.append(South_America[D_cont])
    contn += 1
    D_cont += 1

# print(D_1987)
# print(D_1988)
# print(D_1989)
# print(D_1990)
# print(D_1991)
# print(D_1992)
# print(D_1993)
# print(D_1994)
# print(D_1995)
# print(D_1996)
# print(D_1997)
# print(D_1998)
# print(D_1999)
# print(D_2000)
# print(D_2001)
# print(D_2002)
# print(D_2003)
# print(D_2004)
# print(D_2005)
# print(D_2006)
# print(D_2007)
# print(D_2008)
# print(D_2009)
# print(D_2010)
# print(D_2011)
# print(D_2012)
# print(D_2013)
# print(D_2014)
# print(D_2015)
# print(D_2016)
# print(D_2017)
# print(D_2018)
# print(D_2019)
# print(D_2020)

'''
Depois que dividimos os dados para cada continentes, essa parte do código pega cada dado, em cada continente,
para pôr devidamente ao seu ano.

Vale lembrar que por conta dessa filtração, os dados estão em respectiva ordem:
Ano[Emissão África, Emissão Ásia, Emissão Europa, Emissão América do Norte, Emissão Oceania, Emissão América do Sul]
'''
#---------------------------------------------------------------------------------------------------------------

# Parte - Layout da página

FigPizza = px.pie(
    D_1987, 
    names=continentes, 
    values=D_1987)

#Criar os anos
Anos = range(1987,2021) #Cria uma Variável Anos para fazer nossa caixa de anos em ordem
opcoes = list(Anos) # Fazer uma outra variável para fazer uma listagem de Anos

# Ciando o layout da página que será hospedada nosso gráfico

DashBoard.layout = html.Div(children=[
    html.H1(children='Porcentagem por continente emissor',), # Título
    html.H3(children='Gráfico com a emissão de CO2 por continentes'), #Explicativa
    html.Div(children='''
        Obs: Esse gráfico mostra a emissão em cada continente por ano.
    '''), #Observação

    #Cria uma lista radio para que o usuário escolha o ano a visualizar
    dcc.Dropdown(opcoes, value=1987, id='Anos'),

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
    if value == 1987: # Cada vez que o value do input ser mudado para 1987, faça:
        FigPizza = px.pie(
        D_1987, 
        names=continentes, 
        values=D_1987,
        color=continentes)

        '''
        Nessta parte estamos reconstruido o gráfico "FigPizza" somente para o ano específico o qual o usuário
        selecionou nesse exemplo sendo o ano de 1987.
        '''
    if value == 1988: # Cada vez que o value do input ser mudado para 1988, faça:
        FigPizza = px.pie(
        D_1988, 
        names=continentes, 
        values=D_1988,
        color=continentes)
    if value == 1989: # Cada vez que o value do input ser mudado para 1989, faça:
        FigPizza = px.pie(
        D_1989, 
        names=continentes, 
        values=D_1989,
        color=continentes)
    if value == 1990:
        FigPizza = px.pie(
        D_1990, 
        names=continentes, 
        values=D_1990,
        color=continentes)
    if value == 1991:
        FigPizza = px.pie(
        D_1991, 
        names=continentes, 
        values=D_1991,
        color=continentes)
    if value == 1992:
        FigPizza = px.pie(
        D_1992, 
        names=continentes, 
        values=D_1992,
        color=continentes)
    if value == 1993:
        FigPizza = px.pie(
        D_1993, 
        names=continentes, 
        values=D_1993,
        color=continentes)
    if value == 1994:
        FigPizza = px.pie(
        D_1994, 
        names=continentes, 
        values=D_1994,
        color=continentes)
    if value == 1995:
        FigPizza = px.pie(
        D_1995, 
        names=continentes, 
        values=D_1995,
        color=continentes)
    if value == 1996:
        FigPizza = px.pie(
        D_1996, 
        names=continentes, 
        values=D_1996,
        color=continentes)
    if value == 1997:
        FigPizza = px.pie(
        D_1997, 
        names=continentes, 
        values=D_1997,
        color=continentes)
    if value == 1998:
        FigPizza = px.pie(
        D_1998, 
        names=continentes, 
        values=D_1998,
        color=continentes)
    if value == 1999:
        FigPizza = px.pie(
        D_1999, 
        names=continentes, 
        values=D_1999,
        color=continentes)
    if value == 2000:
        FigPizza = px.pie(
        D_2000, 
        names=continentes, 
        values=D_2000,
        color=continentes)
    if value == 2001:
        FigPizza = px.pie(
        D_2001, 
        names=continentes, 
        values=D_2001,
        color=continentes)
    if value == 2002:
        FigPizza = px.pie(
        D_2002, 
        names=continentes, 
        values=D_2002,
        color=continentes)
    if value == 2003:
        FigPizza = px.pie(
        D_2003, 
        names=continentes, 
        values=D_2003,
        color=continentes)
    if value == 2004:
        FigPizza = px.pie(
        D_2004, 
        names=continentes, 
        values=D_2004,
        color=continentes)
    if value == 2005:
        FigPizza = px.pie(
        D_2005, 
        names=continentes, 
        values=D_2005,
        color=continentes)
    if value == 2006:
        FigPizza = px.pie(
        D_2006, 
        names=continentes, 
        values=D_2006,
        color=continentes)
    if value == 2007:
        FigPizza = px.pie(
        D_2007, 
        names=continentes, 
        values=D_2007,
        color=continentes)
    if value == 2008:
        FigPizza = px.pie(
        D_2008, 
        names=continentes, 
        values=D_2008,
        color=continentes)
    if value == 2009:
        FigPizza = px.pie(
        D_2009, 
        names=continentes, 
        values=D_2009,
        color=continentes)
    if value == 2010:
        FigPizza = px.pie(
        D_2010, 
        names=continentes, 
        values=D_2010,
        color=continentes)
    if value == 2011:
        FigPizza = px.pie(
        D_2011, 
        names=continentes, 
        values=D_2011,
        color=continentes)
    if value == 2012:
        FigPizza = px.pie(
        D_2012, 
        names=continentes, 
        values=D_2012,
        color=continentes)
    if value == 2013:
        FigPizza = px.pie(
        D_2013, 
        names=continentes, 
        values=D_2013,
        color=continentes)
    if value == 2014:
        FigPizza = px.pie(
        D_2014, 
        names=continentes, 
        values=D_2014,
        color=continentes)
    if value == 2015:
        FigPizza = px.pie(
        D_2015, 
        names=continentes, 
        values=D_2015,
        color=continentes)
    if value == 2016:
        FigPizza = px.pie(
        D_2016, 
        names=continentes, 
        values=D_2016,
        color=continentes)
    if value == 2017:
        FigPizza = px.pie(
        D_2017, 
        names=continentes, 
        values=D_2017,
        color=continentes)
    if value == 2018:
        FigPizza = px.pie(
        D_2018, 
        names=continentes, 
        values=D_2018,
        color=continentes)
    if value == 2019:
        FigPizza = px.pie(
        D_2019, 
        names=continentes, 
        values=D_2019,
        color=continentes)
    if value == 2020:
        FigPizza = px.pie(
        D_2020, 
        names=continentes, 
        values=D_2020,
        color=continentes)

    return FigPizza
        
'''
Utilizaremos essa parte do código para que, toda vez o qual o usuário mudar o ano desejável, a function
atualizará a FIGPIZZA com o ano filtrado da escolha do usuário.
'''
#-----------------------------------------------------------------------------------------------------------
# Colocando nossos gráficos pra rodar

if __name__ == '__main__':
    DashBoard.run_server(debug=True)