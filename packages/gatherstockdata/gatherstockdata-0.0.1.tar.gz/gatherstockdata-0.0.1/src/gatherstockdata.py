from dataclasses import dataclass, asdict
from bs4 import BeautifulSoup
import time
import datetime
import pandas as pd
import mplfinance as mpf
import requests


@dataclass
class FundamentalData:
    company: str
    t_ppe: str
    f_ppe: str
    pps: str


def gather_funda_info(ticker):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
    url = f"https://finance.yahoo.com/quote/{ticker}/key-statistics?p={ticker}"

    r = requests.get(url, headers=header)
    soup = BeautifulSoup(r.text, "html.parser")

    funda_info = FundamentalData(
        company=soup.find('h1', {'class': 'D(ib) Fz(18px)'}).text,
        t_ppe=soup.find_all('td', {'class': 'Fw(500) Ta(end) Pstart(10px) Miw(60px)'})[2].text,
        f_ppe=soup.find_all('td', {'class': 'Fw(500) Ta(end) Pstart(10px) Miw(60px)'})[3].text,
        pps=soup.find_all('td', {'class': 'Fw(500) Ta(end) Pstart(10px) Miw(60px)'})[5].text
    )
    return asdict(funda_info)


class BetaValue:
    def __init__(self, company, beta_value):
        self.__company = company
        self.__beta_value = beta_value

    def __str__(self):
        return "{}: {}".format(self.__company, self.__beta_value)

    def __lt__(self, other):
        return self.__beta_value < other.__beta_value

    def __gt__(self, other):
        return other < self

    def get_company(self):
        return self.__company

    def get_beta_value(self):
        return self.__beta_value


# Gathering beta values by using requests to send request to http and use BeautifulSoup to parse the data
def get_html_and_parse_data(tickers):
    beta_values_list = []
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}

    for i in range(len(tickers)):
        url = f"https://finance.yahoo.com/quote/{tickers[i]}/key-statistics?p={tickers[i]}"
        r = requests.get(url, headers=header)
        soup = BeautifulSoup(r.text, "html.parser")

        # Finding beta values and company name in web elements
        company_name = soup.find('h1', {'class': 'D(ib) Fz(18px)'}).text
        company_beta = soup.find_all('td', {'class': 'Fw(500) Ta(end) Pstart(10px) Miw(60px)'})[9].text

        beta_obj = BetaValue(company_name, company_beta)
        beta_values_list.append(beta_obj)

    return beta_values_list


# Sorting beta values list using bubblesort and return sorted list
def sort_beta_value(beta_list):
    for i in range(len(beta_list) - 1, 0, -1):
        for j in range(i):
            if beta_list[j] < beta_list[j + 1]:
                beta_list[j + 1], beta_list[j] = beta_list[j], beta_list[j + 1]

    return beta_list


def gather_beta_data(tickers):
    beta_values_list = get_html_and_parse_data(tickers)
    sorted_beta_list = sort_beta_value(beta_values_list)

    return sorted_beta_list


# Gathering tech data from query url
def gather_tech_data(ticker):

    period1 = int(time.mktime((datetime.datetime.today() - datetime.timedelta(days=30)).timetuple()))
    period2 = int(time.mktime(datetime.datetime.today().timetuple()))
    interval = "1d"
    query_url = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true"

    # Read downloaded data as csv file layout
    df = pd.read_csv(query_url, index_col=0, parse_dates=True)

    # Getting price change percentage and converting to two decimals
    price_change = ((df['Close'][-1] - df['Close'][0]) / df['Close'][0]) * 100
    price_change = f"{price_change:.2f}"

    stock_price_high = df['High'].max()
    stock_price_low = df['Low'].min()

    # Configuring plot colors
    colors = mpf.make_marketcolors(up="#00ff00",
                                   down="#ff0000",
                                   wick="inherit",
                                   edge="inherit",
                                   volume="in")

    # Configuring plot style
    mpf_style = mpf.make_mpf_style(base_mpf_style="nightclouds", marketcolors=colors)

    df['SMA'] = df.Close.rolling(window=5).mean()
    df['stddev'] = df.Close.rolling(window=5).std()
    df['Upper'] = df.SMA + 2 * df.stddev
    df['Lower'] = df.SMA - 2 * df.stddev

    df = df.dropna()

    subplots = df[['Upper', 'Lower']]
    make_subplots = mpf.make_addplot(subplots)

    fig, ax = mpf.plot(df, addplot=make_subplots,
                       type="candle",
                       style=mpf_style,
                       volume=True,
                       returnfig=True,
                       title=ticker
                       )
    # Return dictionary with variables
    data = {
        'df': df,
        'price_change': price_change,
        'stock_price_low': stock_price_low,
        'stock_price_high': stock_price_high,
        'mpf_style': mpf_style,
        'make_subplots': make_subplots,
        'fig': fig
    }

    return data

