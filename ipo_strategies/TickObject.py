__author__ = 'KanwalS'

from settings import *


class TickObject:

    def __init__(self, line):
        line = line.split(",")
        self.timestamp = int(line[TIMESTAMP_INDEX])
        self.ltp = float(line[LTP_INDEX])
        self.ltq = float(line[LTQ_INDEX])
        self.symbol = line[SYMBOL_INDEX]
        self.date = line[DATE_INDEX][:8]

    def __str__(self):
        return "timestamp %s | symbol %s | ltp %s | ltq %s | date %s " % (self.timestamp, self.symbol, self.ltp, self.ltq, self.date)