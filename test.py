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
import parse_log as parseLog

def process(logfilename, output_dir, refresh = 0):

    titile_1 = "test loss"
    titile_2 = "train loss"
    titile_3 = "test accuracy"
    titile_4 = "test top1/acc"
    titile_5 = "test top5/acc"

    str_accName_org = "accuracy"
    str_accName_1 = "top1/acc"
    str_accName_5 = "top5/acc"

    if refresh > 0:
        plt.ion()
    
    fig, ax1 = plt.subplots(figsize=(8, 6))
    ax2 = ax1.twinx()

    ax1.set_xlabel(titile_1)
    ax1.set_ylabel(titile_2)
    ax2.set_ylabel(titile_3)

    fig.canvas.set_window_title(logfilename)

    bFirstTime = True
    # 是否只有一个 Acc 结果
    bOneAcc = True

    while True:
        print 'Refresh at ' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if bFirstTime == True:
            # 如果解析不出来 csv 文件，那么就继续等待
            train_dict_list, test_dict_list = parseLog.parse_log(logfilename)
            parseLog.save_csv_files(logfilename, output_dir, train_dict_list,
                                test_dict_list)
            if os.path.isfile(logfilename + ".train") == False or os.path.isfile(logfilename + ".test") == False:
                print 'Read Log 2 CSV fail at ' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                plt.pause(60)
                continue
            train_log = pd.read_csv(logfilename + ".train")
            test_log = pd.read_csv(logfilename + ".test")

            if str_accName_org in list(train_log):
                bOneAcc = True
            else:
                bOneAcc = False                

            l1,=ax2.plot(train_log["NumIters"], train_log["loss"], color='b', label=titile_2)
            l2,=ax2.plot(test_log["NumIters"], test_log["loss"], color = 'g', label=titile_1)

            if bOneAcc == True:
                l3,=ax1.plot(test_log["NumIters"], test_log[str_accName_org], color = 'r', label=titile_3)
                plt.legend([l1, l2, l3],[titile_2, titile_1, titile_3],loc="upper left") 
            else:
                l3,=ax1.plot(test_log["NumIters"], test_log[str_accName_1], color = 'r', label=titile_4)
                l4,=ax1.plot(test_log["NumIters"], test_log[str_accName_5], color = 'm', label=titile_5)
                plt.legend([l1, l2, l3, l4],[titile_2, titile_1, titile_4, titile_5],loc="upper left") 
            
            # 如果只是想看一次图
            if refresh == 0:
                plt.savefig(logfilename + ".png")    
                plt.show()
                break
            bFirstTime = False
            plt.pause(60)
            continue

        # 移除原有的线
        l1.remove()
        l2.remove()
        l3.remove()

        if bOneAcc == False:
            l4.remove()

        # 重新读取绘制
        train_dict_list, test_dict_list = parseLog.parse_log(logfilename)
        parseLog.save_csv_files(logfilename, output_dir, train_dict_list,
                                test_dict_list)

        train_log = pd.read_csv(logfilename + ".train")
        test_log = pd.read_csv(logfilename + ".test")

        if str_accName_org in list(train_log):
            bOneAcc = True
        else:
            bOneAcc = False  

        l1,=ax2.plot(train_log["NumIters"], train_log["loss"], color='b', label=titile_2)
        l2,=ax2.plot(test_log["NumIters"], test_log["loss"], color = 'g', label=titile_1)

        if bOneAcc == True:
            l3,=ax1.plot(test_log["NumIters"], test_log[str_accName_org], color = 'r', label=titile_3)
            plt.legend([l1, l2, l3],[titile_2, titile_1, titile_3],loc="upper left") 
        else:
            l3,=ax1.plot(test_log["NumIters"], test_log[str_accName_1], color = 'r', label=titile_4)
            l4,=ax1.plot(test_log["NumIters"], test_log[str_accName_5], color = 'm', label=titile_5)
            plt.legend([l1, l2, l3, l4],[titile_2, titile_1, titile_4, titile_5],loc="upper left") 

        plt.pause(60)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('log', help="log file path")
    parser.add_argument('output_dir', help="output_dir path")
    parser.add_argument('refresh', help="refresh(>0) or plot once (==0)")
    args = parser.parse_args()

    process(args.log,args.output_dir, int(args.refresh))