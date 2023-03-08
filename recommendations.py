import requests
import pandas as pd 
from yahoo_fin import stock_info as si 
from pandas_datareader import DataReader
import numpy as np

tickers = si.tickers_sp500()
recommendations = []

for ticker in tickers:
    lhs_url = 'https://query2.finance.yahoo.com/v10/finance/quoteSummary/'
    rhs_url = '?formatted=true&crumb=swg7qs5y9UP&lang=en-US&region=US&' \
              'modules=upgradeDowngradeHistory,recommendationTrend,' \
              'financialData,earningsHistory,earningsTrend,industryTrend&' \
              'corsDomain=finance.yahoo.com'
    
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    url =  lhs_url + ticker + rhs_url
    r = requests.get(url, headers=headers)
    if not r.ok:
        recommendation = 6
    try:
        result = r.json()['quoteSummary']['result'][0]
        recommendation =result['financialData']['recommendationMean']['fmt']
    except:
        recommendation = 6
    
    recommendations.append(recommendation)
    
    print("--------------------------------------------")
    print ("{} has an average recommendation of: ".format(ticker), recommendation)
    #time.sleep(0.5)
    
dataframe = pd.DataFrame(list(zip(tickers, recommendations)), columns =['Company', 'Recommendations']) 
dataframe = dataframe.set_index('Company')
dataframe.to_csv(r'C:\Users\roboz.DESKTOP-F86F289\Desktop\Statements\Python_try\recommendations.csv')

print (dataframe)