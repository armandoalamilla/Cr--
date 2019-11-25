import pandas as pd


#path = 'csv/100 Sales Records.csv'
#par1 = 'Units Sold'


def mode(path,par1):
    data = pd.read_csv(path)
    data[par1] = data[par1].astype(float)
    #promedio= float(data[columna])
    print('La moda en la columna',par1,'es')
    print(data[par1].mode())

#mode(path,par1)
    


