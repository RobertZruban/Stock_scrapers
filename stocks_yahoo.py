
import yahoo_fin.stock_info as si
import pandas as pd
import plotly.express as px
from tqdm import tqdm

payload=pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
first_table = payload[0]
second_table = payload[1]

df = first_table
symbols = df['Symbol'].values.tolist()
count = 0

ticker_stats = {}
for ticker in symbols:
    try:
        print(len(symbols) - count )
        count += 1
        temp = si.get_stats_valuation(ticker)
        temp = temp.iloc[:,:2]
        temp.columns = ["Attribute", "Recent"]
    except (RuntimeError, TypeError, NameError, KeyError, IndexError, ValueError):
        pass
 
    ticker_stats[ticker] = temp


# combine all the stats valuation tables into a single data frame
df1 = pd.concat(ticker_stats)
df1 = df1.reset_index()
count = 0
del df1["level_1"]

# update column names
df1.columns = ["Ticker", "Attribute", "Recent"]

# Get extra stats
ticker_extra_stats = {}
for ticker in tqdm(symbols)[0:10]:
    try:
        print(len(symbols) - count )
        count += 1
        ticker_extra_stats[ticker] = si.get_stats(ticker)
    except (RuntimeError, TypeError, NameError, KeyError, IndexError, ValueError):
        pass
    

df2 = pd.concat(ticker_extra_stats)

df2 = df2.reset_index()

del df2["level_1"]

df2.columns = ["Ticker", "Attribute", "Value"]

df1_wide = df1.pivot(index = "Ticker", columns="Attribute", values="Recent")
df2_wide = df2.pivot(index = "Ticker", columns="Attribute", values="Value")
count = 0
# Clean up column names to remove footnote indicators
try:
    print(len(symbols) - count )
    count += 1
    df1_wide.rename(columns = {"Enterprise Value 3":"Enterprise Value"}, inplace = True)
    df1_wide.rename(columns = {"Enterprise Value/EBITDA 7":"Enterprise Value/EBITDA"}, inplace = True)
    df1_wide.rename(columns = {"Enterprise Value/Revenue 3":"Enterprise Value/Revenue"}, inplace = True)
    df1_wide.rename(columns = {"Forward P/E 1":"Forward P/E"}, inplace = True)
    df1_wide.rename(columns = {"Market Cap (intraday) 5":"Market Cap (intraday)"}, inplace = True)
    df1_wide.rename(columns = {"PEG Ratio (5 yr expected) 1":"PEG Ratio (5 yr expected)"}, inplace = True)

    df2_wide.rename(columns = {"% Held by Insiders 1":"% Held by Insiders"}, inplace = True)
    df2_wide.rename(columns = {"% Held by Institutions 1":"% Held by Institutions"}, inplace = True)
    df2_wide.rename(columns = {"200-Day Moving Average 3":"200-Day Moving Average"}, inplace = True)
    df2_wide.rename(columns = {"5 Year Average Dividend Yield 4":"5 Year Average Dividend Yield %"}, inplace = True)
    df2_wide.rename(columns = {"50-Day Moving Average 3":"50-Day Moving Average"}, inplace = True)
    df2_wide.rename(columns = {"52 Week High 3":"52 Week High"}, inplace = True)
    df2_wide.rename(columns = {"52 Week Low 3":"52 Week Low"}, inplace = True)
    df2_wide.rename(columns = {"52-Week Change 3":"52-Week Change %"}, inplace = True)
    df2_wide.rename(columns = {"Avg Vol (10 day) 3":"Avg Vol (10 day)"}, inplace = True)
    df2_wide.rename(columns = {"Avg Vol (3 month) 3":"Avg Vol (3 month)"}, inplace = True)
    df2_wide.rename(columns = {"Dividend Date 3":"Dividend Date"}, inplace = True)
    df2_wide.rename(columns = {"Ex-Dividend Date 4":"Ex-Dividend Date"}, inplace = True)
    df2_wide.rename(columns = {"Forward Annual Dividend Rate 4":"Forward Annual Dividend Rate"}, inplace = True)
    df2_wide.rename(columns = {"Forward Annual Dividend Yield 4":"Forward Annual Dividend Yield %"}, inplace = True)
    df2_wide.rename(columns = {"Last Split Date 3":"Last Split Date"}, inplace = True)
    df2_wide.rename(columns = {"Last Split Factor 2":"Last Split Factor"}, inplace = True)
    df2_wide.rename(columns = {"Operating Margin (ttm)":"Operating Margin (ttm) %"}, inplace = True)
    df2_wide.rename(columns = {"Payout Ratio 4":"Payout Ratio %"}, inplace = True)
    df2_wide.rename(columns = {"Profit Margin":"Profit Margin %"}, inplace = True)
    df2_wide.rename(columns = {"Quarterly Earnings Growth (yoy)":"Quarterly Earnings Growth (yoy) %"}, inplace = True)
    df2_wide.rename(columns = {"Quarterly Revenue Growth (yoy)":"Quarterly Revenue Growth (yoy) %"}, inplace = True)
    df2_wide.rename(columns = {"Return on Assets (ttm)":"Return on Assets (ttm) %"}, inplace = True)
    df2_wide.rename(columns = {"Return on Equity (ttm)":"Return on Equity (ttm) %"}, inplace = True)
    df2_wide.rename(columns = {"S&P500 52-Week Change 3":"S&P500 52-Week Change %"}, inplace = True)
    df2_wide.rename(columns = {"Shares Outstanding 5":"Shares Outstanding"}, inplace = True)
    df2_wide.rename(columns = {"Trailing Annual Dividend Rate 3":"Trailing Annual Dividend Rate"}, inplace = True)
    df2_wide.rename(columns = {"Trailing Annual Dividend Yield 3":"Trailing Annual Dividend Yield %"}, inplace = True)
