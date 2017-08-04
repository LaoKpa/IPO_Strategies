__author__ = 'JahaanM'
import numpy as np
import math

from Strategy import Strategy
from MovingSum import MovingSum
#Money Flow Strategu -> Buy When Oversold(20 on Indicator) and Sell when Overbought(80 on Indicator)

class MFIStrategy(Strategy):

    def __init__(self, symbol, lookback):
        Strategy.__init__(self, symbol)
        self.pos_flow = MovingSum(lookback)
        self.neg_flow = MovingSum(lookback)
        self.lltp = 0

    def update_signal(self, symbol, signal):
        self.signal = signal
        self.symbol = symbol

    def on_new_tick(self, tick_object):
        #   print "current object", tick_object, "last object : ", self.last_tick_object
        pos = 0
        neg = 0
        diff = tick_object.ltp - self.lltp
        if diff >= 0:
            pos += tick_object.ltq
        else:
            neg += tick_object.ltq
        self.pos_flow.append(pos)
        self.neg_flow.append(neg)

        if self.pos_flow.getSum() is not None:
            MFR = 0
            if self.pos_flow.getSum() == 0:
                MFR += 0
            elif self.neg_flow.getSum() == 0:
                MFR += 99
            else:
                MFR += (1.0*self.pos_flow.getSum())/self.neg_flow.getSum()
            MFI = 100 - 100.0/(1 + MFR)

            if MFI < 20:
                self.update_signal(tick_object.symbol, 2)

            if MFI > 80:
                self.update_signal(tick_object.symbol, -2)
        self.lltp = tick_object.ltp
        self.last_tick_object = tick_object
