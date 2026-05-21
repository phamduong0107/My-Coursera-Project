import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings('ignore',category = FutureWarning)
import matplotlib.pyplot as plt
def make_graph(stock_data,revenue_data,stock):
    stock_data_specific = stock_data[stock_data.Date <= '2021-06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
    fig, axes = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

    # Stock price
    axes[0].plot(pd.to_datetime(stock_data_specific.Date), stock_data_specific.Close.astype("float"), label="Share Price", color="blue")
    axes[0].set_ylabel("Price ($US)")
    axes[0].set_title(f"{stock} - Historical Share Price")

    # Revenue
    axes[1].plot(pd.to_datetime(revenue_data_specific.Date), revenue_data_specific.Revenue.astype("float"), label="Revenue", color="green")
    axes[1].set_ylabel("Revenue ($US Millions)")
    axes[1].set_xlabel("Date")
    axes[1].set_title(f"{stock} - Historical Revenue")

    plt.tight_layout()
    plt.show()
tesla = yf.Ticker('TSLA')
tesla_data = tesla.history(period = 'max')
tesla_data.reset_index(inplace= True)
tesla_data.head()
url = ' https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm'
html_data = requests.get(url).text
soup = BeautifulSoup(html_data,'html.parser')
tesla_revenue = pd.DataFrame(columns = ['Date','Revenue'])
tables = beautiful_soup.find_all('table')
for row in tables.find('tbody').find_all('tr'):
    col = row.find_all('td')
    date = col[0].text
    revenue = col[1].text.replace('$','').replace(',','')
    tesla_revenue = pd.concat([tesla_revenue,pd.DataFrame({'Date':[date],'Revenue':[revenue]})],ignore_index = True)
print(tesla_revenue.head())
tesla_revenue['Revenue'] = tesla_revenue['Revenue'].str.replace(',|\$','',regex = True)
tesla_revenue.dropna(inplace=True)
tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]
print(tesla_revenue.tail())

GameStop = yf.Ticker('GME')
gme_data = GameStop.history(period = 'max')
gme_data.reset_index(inplace = True)
print(gme_data.head())

url_2 = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html'
html_data_2 = requests.get(url_2)
beautiful_soup = BeautifulSoup(html_data_2.text,'html.parser')
gme_revenue = pd.DataFrame(columns = ['GameStop','Revenue'])
tables = beautiful_soup.find_all('table')
for row in tables[1].find('tbody').find_all('tr'):
    col = row.find_all('td')
    if len(col) >= 2:
        date = col[0].text
        revenue = col[1].text.replace('$','').replace(',','')
        gme_revenue = pd.concat([gme_revenue,pd.DataFrame({'Date':[date],'Revenue':[revenue]})],ignore_index = True)
print(gme_revenue.head())
make_graph(tesla_data, tesla_revenue, 'Tesla')
make_graph(gme_data, gme_revenue, 'GameStop')