except(RuntimeError, TypeError, NameError, KeyError, IndexError, ValueError):
    pass

# Convert string values to float as necessary
try:
    df1_wide['Trailing P/E'] = df1_wide['Trailing P/E'].astype(float)
    df1_wide['Enterprise Value/EBITDA'] = df1_wide['Enterprise Value/EBITDA'].astype(float)
    df1_wide['Enterprise Value/Revenue'] = df1_wide['Enterprise Value/Revenue'].astype(float)
    df1_wide['Forward P/E'] = df1_wide['Forward P/E'].astype(float)
    df1_wide['PEG Ratio (5 yr expected)'] = df1_wide['PEG Ratio (5 yr expected)'].astype(float)
    df1_wide['Price/Book (mrq)'] = df1_wide['Price/Book (mrq)'].astype(float)
    df1_wide['Price/Sales (ttm)'] = df1_wide['Price/Sales (ttm)'].astype(float)

    df2_wide['% Held by Insiders'] = df2_wide['% Held by Insiders'].str.strip('%').astype('float') / 100.0
    df2_wide['% Held by Institutions'] = df2_wide['% Held by Institutions'].str.strip('%').astype('float') / 100.0
    df2_wide['5 Year Average Dividend Yield %'] = df2_wide['5 Year Average Dividend Yield %'].astype(float) / 100.0
    df2_wide['50-Day Moving Average'] = df2_wide['50-Day Moving Average'].astype(float)
    df2_wide['52 Week High'] = df2_wide['52 Week High'].astype(float)
    df2_wide['52 Week Low'] = df2_wide['52 Week Low'].astype(float)
    df2_wide['52-Week Change %'] = df2_wide['52-Week Change %'].str.strip('%').astype('float') / 100.0
    df2_wide['Beta (5Y Monthly)'] = df2_wide['Beta (5Y Monthly)'].astype(float)
    df2_wide['Book Value Per Share (mrq)'] = df2_wide['Book Value Per Share (mrq)'].astype(float)
    df2_wide['Current Ratio (mrq)'] = df2_wide['Current Ratio (mrq)'].astype(float)
    df2_wide['Diluted EPS (ttm)'] = df2_wide['Diluted EPS (ttm)'].astype(float)
    df2_wide['Forward Annual Dividend Rate'] = df2_wide['Forward Annual Dividend Rate'].astype(float)
    df2_wide['Forward Annual Dividend Yield %'] = df2_wide['Forward Annual Dividend Yield %'].str.strip('%').astype('float') / 100.0
    df2_wide['Operating Margin (ttm) %'] = df2_wide['Operating Margin (ttm) %'].str.strip('%').astype('float') / 100.0
    df2_wide['Payout Ratio %'] = df2_wide['Payout Ratio %'].str.strip('%').astype('float') / 100.0
    df2_wide['Profit Margin %'] = df2_wide['Profit Margin %'].str.strip('%').astype('float') / 100.0
    df2_wide['Quarterly Earnings Growth (yoy) %'] = df2_wide['Quarterly Earnings Growth (yoy) %'].str.strip('%').astype('float') / 100.0
    df2_wide['Quarterly Revenue Growth (yoy) %'] = df2_wide['Quarterly Revenue Growth (yoy) %'].str.strip('%').astype('float') / 100.0
    df2_wide['Return on Assets (ttm) %'] = df2_wide['Return on Assets (ttm) %'].str.strip('%').astype('float') / 100.0
    df2_wide['Return on Equity (ttm) %'] = df2_wide['Return on Equity (ttm) %'].str.strip('%').astype('float') / 100.0
    df2_wide['Revenue Per Share (ttm)'] = df2_wide['Revenue Per Share (ttm)'].astype(float)
    df2_wide['S&P500 52-Week Change %'] = df2_wide['S&P500 52-Week Change %'].str.strip('%').astype('float') / 100.0
    df2_wide['Total Cash Per Share (mrq)'] = df2_wide['Total Cash Per Share (mrq)'].astype(float)
    df2_wide['Total Debt/Equity (mrq)'] = df2_wide['Total Debt/Equity (mrq)'].astype(float)
    df2_wide['Trailing Annual Dividend Rate'] = df2_wide['Trailing Annual Dividend Rate'].astype(float)
    df2_wide['Trailing Annual Dividend Yield %'] = df2_wide['Trailing Annual Dividend Yield %'].str.strip('%').astype('float') / 100.0
    df2_wide['200-Day Moving Average'] = df2_wide['200-Day Moving Average'].astype(float)
