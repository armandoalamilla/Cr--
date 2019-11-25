import numpy as np
from scipy.stats import norm
import pandas as pd
import scipy.stats as stats
import pylab as pl


#path = 'csv/appleStocks.csv'
#par2 = 'AAPL.Open'


def distN(path,par2):
    data = pd.read_csv(path)
    data[par2] = data[par2].astype(float)
    data[par2] = data[par2].sort_values()
    fit = stats.norm.pdf(data[par2], np.mean(data[par2]), np.std(data[par2]))  
    pl.plot(data[par2],fit,'-o')
    pl.hist(data[par2],density=True)     
    pl.title(path + ' / ' + ' ' +  par2 + ' DIST NORMAL')
    pl.show()

#distN(path,par2)




