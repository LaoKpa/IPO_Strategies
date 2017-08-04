__author__ = 'JahaanM'
class EMA:
    def __init__(self, sma):
        self.prev_ema = sma
        self.count = 0

    def next(self, price, time):
        multiplier = (2.0/(time+1))
        ema = price*multiplier + self.prev_ema*(1-multiplier)
        self.prev_ema = ema
        self.count += 1
        if self.count >= time:
            return ema
        else:
            return None

    def __str__(self):
        return str(self.prev_ema)

