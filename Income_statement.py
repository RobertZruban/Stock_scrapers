
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

df = pd.DataFrame()
List_of_Balance_sheet = ["Revenue","Cost Of Goods Sold","Gross Profit","Research And Development Expenses","SG&A Expenses","Other Operating Income Or Expenses","Operating Expenses","Operating Income","Total Non-Operating Income/Expense","Pre-Tax Income","Income Taxes","Income After Taxes","Other Income","Income From Continuous Operations","Income From Discontinued Operations","Net Income","EBITDA","EBIT","Basic Shares Outstanding","Shares Outstanding","Basic EPS","EPS - Earnings Per Share"]

dates = []
ticker_df = []
name_df = []

Revenue =[]
Cost_Of_Goods_Sold =[]
Gross_Profit =[]
Research_And_Development_Expenses =[]
SGA_Expenses =[]
Other_Operating_Income_or_Expenses =[]
Operating_Expenses =[]
Operating_Income =[]
Total_Non_Operating_Income_Expense =[]
Pre_Tax_Income =[]
Income_Taxes =[]
Income_After_Taxes =[]
Other_Income =[]
Income_From_Continuous_Operations =[]
Income_From_Discontinued_Operations =[]
Net_Income =[]
EBITDA =[]
EBIT =[]
Basic_Shares_Outstanding =[]
Shares_Outstanding =[]
Basic_EPS =[]
EPS_Earning_Per_Share =[]
Net_Common_Equity_Issued_Repurchased = []
Net_Total_Equity_Issued_Repurchased =[]
Total_Common_And_Preferred_Stock_Dividends_Paid = []
Financial_Activities_Other = []
Cash_Flow_From_Financial_Activities = []
Net_Cash_Flow = []
Stock_Based_Compensation = []
Common_Stock_Dividends_Paid = []
###ticker_list = ["MMM","AOS","ABT","ABBV","ABMD","ACN","ATVI","ADM","ADBE","ADP","AAP","AES","AFL","A","AIG","APD","AKAM","ALK","ALB","ARE","ALGN","ALLE","LNT","ALL","GOOGL","GOOG","MO","AMZN","AMCR","AMD","AEE","AAL","AEP","AXP","AMT","AWK","AMP","ABC","AME","AMGN","APH","ADI","ANSS","ANTM","AON","APA","AAPL","AMAT","APTV","ANET","AIZ","T","ATO","ADSK","AZO","AVB","AVY","BKR","BLL","BAC","BBWI","BAX","BDX","WRB","BRK.B","BBY","BIO","TECH","BIIB","BLK","BK","BA","BKNG","BWA","BXP","BSX","BMY","AVGO","BR","BRO","BF.B","CHRW","CDNS","CZR","CPT","CPB","COF","CAH","KMX","CCL","CARR","CTLT","CAT","CBOE","CBRE","CDW","CE","CNC","CNP","CDAY","CERN","CF","CRL","SCHW","CHTR","CVX","CMG","CB","CHD","CI","CINF","CTAS","CSCO","C","CFG","CTXS","CLX","CME","CMS","KO","CTSH","CL","CMCSA","CMA","CAG","COP","ED","STZ","CEG","COO","CPRT","GLW","CTVA","COST","CTRA","CCI","CSX","CMI","CVS","DHI","DHR","DRI","DVA","DE","DAL","XRAY","DVN","DXCM","FANG","DLR","DFS","DISCA","DISCK","DISH","DIS","DG","DLTR","D","DPZ","DOV","DOW","DTE","DUK","DRE","DD","DXC","EMN","ETN","EBAY","ECL","EIX","EW","EA","EMR","ENPH","ETR","EOG","EPAM","EFX","EQIX","EQR","ESS","EL","ETSY","RE","EVRG","ES","EXC","EXPE","EXPD","EXR","XOM","FFIV","FDS","FAST","FRT","FDX","FITB","FRC","FE","FIS","FISV","FLT","FMC","F","FTNT","FTV","FBHS","FOXA","FOX","BEN","FCX","AJG","GRMN","IT","GE","GNRC","GD","GIS","GPC","GILD","GL","GPN","GM","GS","GWW","HAL","HIG","HAS","HCA","PEAK","HSIC","HSY","HES","HPE","HLT","HOLX","HD","HON","HRL","HST","HWM","HPQ","HUM","HII","HBAN","IEX","IDXX","ITW","ILMN","INCY","IR","INTC","ICE","IBM","IP","IPG","IFF","INTU","ISRG","IVZ","IPGP","IQV","IRM","JBHT","JKHY","J","JNJ","JCI","JPM","JNPR","K","KEY","KEYS","KMB","KIM","KMI","KLAC","KHC","KR","LHX","LH","LRCX","LW","LVS","LDOS","LEN","LLY","LNC","LIN","LYV","LKQ","LMT","L","LOW","LUMN","LYB","MTB","MRO","MPC","MKTX","MAR","MMC","MLM","MAS","MA","MTCH","MKC","MCD","MCK","MDT","MRK","FB","MET","MTD","MGM","MCHP","MU","MSFT","MAA","MRNA","MHK","MOH","TAP","MDLZ","MPWR","MNST","MCO","MS","MOS","MSI","MSCI","NDAQ","NTAP","NFLX","NWL","NEM","NWSA","NWS","NEE","NLSN","NKE","NI","NDSN","NSC","NTRS","NOC","NLOK","NCLH","NRG","NUE","NVDA","NVR","NXPI","ORLY","OXY","ODFL","OMC","OKE","ORCL","OGN","OTIS","PCAR","PKG","PARA","PH","PAYX","PAYC","PYPL","PENN","PNR","PEP","PKI","PFE","PM","PSX","PNW","PXD","PNC","POOL","PPG","PPL","PFG","PG","PGR","PLD","PRU","PEG","PTC","PSA","PHM","PVH","QRVO","PWR","QCOM","DGX","RL","RJF","RTX","O","REG","REGN","RF","RSG","RMD","RHI","ROK","ROL","ROP","ROST","RCL","SPGI","CRM","SBAC","SLB","STX","SEE","SRE","NOW","SHW","SBNY","SPG","SWKS","SJM","SNA","SEDG","SO","LUV","SWK","SBUX","STT","STE","SYK","SIVB","SYF","SNPS","SYY","TMUS","TROW","TTWO","TPR","TGT","TEL","TDY","TFX","TER","TSLA","TXN","TXT","TMO","TJX","TSCO","TT","TDG","TRV","TRMB","TFC","TWTR","TYL","TSN","USB","UDR","ULTA","UAA","UA","UNP","UAL","UNH","UPS","URI","UHS","VLO","VTR","VRSN","VRSK","VZ","VRTX","VFC","VTRS","V","VNO","VMC","WAB","WMT","WBA","WM","WAT","WEC","WFC","WELL","WST","WDC","WRK","WY","WHR","WMB","WTW","WYNN","XEL","XYL","YUM","ZBRA","ZBH","ZION","ZTS"]
#browser.find_element_by_class_name("relative inline-flex items-center whitespace-nowrap rounded-md border border-gray-300 bg-white px-1 py-1.5 font-medium text-gray-700 hover:bg-gray-50 xs:px-1.5 xs:py-2 sm:px-4").click()
ticker_list = []
full_name = []
category = []
revenue = []
count = 0
pff = 0
browser = webdriver.Chrome(r'C:\Users\roboz.DESKTOP-F86F289\Desktop\chromedrive\chromedriver.exe') 

