'''
@project       : Queens College CSCI 365/765 Computational Finance
@Instructor    : Dr. Alex Pang
@Date          : June 2021
@Student Name  : Tanzina Eisha, Richard Lin, Mahfuz Uddin

https://github.com/JECSand/yahoofinancials

'''

import pandas as pd

from utils import MyYahooFinancials 


def download_fundamental_data(input_file_name, output_file_name):
    '''

    '''

    # TODO
    df = pd.read_csv(input_file_name)
    symbol= list(df['Symbol'])
    sector = list(df['Sector'])
    epsNext5Y = list(df['EPS Next 5Y'])
    marketCap = []
    totalAssets = []
    totalDebt = []
    freeCashFlow = []
    beta = []
    peRatio = []

    for i in symbol:
        yfinance = MyYahooFinancials(i)
        try:
            marketCap.append(yfinance.get_market_cap())
        except:
            marketCap.append("")
        try:
            totalAssets.append(yfinance.get_total_assets())
        except:
            totalAssets.append("")
        try:
            totalDebt.append(yfinance.get_total_debt())
        except:
            try:
                totalDebt.append(yfinance.get_long_term_debt())
            except:
                totalDebt.append("")
        try:
            freeCashFlow.append(yfinance.get_free_cash_flow())
        except:
            freeCashFlow.append("")
        try:
            beta.append(yfinance.get_beta())
        except:
            beta.append("")
        try:
            peRatio.append(yfinance.get_pe_ratio())
        except:
            peRatio.append("")

    df = pd.DataFrame(list(zip(symbol, sector, epsNext5Y, marketCap, totalAssets, totalDebt, freeCashFlow, beta,peRatio)), columns= ['Symbol', 'Sector','EPS Next 5Y', 'Market Cap', 'Total Assets', 'Total Debt', 'Free Cash Flow', 'Beta', 'P/E Ratio'])
    df.to_csv (output_file_name ,index = False, header=True, )

    # end TODO



def run():
    input_fname = "StockUniverse.csv"
    output_fname = "StockUniverseWithData.csv"
    download_fundamental_data(input_fname, output_fname)

    
if __name__ == "__main__":
    run()
