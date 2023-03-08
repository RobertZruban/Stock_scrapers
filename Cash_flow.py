
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




List_of_Balance_sheet = ['Net Income/Loss','Total Depreciation And Amortization - Cash Flow','Other Non-Cash Items',
                        'Total Non-Cash Items','Change In Accounts Receivable', 'Change In Inventories', 'Change In Accounts Payable',
                         'Change In Assets/Liabilities', 'Total Change In Assets/Liabilities', 'Cash Flow From Operating Activities',
                         'Net Change In Property, Plant, And Equipment', 'Net Change In Intangible Assets', 
                         'Net Acquisitions/Divestitures',
                        'Net Change In Short-term Investments','Net Change In Long-Term Investments',
                        'Net Change In Investments - Total','Investing Activities - Other',
                        'Cash Flow From Investing Activities','Net Long-Term Debt',
                        'Net Current Debt','Debt Issuance/Retirement Net - Total',
                         'Net Common Equity Issued/Repurchased','Net Total Equity Issued/Repurchased','Total Common And Preferred Stock Dividends Paid',
                         'Financial Activities - Other','Cash Flow From Financial Activities',
                         'Net Cash Flow','Stock-Based Compensation','Common Stock Dividends Paid'            
                        ]
dates = []
ticker_df = []

Net_Income_Loss = []
Depreciation_Amortizaton = []
Other_Non_Cash_Items = []
Total_Non_Cash_Items = []
Change_In_Accounts_Receivable = []
Change_In_Inventories = []
Change_In_Accounts_Payable = []
Change_In_Assets_Liabilities = []
Total_Change_In_Assets_Liabilities = []
Cash_Flow_From_Operating_Activities = []
Net_Change_In_Property_Plant_And_Equipment = []
Net_Change_In_Intangible_Assets = []
Net_Acquisitions_Divestitures = []
Net_Change_In_Short_term_Investments = []
Net_Change_In_Long_Term_Investments = []
Net_Change_In_Investments_Total = []
Investing_Activities_Other = []
Cash_Flow_From_Investing_Activities = []
Net_Long_Term_Debt = []
Net_Current_Debt = []
Debt_Issuance_Retirement_Net_Total = []
Net_Common_Equity_Issued_Repurchased = []
Net_Total_Equity_Issued_Repurchased =[]
Total_Common_And_Preferred_Stock_Dividends_Paid = []
Financial_Activities_Other = []
Cash_Flow_From_Financial_Activities = []
Net_Cash_Flow = []
Stock_Based_Compensation = []
Common_Stock_Dividends_Paid = []
####ticker_list = ["MMM","AOS","ABT","ABBV","ABMD","ACN","ATVI","ADM","ADBE","ADP","AAP","AES","AFL","A","AIG","APD","AKAM","ALK","ALB","ARE","ALGN","ALLE","LNT","ALL","GOOGL","GOOG","MO","AMZN","AMCR","AMD","AEE","AAL","AEP","AXP","AMT","AWK","AMP","ABC","AME","AMGN","APH","ADI","ANSS","ANTM","AON","APA","AAPL","AMAT","APTV","ANET","AIZ","T","ATO","ADSK","AZO","AVB","AVY","BKR","BLL","BAC","BBWI","BAX","BDX","WRB","BRK.B","BBY","BIO","TECH","BIIB","BLK","BK","BA","BKNG","BWA","BXP","BSX","BMY","AVGO","BR","BRO","BF.B","CHRW","CDNS","CZR","CPT","CPB","COF","CAH","KMX","CCL","CARR","CTLT","CAT","CBOE","CBRE","CDW","CE","CNC","CNP","CDAY","CERN","CF","CRL","SCHW","CHTR","CVX","CMG","CB","CHD","CI","CINF","CTAS","CSCO","C","CFG","CTXS","CLX","CME","CMS","KO","CTSH","CL","CMCSA","CMA","CAG","COP","ED","STZ","CEG","COO","CPRT","GLW","CTVA","COST","CTRA","CCI","CSX","CMI","CVS","DHI","DHR","DRI","DVA","DE","DAL","XRAY","DVN","DXCM","FANG","DLR","DFS","DISCA","DISCK","DISH","DIS","DG","DLTR","D","DPZ","DOV","DOW","DTE","DUK","DRE","DD","DXC","EMN","ETN","EBAY","ECL","EIX","EW","EA","EMR","ENPH","ETR","EOG","EPAM","EFX","EQIX","EQR","ESS","EL","ETSY","RE","EVRG","ES","EXC","EXPE","EXPD","EXR","XOM","FFIV","FDS","FAST","FRT","FDX","FITB","FRC","FE","FIS","FISV","FLT","FMC","F","FTNT","FTV","FBHS","FOXA","FOX","BEN","FCX","AJG","GRMN","IT","GE","GNRC","GD","GIS","GPC","GILD","GL","GPN","GM","GS","GWW","HAL","HIG","HAS","HCA","PEAK","HSIC","HSY","HES","HPE","HLT","HOLX","HD","HON","HRL","HST","HWM","HPQ","HUM","HII","HBAN","IEX","IDXX","ITW","ILMN","INCY","IR","INTC","ICE","IBM","IP","IPG","IFF","INTU","ISRG","IVZ","IPGP","IQV","IRM","JBHT","JKHY","J","JNJ","JCI","JPM","JNPR","K","KEY","KEYS","KMB","KIM","KMI","KLAC","KHC","KR","LHX","LH","LRCX","LW","LVS","LDOS","LEN","LLY","LNC","LIN","LYV","LKQ","LMT","L","LOW","LUMN","LYB","MTB","MRO","MPC","MKTX","MAR","MMC","MLM","MAS","MA","MTCH","MKC","MCD","MCK","MDT","MRK","FB","MET","MTD","MGM","MCHP","MU","MSFT","MAA","MRNA","MHK","MOH","TAP","MDLZ","MPWR","MNST","MCO","MS","MOS","MSI","MSCI","NDAQ","NTAP","NFLX","NWL","NEM","NWSA","NWS","NEE","NLSN","NKE","NI","NDSN","NSC","NTRS","NOC","NLOK","NCLH","NRG","NUE","NVDA","NVR","NXPI","ORLY","OXY","ODFL","OMC","OKE","ORCL","OGN","OTIS","PCAR","PKG","PARA","PH","PAYX","PAYC","PYPL","PENN","PNR","PEP","PKI","PFE","PM","PSX","PNW","PXD","PNC","POOL","PPG","PPL","PFG","PG","PGR","PLD","PRU","PEG","PTC","PSA","PHM","PVH","QRVO","PWR","QCOM","DGX","RL","RJF","RTX","O","REG","REGN","RF","RSG","RMD","RHI","ROK","ROL","ROP","ROST","RCL","SPGI","CRM","SBAC","SLB","STX","SEE","SRE","NOW","SHW","SBNY","SPG","SWKS","SJM","SNA","SEDG","SO","LUV","SWK","SBUX","STT","STE","SYK","SIVB","SYF","SNPS","SYY","TMUS","TROW","TTWO","TPR","TGT","TEL","TDY","TFX","TER","TSLA","TXN","TXT","TMO","TJX","TSCO","TT","TDG","TRV","TRMB","TFC","TWTR","TYL","TSN","USB","UDR","ULTA","UAA","UA","UNP","UAL","UNH","UPS","URI","UHS","VLO","VTR","VRSN","VRSK","VZ","VRTX","VFC","VTRS","V","VNO","VMC","WAB","WMT","WBA","WM","WAT","WEC","WFC","WELL","WST","WDC","WRK","WY","WHR","WMB","WTW","WYNN","XEL","XYL","YUM","ZBRA","ZBH","ZION","ZTS"]