for ticker,name in zip(ticker,ticker_names):
    print(len(ticker_names) - count )
    url2 = "https://www.macrotrends.net/stocks/charts/" + ticker + "/" + name + "/income-statement"
    pff = pff + 1
    ##if pff == 10:
        ##break
            
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
                #print("here")
                i += 1
                Revenue.append(point)
                ticker_df.append(ticker)
                name_df.append(name)

            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[1]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[2]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Cost_Of_Goods_Sold.append(point)
                i +=1 
            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[2]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[3]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Gross_Profit.append(point)
                i +=1 
            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[3]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[4]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Research_And_Development_Expenses.append(point)
                i +=1  
            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[4]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[5]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                SGA_Expenses.append(point)
                i +=1 
            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[5]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[6]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Other_Operating_Income_or_Expenses.append(point)
                i +=1 
            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[6]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[7]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Operating_Expenses.append(point)
                i +=1 
            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[7]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[8]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Operating_Income.append(point)
                i +=1 
            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[8]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[9]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Total_Non_Operating_Income_Expense.append(point)
                i +=1 
            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[9]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[10]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Pre_Tax_Income.append(point)
                i +=1 

            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[10]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[11]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Income_Taxes.append(point)
                i +=1 


            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[11]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[12]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Income_After_Taxes.append(point)
                i +=1 
            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[12]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[13]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Other_Income.append(point)
                i +=1 

            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[13]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[14]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Income_From_Continuous_Operations.append(point)
                i +=1 
            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[14]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[15]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Income_From_Discontinued_Operations.append(point)
                i +=1 


            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[15]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[16]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Net_Income.append(point)
                i +=1 

            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[16]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[17]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                EBITDA.append(point)
                i +=1 

            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[17]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[18]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                EBIT.append(point)
                i +=1 

            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[18]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[19]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Basic_Shares_Outstanding.append(point)

                i +=1 

            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[19]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[20]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Shares_Outstanding.append(point)
                i +=1

            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[20]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[21]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Basic_EPS.append(point)
                i +=1 
            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[21]:
                print('lol')
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[22]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                EPS_Earning_Per_Share.append(point)    
                i +=1 
                if i == 1000:
                    break

    except Exception as e:
        pass

        #df['Ticker'] = Ticker_list

        ##point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
        ##Net_Income_Loss.append(point)
        ##i +=1
try:
    df['Date'] = dates
    df['Ticker'] = ticker_df
    df['name_df'] = name_df
    df["Revenue"] = Revenue
    df["Cost_Of_Goods_Sold"] = Cost_Of_Goods_Sold
    df["Gross_Profit"] = Gross_Profit
    df["Research_And_Development_Expenses"] = Research_And_Development_Expenses
    df["SGA_Expenses"] = SGA_Expenses
    df["Other_Operating_Income_or_Expenses"] = Other_Operating_Income_or_Expenses
    df["Operating_Expenses"] = Operating_Expenses
    df["Operating_Income"] = Operating_Income
    df["Total_Non-Operating_Income_Expense"] = Total_Non_Operating_Income_Expense
    df["Pre_Tax_Income"] = Pre_Tax_Income
    df["Income_Taxes"] = Income_Taxes
    df["Income_After_Taxes"] = Income_After_Taxes
    df["Other_Income"] = Other_Income
    df["Income_From_Continuous_Operations"] = Income_From_Continuous_Operations
    df["Income_From_Discontinued_Operations"] = Income_From_Discontinued_Operations
    df["Net_Income"] = Net_Income
    df["EBITDA"] = EBITDA
    df["EBIT"] = EBIT
    df["Basic_Shares_Outstanding"] = Basic_Shares_Outstanding
    df["Shares_Outstanding"] = Shares_Outstanding
    df["Basic_EPS"] = Basic_EPS
    df["EPS_Earning_Per_Share"] = EPS_Earning_Per_Share

except Exception as e:
    pass

print(df)

df.to_csv(r'C:\Users\roboz.DESKTOP-F86F289\Desktop\Statements\income_statement_2.csv')
