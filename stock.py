'''
@project       : Queens College CSCI 365/765 Computational Finance
@Instructor    : Dr. Alex Pang
@Student Name  : Tanzina Eisha, Richard Lin, Mahfuz Uddin
@Date          : June 2021

'''
import enum
import calendar
import math
import pandas as pd
import numpy as np

import datetime 
from scipy.stats import norm

from math import log, exp, sqrt

from utils import MyYahooFinancials 

class Stock(object):
    '''
    Stock class for getting financial statements as well as pricing data
    '''
    def __init__(self, symbol, spot_price = None, sigma = None, dividend_yield = 0, freq = 'annual'):
        self.symbol = symbol
        self.spot_price = spot_price
        self.sigma = sigma
        self.dividend_yield = dividend_yield
        self.yfinancial = MyYahooFinancials(symbol, freq)
        self.ohlcv_df = None
        

    def get_daily_hist_price(self, start_date, end_date):
        '''
        Get historical OHLCV pricing dataframe
        '''
        #TODO
        # self.ohlcv_df = ....
        data = self.yfinancial.get_historical_price_data(start_date,end_date, "Daily")
        self.ohlcv_df = pd.DataFrame(data[self.symbol]['prices'])
        self.ohlcv_df = self.ohlcv_df.drop('date', axis=1).set_index('formatted_date')
        #end TODO
        
    def calc_returns(self):
        '''
        '''
        self.ohlcv_df['prev_close'] = self.ohlcv_df['close'].shift(1)
        self.ohlcv_df['returns'] = (self.ohlcv_df['close'] - self.ohlcv_df['prev_close'])/ \
                                        self.ohlcv_df['prev_close']


    # financial statements related methods
    
    def get_total_debt(self):
        '''
        compute total_debt as long term debt + current debt 
        current debt = total current liabilities - accounts payables - other current liabilities (ignoring current deferred liabilities)
        '''
        result = None
        # TODO
        currentDebt = self.yfinancial.get_total_current_liabilities() - self.yfinancial.get_account_payable() - self.yfinancial.get_other_current_liabilities()
        result = (self.yfinancial.get_long_term_debt() + currentDebt)
        # end TODO
        return(result)

    def get_free_cashflow(self):
        '''
        get free cash flow as operating cashflow + capital expenditures (which will be negative)
        '''
        result = None
        # TODO
        result = (self.yfinancial.get_operating_cashflow() + self.yfinancial.get_capital_expenditures())
        # end TODO
        return(result)

    def get_cash_and_cash_equivalent(self):
        '''
        Return cash plus short term investment 
        '''
        result = None
        # TODO
        result = (self.yfinancial.get_cash() + self.yfinancial.get_short_term_investments())
        # end TODO
        return result

    def get_num_shares_outstanding(self):
        '''
        get current number of shares outstanding from Yahoo financial library
        '''
        result = None
        # TODO
        result = self.yfinancial.get_num_shares_outstanding()
        # end TODO
        return(result)

    def get_beta(self):
        '''
        get beta from Yahoo financial
        '''
        result = None
        # TODO
        result = self.yfinancial.get_beta()
        # end TODO
        return(result)

    def lookup_wacc_by_beta(self, beta):
        '''
        lookup wacc by using the table in Slide 15 of the DiscountedCashFlowModel lecture powerpoint
        '''
        result = None
        # TODO:
        if (beta < 0.8):
            result = 0.05
        elif (0.8 <= beta and beta < 1.0):
            result = 0.06
        elif (1.0 <= beta and beta < 1.1):
            result = 0.065
        elif (1.1 <= beta and beta < 1.2):
            result = 0.07
        elif (1.2 <= beta and beta < 1.3):
            result = 0.075
        elif (1.3 <= beta and beta < 1.5):
            result = 0.08
        elif (1.5 <= beta and beta < 1.6):
            result = 0.085
        elif (beta >= 1.6):
            result = 0.09
        #end TODO
        return(result)
        



def _test():
    symbol = 'CAT'

    stock = Stock(symbol, 'annual')
    print(stock.get_beta())



if __name__ == "__main__":
    _test()
