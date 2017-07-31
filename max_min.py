import numpy as np
import pandas as pd
import itertools
from scipy.signal import argrelextrema
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

def maxmin_target():
    df = pd.read_csv('USDT_BTC.csv')
    df=df['close'].values

    # for local maxima
    max_local = argrelextrema(df, np.greater)

    # for local minima
    min_local= argrelextrema(df, np.less)

    #Convert a Array of Tuples to a list
    max_local = list(itertools.chain.from_iterable(max_local))
    min_local = list(itertools.chain.from_iterable(min_local))

    print('Maxs and Mins')
    print(max_local)
    print(min_local)

    #Adjust array to plot
    aux = []
    aux2 = []
    for i, val in enumerate(max_local):
        aux.append(i)
        aux[i]= df[max_local[i]]

    for i, val in enumerate(min_local):
        aux2.append(i)
        aux2[i]= df[min_local[i]]


    plt.plot(df, c='black', label='Fechamento', linewidth=0.5)
    plt.plot(max_local, aux, c='blue', marker='s', label='Maximos Locais', linestyle="None")
    plt.plot(min_local, aux2, c='red', marker='^', label='Minimos Locais', linestyle="None")
    plt.legend(loc='upper left')



    df = pd.read_csv('USDT_BTC.csv')
    df['target'] = 0

    #Put Max and Min in a column Target
    for i, val in enumerate(max_local):
        df['target'].values[max_local[i]] = 1

    for i, val in enumerate(min_local):
        df['target'].values[min_local[i]] = -1

    df.to_csv('USDT_BTC.csv', index=False)
    plt.show()
