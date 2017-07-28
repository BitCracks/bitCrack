import numpy as np
import pandas as pd
from scipy.signal import argrelextrema
from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt


df = pd.read_csv('USDT_BTC.csv')
df=df['close'].values

# for local maxima
max_local = argrelextrema(df, np.greater)
print(max_local)


# for local minima
min_local= argrelextrema(df, np.less)
print(min_local)


plt.plot(max_local, c='blue', marker='s', ms=8, label='Maximos Locais')
plt.plot(min_local, c='red', marker='^', ms=8, label='Minimos Locais')
plt.show()