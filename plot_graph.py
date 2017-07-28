from matplotlib import style
style.use('fivethirtyeight')
from matplotlib.finance import candlestick2_ohlc
import matplotlib.pyplot as plt

#Graph Style
style.use('ggplot')

def plot_Avg(df):
    #Create a SubPlot for Moving Averege
    ax1 = plt.subplot2grid((6,1),(0,0),rowspan=5, colspan=1)

    ax2 = plt.subplot2grid((6,1),(5,0),rowspan=1, colspan=1)

    #Plot a Moving Averege
    ax1.plot(df.index, df['close'])
    ax1.plot(df.index, df['fast_mean'])
    ax1.plot(df.index, df['slow_mean'])
    ax2.bar(df.index, df['volume'])



def plot_Exp(df):
    #Create a SubPlot for Moving Averege
    ax1 = plt.subplot2grid((3,3),(0,0), colspan=3)
    ax2 = plt.subplot2grid((3,3),(1,0), colspan=3)
    ax3 = plt.subplot2grid((3, 3), (2, 0), colspan=3)

    #Plot a Moving Averege
    ax1.plot(df.index, df['close'])
    ax1.plot(df.index, df['fast_exp'])
    ax1.plot(df.index, df['slow_exp'])

    ax2.bar(df.index, df['volume'])

    ax3.plot(df.index, df['macd'])
    ax3.plot(df.index, df['zeros'])
    ax3.plot(df.index, df['signal_macd'])
    ax3.plot(df.index, df['signal_macd'])
    ax3.plot(df.index, df['signal_cross'])

    plt.show()




def plot_Candle(df):
    fig, ax = plt.subplots()
    candlestick2_ohlc(ax,df['open'],df['high'],df['low'],df['close'],width=0.5)
    plt.show()