ticker_list = []
full_name = []
category = []
revenue = []
count = 0
pff = 0
browser = webdriver.Chrome(r'C:\Users\roboz.DESKTOP-F86F289\Desktop\chromedrive\chromedriver.exe') 
#browser.find_element_by_class_name("relative inline-flex items-center whitespace-nowrap rounded-md border border-gray-300 bg-white px-1 py-1.5 font-medium text-gray-700 hover:bg-gray-50 xs:px-1.5 xs:py-2 sm:px-4").click()
for ticker,name in zip(ticker,ticker_names):
    print(len(ticker_names) - count )
    url2 = "https://www.macrotrends.net/stocks/charts/" + ticker + "/" + name + "/cash-flow-statement"
    pff = pff + 1
    ##if pff == 20:
        ##break
    count += 1        
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
                Net_Income_Loss.append(point)
                ticker_df.append(ticker)
                name_df.append(name)

            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[1]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[2]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Depreciation_Amortizaton.append(point)
                i +=1 
            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[2]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[3]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Other_Non_Cash_Items.append(point)
                i +=1 

            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[3]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[4]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Total_Non_Cash_Items.append(point)
                i +=1 


            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[4]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[5]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Change_In_Accounts_Receivable.append(point)
                i +=1 

            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[5]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[6]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Change_In_Inventories.append(point)
                i +=1 

            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[6]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[7]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Change_In_Accounts_Payable.append(point)
                i +=1 

            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[7]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[8]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Change_In_Assets_Liabilities.append(point)
                i +=1 

            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[8]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[9]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Total_Change_In_Assets_Liabilities.append(point)
                i +=1 


            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[9]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[10]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Cash_Flow_From_Operating_Activities.append(point)
                i +=1 
            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[10]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[11]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Net_Change_In_Property_Plant_And_Equipment.append(point)
                i +=1 

            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[11]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[12]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Net_Change_In_Intangible_Assets.append(point)
                i +=1 

            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[12]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[13]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Net_Acquisitions_Divestitures.append(point)
                i +=1 


            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[13]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[14]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Net_Change_In_Short_term_Investments.append(point)
                i +=1 

            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[14]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[15]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Net_Change_In_Long_Term_Investments.append(point)
                i +=1 

            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[15]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[16]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Net_Change_In_Investments_Total.append(point)
                i +=1 

            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[16]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[17]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Investing_Activities_Other.append(point)
                i +=1 

            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[17]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[18]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Cash_Flow_From_Investing_Activities.append(point)
                i +=1 


            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[18]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[19]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Net_Long_Term_Debt.append(point)
                i +=1 


            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[19]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[20]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Net_Current_Debt.append(point)
                i +=1 

            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[20]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[21]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Debt_Issuance_Retirement_Net_Total.append(point)
                i +=1 

            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[21]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[22]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Net_Common_Equity_Issued_Repurchased.append(point)
                i +=1 

            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[22]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[23]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Net_Total_Equity_Issued_Repurchased.append(point)

                i +=1 

            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[23]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[24]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()

                Total_Common_And_Preferred_Stock_Dividends_Paid.append(point)
                i +=1 

            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[24]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[25]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Financial_Activities_Other.append(point)

                i +=1 

            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[25]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[26]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()

                Cash_Flow_From_Financial_Activities.append(point)
                i +=1 

            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[26]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[27]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Net_Cash_Flow.append(point)

                i +=1 

            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[27]:
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[28]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()

                Stock_Based_Compensation.append(point)
                i +=1 
                #if i ==500:
                    #break


            if soup.findAll('div', {'role' : 'gridcell'})[i].get_text() == List_of_Balance_sheet[28]:
                print(i)
                i += 2
            while soup.findAll('div', {'role' : 'gridcell'})[i].get_text() != List_of_Balance_sheet[28]:
                point = soup.findAll('div', {'role' : 'gridcell'})[i].get_text()
                Common_Stock_Dividends_Paid.append(point)
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
    df['Net Income/Loss'] = Net_Income_Loss
    df['Total Depreciation And Amortization - Cash Flow'] = Depreciation_Amortizaton
    df['Other Non-Cash Items'] = Other_Non_Cash_Items
    df['Total Non-Cash Items'] = Total_Non_Cash_Items
    df['Change In Accounts Receivable'] = Change_In_Accounts_Receivable
    df['Change In Inventories'] = Change_In_Inventories
    df['Change In Accounts Payable'] = Change_In_Accounts_Payable
    df['Change In Assets/Liabilities'] =Change_In_Assets_Liabilities
    df['Total Change In Assets/Liabilities'] = Total_Change_In_Assets_Liabilities
    df['Cash_Flow_From_Operating_Activities'] = Cash_Flow_From_Operating_Activities
    df['Net Change In Property, Plant, And Equipment'] = Net_Change_In_Property_Plant_And_Equipment
    df['Net Change In Intangible Assets'] = Net_Change_In_Intangible_Assets
    df['Net Acquisitions/Divestitures'] = Net_Acquisitions_Divestitures
    df['Net Change In Short-term Investments'] = Net_Change_In_Short_term_Investments
    df['Net Change In Long-Term Investments'] = Net_Change_In_Long_Term_Investments
    df['Net Change In Investments - Total'] = Net_Change_In_Investments_Total
    df['Investing Activities - Other'] = Investing_Activities_Other
    df['Cash Flow From Investing Activities'] = Cash_Flow_From_Investing_Activities
    df['Net Long-Term Debt'] = Net_Long_Term_Debt
    df['Net Current Debt'] = Net_Current_Debt
    df['Debt Issuance/Retirement Net - Total'] = Debt_Issuance_Retirement_Net_Total
    df['Net Common Equity Issued/Repurchased'] = Net_Common_Equity_Issued_Repurchased
    df['Net_Total_Equity_Issued_Repurchased'] = Net_Total_Equity_Issued_Repurchased
    df['Total Common And Preferred Stock Dividends Paid'] = Total_Common_And_Preferred_Stock_Dividends_Paid
    df['Financial Activities - Other'] = Financial_Activities_Other
    df['Cash Flow From Financial Activities'] = Cash_Flow_From_Financial_Activities
    df['Net Cash Flow'] = Net_Cash_Flow
    df['Stock-Based Compensation'] = Stock_Based_Compensation
    df['Common_Stock_Dividends_Paid']= Common_Stock_Dividends_Paid
except Exception as e:
    pass

print(df)

df.to_csv(r'C:\Users\roboz.DESKTOP-F86F289\Desktop\Statements\cash_flow_final.csv')