__author__ = 'KanwalS'
from collections import deque
import numpy as np


class MovingSum(deque):
    def __init__(self, size=0):
        super(MovingSum, self).__init__(maxlen=size)

    def getAvg(self):  # TODO: Make type check for integer or floats
        if(len(self) < self.maxlen):
            return None
        return sum(self)/len(self)

    def getSum(self):

        if(len(self) < self.maxlen):
            return None

        return sum(self)

    def getStd(self):
        if(len(self) < self.maxlen):
            return None
        return np.std(self)