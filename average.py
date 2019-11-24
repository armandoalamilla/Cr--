import pandas as pd
import plotly.graph_objects as go
import plotly.express as px


path = 'csv/100 Sales Records.csv'
par1 = 'Region'
par2 = 'Units Sold'
grafico = 'piechart'


def average(path,par1,par2,grafico):
    data = pd.read_csv(path)
    data[par2] = data[par2].astype(float)
    algo = data.groupby(par1).agg({par2:'mean'})
    listaPar1 = list(algo[par2].keys())
    listaPar2 = list(algo[par2])

    if grafico == 'piechart':
        fig = go.Figure(data=[go.Pie(labels=listaPar1, values=listaPar2)])
        fig.update_layout(title_text= par1 + '/' + par2 +'--- PROMEDIO')
        fig.write_html('promedio.html', auto_open=True)
    elif grafico == 'barchart':
        fig = px.bar(algo, x=listaPar1, y=listaPar2)
        fig.update_layout(title_text= collection_name + ': '+ par1 + '/' + par2 +'--- PROMEDIO')
        fig.write_html('promedio.html', auto_open=True)
    else:
        print("SOLO SE PUEDE GRAFICAR piechart o barchart")

average(path,par1,par2,grafico)












