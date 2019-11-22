import pandas as pd
import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

collection_name = 'SalesRevenue'
BD = 'Cr--'
columna = 'Units Sold'
mydb = myclient[BD]
mycol = mydb[collection_name]

data = pd.DataFrame(list(mycol.find()))

#promedio= float(data[columna])
data[columna] = data[columna].astype(float)

print('La moda de en la columna',columna,'es')
print(data[columna].mode())
