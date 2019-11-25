import plotly.express as px
import pandas as pd

#path = 'csv/microsoftStocks.csv'


def violin(path,par1):
    data = pd.read_csv(path)
    data[par1] = data[par1].astype(float)
    fig = px.violin(data[par1], y=par1)
    fig.update_layout(title_text= par1 + ' / ' + path)
    fig.write_html('basicViolin.html', auto_open=True)

#violin(path,'Close')


