
import pprint
import random
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from selenium import webdriver  
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.common.keys import Keys  
from bs4 import BeautifulSoup
import pandas as pd
import pyodbc
import sqlalchemy


pp = pprint.PrettyPrinter(indent=4)


conn = pyodbc.connect(
"Driver={SQL Server};"
"Server=DESKTOP-F86F289;"
"Database =Stonks;"
"Trusted_Connection=yes;")
data = pd.read_sql("SELECT TOP(100000) * FROM Stonks.dbo.stocks", conn)

#links = data['Links']

ticker = []
name_df = []
ticker_names = []
for x in data['ticker']:
    ticker.append(x)
for x in data['name_df']:
    ticker_names.append(x)

data_2= pd.read_sql("SELECT TOP(100000) * FROM Stonks.dbo.balance_sheet", conn)
ticker_2 = []
name_df_2 = []
ticker_names_2 = []
for x in data_2['Ticker']:
    ticker_2.append(x)
for x in data_2['Name_df']:
    ticker_names_2.append(x)

ticker_2 = list(set(ticker_2))
ticker = [x for x in ticker if x != ticker_2]

ticker_names_2 = list(set(ticker_names_2))
ticker_names = [x for x in ticker_names if x != ticker_names_2]


df = pd.DataFrame()

dates = []
ticker_df = []
name_df = []

List_of_Balance_sheet = ["Cash On Hand","Receivables","Inventory","Pre-Paid Expenses","Other Current Assets","Total Current Assets","Property, Plant, And Equipment",
"Long-Term Investments","Goodwill And Intangible Assets","Other Long-Term Assets","Total Long-Term Assets","Total Assets","Total Current Liabilities",
"Long Term Debt","Other Non-Current Liabilities","Total Long Term Liabilities","Total Liabilities","Common Stock Net","Retained Earnings (Accumulated Deficit)",
"Comprehensive Income","Other Share Holders Equity","Share Holder Equity","Total Liabilities And Share Holders Equity"]
Cash_On_Hand =[]
Receivables =[]
Inventory =[]
Pre_Paid_Expenses =[]
Other_Current_Assets =[]
Total_Current_Assets =[]
Property_Plant_And_Equipment =[]
Long_Term_Investments =[]
Goodwill_And_Intangible_Assets =[]

Total_Long_Term_Assets =[]
Total_Assets =[]
Total_Current_Liabilities =[]
Long_Term_Debt =[]
Other_Non_Current_Liabilities =[]
Total_Long_Term_Liabilities =[]
Total_Liabilities =[]
Common_Stock_Net =[]
Retained_Earnings_Accumulated_Deficit =[]
Comprehensive_Income =[]
Other_Share_Holders_Equity =[]
Share_Holder_Equity =[]
Other_Long_Term_Assets = []
Total_Liabilities_And_Share_Holders_Equity =[]

ticker_list = []
full_name = []
category = []
revenue = []
count = 0
pff = 0
browser = webdriver.Chrome(r'C:\Users\roboz.DESKTOP-F86F289\Desktop\chromedrive\chromedriver.exe') 

