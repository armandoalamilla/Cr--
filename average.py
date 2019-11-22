import pandas as pd
import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

collection_name = 'SalesRevenue'
BD = 'Cr--'
mydb = myclient[BD]
mycol = mydb[collection_name]

data = pd.DataFrame(list(mycol.find()))
columna = 'Total Revenue'
#promedio= float(data[columna])
data[columna] = data[columna].astype(float)

print('El promedio de la columna',columna,'es',data[columna].mean())
