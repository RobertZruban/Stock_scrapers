import numpy as np
import pandas
from pandas_datareader import data as pdr
import yfinance as yfin
yfin.pdr_override()
start = dt.datetime(2020, 1, 1)
data = pdr.get_data_yahoo('AAPL', start)
print(data)
