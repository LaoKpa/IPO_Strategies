__author__ = 'KanwalS'

import numpy as np
import math

from Strategy import Strategy
from MovingSum import MovingSum


class TradedQtyStrategy(Strategy):

    def __init__(self, symbol, lookback, threshold):
        Strategy.__init__(self, symbol)
        self.traded_qty = MovingSum(lookback)
        self.returns = MovingSum(2+lookback/10)
        self.threshold = threshold
        self.continuous_traded_qty = 0

    def update_signal(self, symbol, signal):
        self.signal = signal
        self.symbol = symbol

    def on_new_tick(self, tick_object):
        #   print "current object", tick_object, "last object : ", self.last_tick_object
        self.traded_qty.append(tick_object.ltq)

        if self.last_tick_object is not None:

            self.returns.append(10000*math.log(tick_object.ltp*1.0/self.last_tick_object.ltp))
            qty_zscore = (tick_object.ltq - self.traded_qty.getAvg())/self.traded_qty.getStd()

            if qty_zscore > self.threshold:
                self.update_signal(tick_object.symbol, np.sign(self.returns.getSum())*2)

            if qty_zscore > self.threshold/2:
                self.update_signal(tick_object.symbol, np.sign(self.returns.getSum()))

        self.last_tick_object = tick_object

    def __str__(self):
        return "symbol %s | signal %s | returns %s | qty_mean %s | qty_std %s" % (self.symbol,
                                                                        self.signal,
                                                                        self.returns.getSum(),
                                                                        self.traded_qty.getAvg(),
                                                                        self.traded_qty.getStd())
