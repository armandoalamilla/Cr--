import plotly.graph_objects as go
import pandas as pd

url = "csv/microsoftStocks.csv"
par1 = 'High'
par2 = 'Low'
par3 = 'Date'
df = pd.read_csv(url)


def plot(url,par1,par2,par3):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
                    x=df[par3],
                    y=df[par1],
                    name=par1,
                    line_color='deepskyblue',
                    opacity=0.8))

    fig.add_trace(go.Scatter(
                    x=df[par3],
                    y=df[par2],
                    name=par2,
                    line_color='dimgray',
                    opacity=0.8))

    # Use date string to set xaxis range
    fig.update_layout(title_text=url)
    fig.write_html('plot.html', auto_open=True)

plot(url,par1,par2,par3)


