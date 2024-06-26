from bs4 import BeautifulSoup
import requests

def scrape_stock_data(symbol):
    url = f"https://finance.yahoo.com/quote/{symbol}/"

    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, 'html.parser')
    # print(soup.head)
    current_price = soup.find(f"fin-streamer", {"data-symbol": {symbol}, "data-testid": "qsp-price"})['data-value']

    previous_price_data = soup.find('span', class_="value svelte-tx3nkj")
    previous_price = [i['data-value'] for i in previous_price_data]

    price_change = soup.find(f"fin-streamer", {"data-symbol": {symbol}, "data-testid": "qsp-price-change"})['data-value']
    percentage_changed = soup.find(f"fin-streamer", {"data-symbol": {symbol}, "data-field": "regularMarketChangePercent"})['data-value']
    week_52_range = soup.find(f"fin-streamer", {"data-symbol": {symbol},"data-field": "fiftyTwoWeekRange"})['data-value']
    week_52_low, week_52_high = week_52_range.split(' - ')

    market_cap = soup.find(f"fin-streamer", {"data-symbol": {symbol},"data-field": "marketCap"})['data-value']
    pe_ratio = soup.find(f"fin-streamer", {"data-symbol": {symbol},"data-field": "trailingPE"})['data-value']
    dividend_yield = soup.find('span', class_="value svelte-tx3nkj").text
 
    print("Current Price : ",current_price)
    print("Previous Closed : ", previous_price[0])
    print("price_change :", price_change)
    print("percentage_changed :", percentage_changed)
    print("week_52_high :", week_52_high)
    print("week_52_low:", week_52_low)
    print("market_cap:", market_cap)
    print("pe_ratio:", pe_ratio)
    print("dividend_yield:", dividend_yield)



scrape_stock_data('GOOG')