for ticker,name in zip(ticker,ticker_names):
    url2 = "https://www.macrotrends.net/stocks/charts/" + ticker + "/" + name + "/balance-sheet"
    pff = pff + 1
    print(len(ticker_names) - count )
    #if pff == 100:
       # break
            
    browser.get(url2) 
    #time.sleep(2)
    html_source2 = browser.page_source  
    soup = BeautifulSoup(html_source2,'html.parser')
    i = 0
    j = 2
    try:
        for x in soup.findAll('div', {'role' : 'columnheader'}):
            date = soup.findAll('div', {'role' : 'columnheader'})[j].get_text()
            dates.append(date)
            j +=1
    except Exception:
        pass

    try:

        for x in soup.findAll('div', {'role' : 'gridcell'}):
            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[0]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[1]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                i += 1
                Cash_On_Hand.append(point)
                ticker_df.append(ticker)
                name_df.append(name)

            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[1]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[2]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Receivables.append(point)
                i +=1 
            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[2]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[3]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Inventory.append(point)
                i +=1 
            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[3]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[4]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Pre_Paid_Expenses.append(point)
                i +=1  
            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[4]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[5]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Other_Current_Assets.append(point)
                i +=1 
            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[5]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[6]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Total_Current_Assets.append(point)
                i +=1 
            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[6]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[7]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Property_Plant_And_Equipment.append(point)
                i +=1 
            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[7]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[8]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Long_Term_Investments.append(point)
                i +=1 
            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[8]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[9]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Goodwill_And_Intangible_Assets.append(point)
                i +=1 
            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[9]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[10]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Other_Long_Term_Assets.append(point)
                i +=1 

            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[10]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[11]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Total_Long_Term_Assets.append(point)
                i +=1 

                
            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[11]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[12]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Total_Assets.append(point)
                i +=1 
            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[12]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[13]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Total_Current_Liabilities.append(point)
                i +=1 

            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[13]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[14]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Long_Term_Debt.append(point)
                i +=1 
            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[14]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[15]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Other_Non_Current_Liabilities.append(point)
                i +=1 


            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[15]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[16]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Total_Long_Term_Liabilities.append(point)
                i +=1 

            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[16]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[17]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Total_Liabilities.append(point)
                i +=1 

            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[17]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[18]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Common_Stock_Net.append(point)
                i +=1 

            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[18]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[19]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Retained_Earnings_Accumulated_Deficit.append(point)
                i +=1 

            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[19]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[20]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Comprehensive_Income.append(point)
                i +=1 

            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[20]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[21]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Other_Share_Holders_Equity.append(point)
                i +=1 


            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[21]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[22]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Share_Holder_Equity.append(point)
                i +=1
                
            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[22]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[22]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Total_Liabilities_And_Share_Holders_Equity.append(point)
                i +=1 
                if i == 1000:
                    break


    except Exception as e:
        pass

        #df['Ticker'] = Ticker_list

        ##point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
        ##Net_Income_Loss.append(point)
        ##i +=1
df['Date'] = dates
df['Ticker'] = ticker_df
df['Name_df'] = name_df
df["Cash On Hand"] = Cash_On_Hand
df["Receivables"] = Receivables
df["Inventory"] = Inventory
df["Pre-Paid Expenses"] = Pre_Paid_Expenses
df["Other Current Assets"] = Other_Current_Assets
df["Total Current Assets"] = Total_Current_Assets
df["Property Plant And Equipment"] = Property_Plant_And_Equipment
df["Long-Term Investments"] = Long_Term_Investments
df["Goodwill And Intangible Assets"] = Goodwill_And_Intangible_Assets
df["Other Long-Term Assets"] = Other_Long_Term_Assets
df["Total Long-Term Assets"] = Total_Long_Term_Assets
df["Total Assets"] = Total_Assets
df["Total Current Liabilities"] = Total_Current_Liabilities
df["Long Term Debt"] = Long_Term_Debt
df["Other Non-Current Liabilities"] = Other_Non_Current_Liabilities
df["Total Long Term Liabilities"] = Total_Long_Term_Liabilities
df["Total Liabilities"] = Total_Liabilities
df["Common Stock Net"] = Common_Stock_Net
df["Retained Earnings_Accumulated_Deficit"] = Retained_Earnings_Accumulated_Deficit
df["Comprehensive Income"] = Comprehensive_Income
df["Other Share Holders Equity"] = Other_Share_Holders_Equity
df["Share Holder Equity"] = Share_Holder_Equity
df["Total Liabilities And Share Holders Equity"] = Total_Liabilities_And_Share_Holders_Equity


print(df)

df.to_csv(r'C:\Users\roboz.DESKTOP-F86F289\Desktop\Statements\balance_sheet_yearly.csv')
