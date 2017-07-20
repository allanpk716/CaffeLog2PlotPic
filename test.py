#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-20 14:08:00
# @Author  : Chin Allan
import pandas as pd
from matplotlib import *
from matplotlib.pyplot import *
import matplotlib.pyplot as plt
import sys
import argparse
import time
import datetime

def process(logfilename, refresh = 0):

    titile_1 = "test loss"
    titile_2 = "train loss"
    titile_3 = "test accuracy"

    if refresh > 0:
        plt.ion()
            
    fig, ax1 = plt.subplots(figsize=(8, 6))
    ax2 = ax1.twinx()

    ax1.set_xlabel(titile_1)
    ax1.set_ylabel(titile_2)
    ax2.set_ylabel(titile_3)
    # 第一次读取
    train_log = pd.read_csv(logfilename + ".train")
    test_log = pd.read_csv(logfilename + ".test")

    l1,=ax1.plot(train_log["NumIters"], train_log["loss"], color='b', label=titile_2)
    l2,=ax1.plot(test_log["NumIters"], test_log["loss"], color = 'g', label=titile_1)
    l3,=ax2.plot(test_log["NumIters"], test_log["accuracy"], color = 'r', label=titile_3)

    plt.legend([l1, l2, l3],[titile_2, titile_1, titile_3],loc="upper left") 
    # ax1.legend(loc="upper left")
    # ax2.legend(loc="upper left")

    fig.canvas.set_window_title(logfilename)

    if refresh == 0:
        plt.savefig(logfilename + ".png")    
        plt.show()

    bFirstTime = True

    while refresh > 0:
        print 'Refresh at ' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if bFirstTime == True:
            plt.pause(60)

        ax1.lines.pop(0)
        ax1.lines.pop(0)
        ax2.lines.pop(0)

        train_log = pd.read_csv(logfilename + ".train")
        test_log = pd.read_csv(logfilename + ".test")

        l1,=ax1.plot(train_log["NumIters"], train_log["loss"], color='b')
        l2,=ax1.plot(test_log["NumIters"], test_log["loss"], color = 'g')
        l3,=ax2.plot(test_log["NumIters"], test_log["accuracy"], color = 'r')

        if bFirstTime == True:
            bFirstTime = False
        else:
            plt.pause(60)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('log', help="log file path")
    parser.add_argument('refresh', help="refresh(>0) or plot once (==0)")
    args = parser.parse_args()

    process(args.log, int(args.refresh))