except(RuntimeError, TypeError, NameError, KeyError, IndexError, ValueError):
    pass
# Merge the dataframes into company_data

lol = pd.DataFrame()
flow_all = []
balance_all = []
income_all = []

for x in symbols:
    print("starting" + x)
    try:
        balance_sheet = si.get_balance_sheet(x, yearly=False)
        ticker_name_balance_sheet = [x]*len(balance_sheet.index)
        balance_sheet.insert(0,'ticker', ticker_name_balance_sheet)
        #balance_all.append(balance_sheet)
       
        balance_sheet_yearly = si.get_balance_sheet(x)
        ticker_name_balance_sheet_yearly = [x]*len(balance_sheet_yearly.index)
        balance_sheet_yearly.insert(0,'ticker', ticker_name_balance_sheet_yearly)
        #balance_all.append(balance_sheet_yearly)


        income = si.get_income_statement(x, yearly=False)
        ticker_name_income = [x]*len(income.index)
        income.insert(0,'ticker',ticker_name_income )
        #income_all.append(income)

        
        income_yearly = si.get_income_statement(x)
        ticker_name_income_yearly = [x]*len(income_yearly.index)
        income_yearly.insert(0,'ticker',ticker_name_income_yearly )
        #income_all.append(income_yearly)



        flow = si.get_cash_flow(x, yearly=False)
        ticker_name_flow = [x]*len(flow.index)
        #flow.insert(0,'ticker',ticker_name_flow )

        flow_yearly = si.get_cash_flow(x)
        ticker_name_flow_yearly = [x]*len(flow_yearly.index)
        flow_yearly.insert(0,'ticker',ticker_name_flow_yearly )
        #flow_all.append(flow_yearly)

        result = balance_sheet.append(balance_sheet_yearly)
        result = result.append(income)
        result = result.append(income_yearly)
        result = result.append(flow)
        result = result.append(flow_yearly)

        #lol.append(balance_sheet)
        #lol.append(income)
        #lol.append(flow)
        print("finishing" + x)
    except (RuntimeError, TypeError, NameError, KeyError, IndexError, ValueError):
        pass
