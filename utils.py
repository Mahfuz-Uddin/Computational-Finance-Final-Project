'''
@project       : Queens College CSCI 365/765 Computational Finance
@Instructor    : Dr. Alex Pang
@Date          : June 2021
@Student Name  : Tanzina Eisha, Richard Lin, Mahfuz Uddin

https://github.com/JECSand/yahoofinancials

'''

from yahoofinancials import YahooFinancials 

class MyYahooFinancials(YahooFinancials):
    '''
    Extended class based on YahooFinancial libary

    '''
    def __init__(self, symbol, freq = 'annual'):
        YahooFinancials.__init__(self, symbol)
        self.freq = freq

    def get_operating_cashflow(self):
        return self._financial_statement_data('cash', 'cashflowStatementHistory', 'totalCashFromOperatingActivities', self.freq)

    def get_capital_expenditures(self):
        return self._financial_statement_data('cash', 'cashflowStatementHistory', 'capitalExpenditures', self.freq)

    def get_long_term_debt(self):
        return self._financial_statement_data('balance', 'balanceSheetHistory', 'longTermDebt', self.freq)

    def get_account_payable(self):
        return self._financial_statement_data('balance', 'balanceSheetHistory', 'accountsPayable', self.freq)

    def get_total_current_liabilities(self):
        return self._financial_statement_data('balance', 'balanceSheetHistory', 'totalCurrentLiabilities', self.freq)

    def get_other_current_liabilities(self):
        return self._financial_statement_data('balance', 'balanceSheetHistory', 'otherCurrentLiab', self.freq)

    def get_cash(self):
        return self._financial_statement_data('balance', 'balanceSheetHistory', 'cash', self.freq)

    ##
    def get_short_term_investments(self):
        return self._financial_statement_data('balance', 'balanceSheetHistory', 'shortTermInvestments', self.freq)
 
    
    def get_total_assets(self):
        return self._financial_statement_data('balance', 'balanceSheetHistory', 'totalAssets', self.freq)

    def get_total_debt(self):
        currentDebt = self.get_total_current_liabilities() - self.get_account_payable() - self.get_other_current_liabilities()
        return (self.get_long_term_debt() + currentDebt)

    def get_current_debt(self):
        return (self.get_total_current_liabilities() - self.get_account_payable() - self.get_other_current_liabilities())

    def get_free_cash_flow(self):
        return (self.get_operating_cashflow() + self.get_capital_expenditures())
        



def _test():
    symbol = "CAT"
    
    yfinance = MyYahooFinancials(symbol)
    print(yfinance.get_short_term_investments())
    


if __name__ == "__main__":
    _test()
