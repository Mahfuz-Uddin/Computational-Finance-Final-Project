'''
@project       : Queens College CSCI 365/765 Computational Finance
@Instructor    : Dr. Alex Pang

@Student Name  : Tanzina Eisha, Richard Lin, Mahfuz Uddin

@Date          : June 2021


'''

import datetime
import math

from scipy.stats import norm
from math import log, exp, sqrt, pi
import datetime

from stock import Stock
from option import Option, EuropeanCallOption, EuropeanPutOption


class BlackScholesModel(object):
    '''
    OptionPricer
    '''

    def __init__(self, pricing_date, risk_free_rate):
        self.pricing_date = pricing_date
        self.risk_free_rate = risk_free_rate

    def calc_parity_price(self, option, option_price):
        '''
        return the put price from Put-Call Parity if input option is a call
        else return the call price from Put-Call Parity if input option is a put
        '''
        # TODO: implement details here
        if option.option_style == Option.Style.AMERICAN:
            raise Exception("Price for American option not implemented yet")
        elif option.option_style == Option.Style.EUROPEAN:
            if option.option_type == Option.Type.CALL:
                result = (option_price + (option.strike * exp(-self.risk_free_rate * option.time_to_expiry))
                          - option.underlying.spot_price)
            elif option.option_type == Option.Type.PUT:
                result = (option_price + option.underlying.spot_price - (option.strike * exp(-self.risk_free_rate *
                                                                                             option.time_to_expiry)))
        else:
            raise Exception("Unsupported option type")
        # end TODO
        return result

    def calc_model_price(self, option):
        '''
        Calculate the price of the option using Black-Scholes model
        '''
        px = None
        if option.option_style == Option.Style.AMERICAN:
            raise Exception("B\S price for American option not implemented yet")
        elif option.option_style == Option.Style.EUROPEAN:

            S0 = option.underlying.spot_price
            sigma = option.underlying.sigma
            T = option.time_to_expiry
            K = option.strike
            q = option.underlying.dividend_yield
            r = self.risk_free_rate
            d1 = (log(S0 / K) + T * (r - q + pow(sigma, 2) / 2)) / (sigma * sqrt(T))
            d2 = d1 - (sigma * sqrt(T))
            # TODO: implement details here
            if option.option_type == Option.Type.CALL:
                px = S0 * exp(-q * T) * norm.cdf(d1) - K * exp(-r * T) * norm.cdf(d2)
            if option.option_type == Option.Type.PUT:
                px = (K * exp(-r * T)) * norm.cdf(-d2) - (S0 * exp(-q * T) * norm.cdf(-d1))
            # end TODO
        else:
            raise Exception("Unsupported option type")
        return px

    def calc_delta(self, option):
        S0 = option.underlying.spot_price
        sigma = option.underlying.sigma
        T = option.time_to_expiry
        K = option.strike
        q = option.underlying.dividend_yield
        r = self.risk_free_rate
        d1 = (log(S0 / K) + T * (r - q + pow(sigma, 2) / 2)) / (sigma * sqrt(T))
        if option.option_style == Option.Style.AMERICAN:
            raise Exception("B\S price for American option not implemented yet")
        elif option.option_style == Option.Style.EUROPEAN:
            # TODO:
            if option.option_type == Option.Type.CALL:
                result = exp(-q * T) * norm.cdf(d1)
            if option.option_type == Option.Type.PUT:
                result = exp(-q * T) * (norm.cdf(d1) - 1)
        # end TODO
        else:
            raise Exception("Unsupported option type")

        return result

    def calc_gamma(self, option):

        S0 = option.underlying.spot_price
        sigma = option.underlying.sigma
        T = option.time_to_expiry
        K = option.strike
        q = option.underlying.dividend_yield
        r = self.risk_free_rate
        d1 = (log(S0 / K) + T * (r - q + pow(sigma, 2) / 2)) / (sigma * sqrt(T))
        if option.option_style == Option.Style.AMERICAN:
            raise Exception("B\S price for American option not implemented yet")
        elif option.option_style == Option.Style.EUROPEAN:
            if option.option_type == Option.Type.CALL:
                result = (norm.pdf(d1) * (exp(-q * T))) / (S0 * sigma * sqrt(T))
            if option.option_type == Option.Type.PUT:
                result = (norm.pdf(d1) * (exp(-q * T))) / (S0 * sigma * sqrt(T))
        else:
            raise Exception("Unsupported option type")

        return result

    def calc_theta(self, option):
        S0 = option.underlying.spot_price
        sigma = option.underlying.sigma
        T = option.time_to_expiry
        K = option.strike
        q = option.underlying.dividend_yield
        r = self.risk_free_rate
        d1 = (log(S0 / K) + T * (r - q + pow(sigma, 2) / 2)) / (sigma * sqrt(T))
        d2 = d1 - (sigma * sqrt(T))

        if option.option_style == Option.Style.AMERICAN:
            raise Exception("B\S price for American option not implemented yet")
        elif option.option_style == Option.Style.EUROPEAN:

            if option.option_type == Option.Type.CALL:
                result = (((-S0 * norm.pdf(d1) * sigma * exp(-q * T)) / (2 * sqrt(T))) +
                          ((q * S0 * norm.cdf(d1) * exp(-q * T)) - (r * K * exp(-r * T) * norm.cdf(d2))))
            if option.option_type == Option.Type.PUT:
                result = (((-S0 * norm.pdf(d1) * sigma * exp(-q * T)) / (2 * sqrt(T))) -
                          ((q * S0 * norm.cdf(-d1) * exp(-q * T)) + (r * K * exp(-r * T) * norm.cdf(-d2))))
        else:
            raise Exception("Unsupported option type")

        return result

    def calc_vega(self, option):
        S0 = option.underlying.spot_price
        sigma = option.underlying.sigma
        T = option.time_to_expiry
        K = option.strike
        q = option.underlying.dividend_yield
        r = self.risk_free_rate
        d1 = (log(S0 / K) + T * (r - q + pow(sigma, 2) / 2)) / (sigma * sqrt(T))
        if option.option_style == Option.Style.AMERICAN:
            raise Exception("B\S price for American option not implemented yet")
        elif option.option_style == Option.Style.EUROPEAN:

            if option.option_type == Option.Type.CALL:
                result = S0 * sqrt(T) * norm.pdf(d1) * exp(-q * T)
            if option.option_type == Option.Type.PUT:
                result = S0 * sqrt(T) * norm.pdf(d1) * exp(-q * T)
        else:
            raise Exception("Unsupported option type")

        return result

    def calc_rho(self, option):
        S0 = option.underlying.spot_price
        sigma = option.underlying.sigma
        T = option.time_to_expiry
        K = option.strike
        q = option.underlying.dividend_yield
        r = self.risk_free_rate
        d1 = (log(S0 / K) + T * (r - q + pow(sigma, 2) / 2)) / (sigma * sqrt(T))
        d2 = d1 - (sigma * sqrt(T))
        if option.option_style == Option.Style.AMERICAN:
            raise Exception("B\S price for American option not implemented yet")
        elif option.option_style == Option.Style.EUROPEAN:
            # TODO:
            if option.option_type == Option.Type.CALL:
                result = K * T * exp(-r * T) * norm.cdf(d2)
            if option.option_type == Option.Type.PUT:
                result = -K * T * exp(-r * T) * norm.cdf(-d2)

            # end TODO
        else:
            raise Exception("Unsupported option type")
        return result


def _test():
    symbol = 'APPL'
    pricing_date = datetime.date(2021, 6, 1)
    risk_free_rate = 0.04
    model = BlackScholesModel(pricing_date, risk_free_rate)
    # .... use this as your unit test
    # calculate the B/S model price for a 3-month ATM call
    T = 3 / 12
    num_period = 2
    dt = T / num_period
    S0 = 130
    K = 130

    sigma = 0.3
    stock = Stock(symbol, S0, sigma)

    call = EuropeanCallOption(stock, T, K)

    model_price = model.calc_model_price(call)
    delta = model.calc_delta(call)
    gamma = model.calc_gamma(call)
    theta = model.calc_theta(call)
    vega = model.calc_vega(call)
    rho = model.calc_rho(call)
    parity = model.calc_parity_price(call, model_price)
    print('Model Price: ', model_price)
    print('delta: ', delta)
    print('Gamma: ', gamma)
    print('Theta: ', theta)
    print('Vega: ', vega)
    print('Rho', rho)
    print('parity', parity)


if __name__ == "__main__":
    _test()