i = 0    
for x in symbols[1:]:
    print("starting" + x)
    print(len(symbols)-i)
    try:
        balance_sheet = si.get_balance_sheet(x, yearly=False)
        ticker_name_balance_sheet = [x]*len(balance_sheet.index)
        balance_sheet.insert(0,'ticker', ticker_name_balance_sheet)
        #balance_all.append(balance_sheet)
       
        balance_sheet_yearly = si.get_balance_sheet(x)
        ticker_name_balance_sheet_yearly = [x]*len(balance_sheet_yearly.index)
        balance_sheet_yearly.insert(0,'ticker', ticker_name_balance_sheet_yearly)


        income = si.get_income_statement(x, yearly=False)
        ticker_name_income = [x]*len(income.index)
        income.insert(0,'ticker',ticker_name_income )
        #income_all.append(income)

        income_yearly = si.get_income_statement(x)
        ticker_name_income_yearly = [x]*len(income_yearly.index)
        income_yearly.insert(0,'ticker',ticker_name_income_yearly )
        #income_all.append(income_yearly)


        flow = si.get_cash_flow(x, yearly=False)
        ticker_name_flow = [x]*len(flow.index)
        flow.insert(0,'ticker',ticker_name_flow )
        #flow_all.append(flow)


        flow_yearly = si.get_cash_flow(x)
        ticker_name_flow_yearly = [x]*len(flow_yearly.index)
        flow_yearly.insert(0,'ticker',ticker_name_flow_yearly )
        #flow_all.append(flow_yearly)
             
        result = result.append(balance_sheet)
        result = result.append(balance_sheet_yearly)

        result = result.append(income)
        result = result.append(income_yearly)
        
        result = result.append(flow)
        result = result.append(flow_yearly)

        #lol.append(balance_sheet)
        #lol.append(income)
        #lol.append(flow)
        print("finishing" + x)
    except (RuntimeError, TypeError, NameError, KeyError, IndexError, ValueError):
        pass
        #df.to_csv(r'C:\Users\roboz\Desktop\Stocks\stocks4.csv')
        #balance_sheet
    #balance_sheet

result.to_csv(r'C:\Users\roboz.DESKTOP-F86F289\Desktop\Statements\stocks_yahoo\Stock_final_final.csv')
df.to_csv(r'C:\Users\roboz.DESKTOP-F86F289\Desktop\Statements\stocks_yahoo\df.csv')
df1.to_csv(r'C:\Users\roboz.DESKTOP-F86F289\Desktop\Statements\stocks_yahoo\df1.csv')
df1_wide.to_csv(r'C:\Users\roboz.DESKTOP-F86F289\Desktop\Statements\stocks_yahoo\df1_wide.csv')
df2.to_csv(r'C:\Users\roboz.DESKTOP-F86F289\Desktop\Statements\stocks_yahoo\df2.csv')
df2_wide.to_csv(r'C:\Users\roboz.DESKTOP-F86F289\Desktop\Statements\stocks_yahoo\df2_wide.csv')
first_table.to_csv(r'C:\Users\roboz.DESKTOP-F86F289\Desktop\Statements\stocks_yahoo\first_table.csv')

