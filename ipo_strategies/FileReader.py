
import TickObject
import Strategy
import TradedQtyStrategy
import MACDStrategy
import MAPAStrategy
import MFIStratetgy
import os
from settings import *


def read_file(filename, symbol_list_file):

    strategies = {}
    version = "version_"

    with open(symbol_list_file, mode='r') as f_symbol:
        for line in f_symbol.readlines():
            line = line.split(",")
            # replace your strategy here
            strategies[line[0]] = MAPAStrategy.MAPAStrategy(line[0], int(line[1]))
            version = (line[1] + "_" + line[2]).replace("\n", "")
            write_directory = SIGNAL_FILE_PATH + version + "/"
            if not os.path.exists(write_directory):
                os.makedirs(write_directory)
    print "Strategy init complete , now proceeding with file reading \n"

    with open(filename, mode='r') as f_read:

        symbols = strategies.keys()
        current_symbol = None
        print "the symbols in symbol file are ", symbols
        for symbol in symbols:
            if symbol in filename:
                current_symbol = symbol
                break
        print "the symbol for filename ", filename, " is ", current_symbol
        date = filename.split(current_symbol)[1].replace("_", "")

        current_strategy = strategies[current_symbol]
        print current_symbol, date, filename

        with open(SIGNAL_FILE_PATH + version + "/" + current_symbol + "_" + date + "_sgnl.csv", mode="w") as f_write:
            count = 0
            for line in f_read.readlines():
                count += 1
                if count <= START_FROM_ROW:
                    continue

                line = line.replace("\n", "")
                tick_object = TickObject.TickObject(line)
                current_strategy.on_new_tick(tick_object)

                f_write.write(str(tick_object.timestamp) + ","
                                + current_symbol + ","
                                + tick_object.date + ","
                                + version + ","
                                + str(tick_object.ltp) + ","
                                + str(current_strategy.signal) + "\n")

    f_read.close()

read_file(TICK_FILE_PATH + "LAURUSLABS-EQ20161219.csv", "./symbol_list.csv")