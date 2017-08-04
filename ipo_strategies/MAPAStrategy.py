__author__ = 'JahaanM'

import numpy as np
import math

from Strategy import Strategy
from MovingSum import MovingSum

#Moving Average Price Action -> Buy when 3 points are above the moving average and follow a
# price pattern of high, lower than high, higher than high and sell when the opposite occurs.

class MAPAStrategy(Strategy):

    def __init__(self, symbol, lookback):
        Strategy.__init__(self, symbol)
        self.sma = MovingSum(lookback)
        self.price_act = MovingSum(3)

    def update_signal(self, symbol, signal):
        self.signal = signal
        self.symbol = symbol

    def on_new_tick(self, tick_object):
        #   print "current object", tick_object, "last object : ", self.last_tick_object
        self.sma.append(tick_object.ltp)
        self.price_act.append(tick_object.ltp)

        if self.sma.getAvg() is not None:

            avg = self.sma.getAvg()
            below = all(t < avg for t in self.price_act)
            above = all(t > avg for t in self.price_act)

            if below:
                lis = self.price_act
                if lis[2] < lis[0] < lis[1]:
                    self.update_signal(tick_object.symbol, -2)

            if above:
                lis = self.price_act
                if lis[2] > lis[0] > lis[1]:
                    self.update_signal(tick_object.symbol, 2)

        self.last_tick_object = tick_object

    def __str__(self):
        return "mov_avg = {} ltp3 = {}".format(self.sma.getAvg(), self.price_act)