import pandas as pd
import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

collection_name = 'SalesRevenue'
BD = 'Cr--'
columna = 'Total Profit'
mydb = myclient[BD]
mycol = mydb[collection_name]

data = pd.DataFrame(list(mycol.find()))

#promedio= float(data[columna])
data[columna] = data[columna].astype(float)

print('La mediana de la columna',columna,'es',data[columna].median())
