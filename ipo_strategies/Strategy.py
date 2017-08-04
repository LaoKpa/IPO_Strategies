__author__ = 'KanwalS'


class Strategy(object):

    # symbol = 0  # stock symbol
    # signal = 0  # 2, -2
    # square_off_signal = 0   # -1,1
    # timestamp = 0   # epoch timestamp
    # las_tick_object = None

    def __init__(self, symbol):
        self.symbol = symbol
        self.signal = 0
        self.last_tick_object = None

    def init_strategy(self, symbol):
        self.symbol = symbol
        self.signal = 0

    def update_signal(self, symbol, signal):
        self.signal = signal
        self.symbol = symbol

    def on_new_tick(self, tick_object):
        print "current object", tick_object, "last object : ", self.last_tick_object
        self.last_tick_object = tick_object

    def __str__(self):
        return "symbol %s | signal %s " % (self.symbol, self.signal)