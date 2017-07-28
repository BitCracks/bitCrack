import numpy as np



def delta(df):
    for index, row in df.iterrows():
        df['delta'] = df['close'] - df['open']
        df['percent'] = (df['delta'] / df['open']) * 100
        df['type'] = np.sign(df.close - df.open)

def movAverage(df, fast, slow):
    # Create Moving Averege
    df['fast_mean'] = df['close'].rolling(window=fast).mean()
    df['slow_mean'] = df['close'].rolling(window=slow).mean()

def movExpAvg(df, fast, slow):
    # Create Moving Averege Expo
    df['fast_exp'] =  df['close'].ewm(span=fast, adjust=False).mean()
    df['slow_exp'] =  df['close'].ewm(span=slow, adjust=False).mean()

def MACD(df):
    df['macd'] = df['fast_exp'] - df['slow_exp']

def signal_Macd(df, span):
    df['signal_macd'] = df['macd'].ewm(span=span, adjust=False).mean()

def signal_Cross(df):
    df['signal_cross'] = np.where(df['macd'] > df['signal_macd'], 10, 0)
    df['signal_cross'] = np.where(df['macd'] < df['signal_macd'], -10, df['signal_cross'])