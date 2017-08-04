__author__ = 'JahaanM'

import numpy as np
import math

from Strategy import Strategy
from EMA import EMA
#MACD Strategy -> Buy when slow_ema crosses over fast_ema and Sell when the opposite occurs

class MACDStrategy(Strategy):

    def __init__(self, symbol, fast_time, slow_time, signal_time):
        Strategy.__init__(self, symbol)
        self.fast_ema = EMA(0)
        self.slow_ema = EMA(0)
        self.signal_ema = EMA(0)
        self.fast_time = fast_time
        self.slow_time = slow_time
        self.signal_time = signal_time
        self.prev_hist = 0

    def update_signal(self, symbol, signal):
        self.signal = signal
        self.symbol = symbol

    def on_new_tick(self, tick_object):
        #   generate macd --> e.g. 12 sec EMA of p - 26 sec EMA of p
        fast_line = self.fast_ema.next(tick_object.ltp, self.fast_time)
        slow_line = self.slow_ema.next(tick_object.ltp, self.slow_time)
        macd_line = fast_line - slow_line if slow_line is not None else None
        #   generate signal --> e.g. 9 sec EMA of MACD
        signal_line = self.signal_ema.next(macd_line, self.signal_time) if macd_line is not None else None

        if signal_line is not None:
            histogram = macd_line - signal_line
            if histogram > 0 > self.prev_hist:
                self.update_signal(tick_object.symbol, 2)
            if histogram < 0 < self.prev_hist:
                self.update_signal(tick_object.symbol, -2)

            self.prev_hist = histogram

        self.last_tick_object = tick_object

    #def __str__(self):
        #return "symbol %s | signal %s | fast %s | slow %s | signal %s | prev_hist %s | price %s" % \
               #(self.symbol, self.signal, self.fast_ema, self.slow_ema, self.signal_ema, self.prev_hist, self.last_tick_object.ltp)

