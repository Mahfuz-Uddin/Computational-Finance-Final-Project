'''
@project       : Queens College CSCI 365/765 Computational Finance
@Instructor    : Dr. Alex Pang
@Student Name  : Team Rocket
@Date          : June 2021

A Simple Option Class

'''
import enum
import calendar
import math
import pandas as pd
import numpy as np


class Option(object):
    '''
    time_to_expiry is the number of days till expiry_date expressed in unit of years
    underlying is the underlying stock object
    '''

    class Type(enum.Enum):
        CALL = "Call"
        PUT  = "Put"

    class Style(enum.Enum):
        EUROPEAN = "European"
        AMERICAN = "American"

    def __init__(self, option_type, option_style,  underlying, time_to_expiry, strike):
        self.option_type = option_type
        self.option_style = option_style
        self.underlying = underlying
        self.time_to_expiry = time_to_expiry
        self.strike = strike

class EuropeanCallOption(Option):
    def __init__(self, underlying, time_to_expiry, strike):
        Option.__init__(self, Option.Type.CALL, Option.Style.EUROPEAN,
                        underlying, time_to_expiry, strike)

class EuropeanPutOption(Option):
    def __init__(self, underlying, time_to_expiry, strike):
        Option.__init__(self, Option.Type.PUT, Option.Style.EUROPEAN,
                        underlying, time_to_expiry, strike)

class AmericanCallOption(Option):
    def __init__(self, underlying, time_to_expiry, strike):
        Option.__init__(self, Option.Type.CALL, Option.Style.AMERICAN,
                        underlying, time_to_expiry, strike)

class AmericanPutOption(Option):
    def __init__(self, underlying, time_to_expiry, strike):
        Option.__init__(self, Option.Type.PUT, Option.Style.AMERICAN,
                        underlying, time_to_expiry, strike)


