import pandas as pd
import plotly.graph_objects as go
import plotly.express as px


#path = 'csv/100 Sales Records.csv'
#par1 = 'Region'
#par2 = 'Units Sold'


def pieChart(path,par1,par2):
    data = pd.read_csv(path)
    data[par2] = data[par2].astype(float)
    algo = data.groupby(par1).agg({par2:'sum'})
    listaPar1 = list(algo[par2].keys())
    listaPar2 = list(algo[par2])
    
    fig = go.Figure(data=[go.Pie(labels=listaPar1, values=listaPar2)])
    fig.update_layout(title_text= par1 + '/' + par2 +'--- TOTAL')
    fig.write_html('pastel.html', auto_open=True)
    

#pieChart(path,par1,par2)












