import pandas as pd
import pymongo
import plotly.graph_objects as go
import plotly.express as px


myclient = pymongo.MongoClient('mongodb://localhost:27017/')

collection_name = 'SalesRecords'
BD = 'Cr--'
par1 = 'Region'
par2 = 'Units Sold'
mydb = myclient[BD]
mycol = mydb[collection_name]

data = pd.DataFrame(list(mycol.find()))
data[par2] = data[par2].astype(float)
algo = data.groupby(par1).agg({par2:'sum'})
listaPar1 = list(algo[par2].keys())
listaPar2 = list(algo[par2])


fig = go.Figure(data=[go.Pie(labels=listaPar1, values=listaPar2)])

fig = px.bar(algo, x=listaPar1, y=listaPar2)
#fig.update_layout(title_text= collection_name + ': '+ par1 + '/' + par2 +'--- TOTAL DATOS'  )
fig.write_html('first_figure.html', auto_open=True)




