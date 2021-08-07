'''
A lot of technical indicators are used by traders. Here I implement them.
'''

import pandas as pd

def rsi(p = 14, close_prices):
    '''
    Relative Strength Index (RSI) is a momentum indicator that measures the magnitude
    of recent price changes to evaluate overbought or oversold conditions in
    the price of a stock or other asset.

    Displayed as an oscillator, RSI is calculated by the following formula:
    RSI = 100 - (100 / (1 + RS))
    where RS is the average of all up or down price changes for the last 14 periods.

    RS = Average Gain / Average Loss

    Params:
        input_period p = take the average gain in the past input_period days

    '''

    df = pd.DataFrame()
    df['close'] = close_prices
    df['change'] = df['close'].pct_change()

    # Calculate gain and loss columns
    df['gain'] = df['change'].apply(lambda x: 0 if x < 0 else x)
    df['loss'] = df['change'].apply(lambda x: 0 if x > 0 else -x)
    df['gain'] = df['gain'].fillna(0)
    df['loss'] = df['loss'].fillna(0)
    df['gain_avg'] = df['gain'].rolling(p).mean()
    df['loss_avg'] = df['loss'].rolling(p).mean()
    df['rs'] = df['gain_avg'] / df['loss_avg']
    df['rsi'] = 100 - (100 / (1 + df['rs']))
    df['rsi'] = df['rsi'].fillna(0)
    df['rsi'] = df['rsi'].astype(float)

    return df


    