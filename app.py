# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

# Import necessary libraries
from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import pandas as pd

# Initialize the Dash app
app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options



# # Cria a base de dados de exemplo, pode ser substituída por qualquer outra fonte de dados
# df = pd.DataFrame({
#     "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
#     "Amount": [4, 1, 2, 2, 4, 5],
#     "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
# })

# usando uma babe de dados de um arquivo excel 
df = pd.read_excel('vendas.xlsx')

#Cria o do gráfico de barras
fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")

opcoes = list(df['ID Loja'].unique())
opcoes.append("Todas as Lojas")

# Define the layout of the app com componentes HTML e gráficos(dcc)
app.layout = html.Div(children=[     # conteúdo da página, com uma lista de itens filhos

    html.H1(children='Faturamento das lojas'),  # título principal
    html.H1(children='Gáfico todos os faturamentos das lojas '), # subtítulo adicional
    html.Div(children='''            
        OBS: Esse gráfico mostra a quantidade de produtos vendidos por loja.
    '''),

    dcc.Dropdown(opcoes,value='Todas as Lojas', id='lista_lojas'),

    dcc.Graph(                       # componente de gráfico
        id='grafico_quantidade_vendas',
        figure=fig
    )
])

@app.callback(
    Output('grafico_quantidade_vendas', 'figure'),
    Input('lista_lojas', 'value')
)
def update_output(value):
    if value == 'Todas as Lojas':
        fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
    else:
        tabela_filtrada = df.loc[df['ID Loja'] == value, :]
        fig = px.bar(tabela_filtrada, x="Produto", y="Quantidade", color="ID Loja", barmode="group")


    return fig

if __name__ == '__main__':
    app.run(debug=True)
