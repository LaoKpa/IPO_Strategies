__author__ = 'JahaanM'

from numpy import genfromtxt
import numpy as np

my_data = genfromtxt('lauruslab.csv', delimiter=',', dtype=None)

my_data = my_data[1:]

time = my_data[0][0][12:20]
hour = int(time[0:2])
min = int(time[3:5])
sec = int(time[6:8])

large = 0
pt = [hour, min, sec]
prev_ep = [1482121800]

with open("LAURUSLABS-EQ20161219.csv", mode="w") as f_write:
    for i in range(len(my_data)):
        time = my_data[i][0][12:20]
        hour = int(time[0:2])
        min = int(time[3:5])
        sec = int(time[6:8])
        ct = [hour, min, sec]
        delta = (ct[0]-pt[0])*60*60 + (ct[1]-pt[1])*60 + (ct[2]-pt[2])
        if delta > large:
            large = delta
        if delta > 0:
            if delta == 1:
                f_write.write(str(prev_ep[0]) + ","
                                + str(my_data[i-1][2]) + ","
                                + str(my_data[i-1][7]) + ","
                                + str(my_data[i-1][8]) + ","
                                + "20161219" + ","
                                        + "\n")
                prev_ep[0] += 1
            else:
                for y in range(delta):
                    f_write.write(str(prev_ep[0]+y+1) + ","
                                    + str(my_data[i-1][2]) + ","
                                    + (my_data[i-1][7]).strip('\'') + ","
                                    + (my_data[i-1][8]).strip('\'') + ","
                                    + "20161219" + ","
                                            + "\n")
                prev_ep[0] += delta
        pt[2] = ct[2]
        pt[1] = ct[1]
        pt[0] = ct[0]
    f_write.close()

print(large)

