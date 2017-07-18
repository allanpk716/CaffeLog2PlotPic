import pandas as pd
from matplotlib import *
from matplotlib.pyplot import *
import matplotlib.pyplot as plt
import sys

def process(logfilename):
    train_log = pd.read_csv(logfilename + ".train")
    test_log = pd.read_csv(logfilename + ".test")

    titile_1 = "test loss"
    titile_2 = "train loss"
    titile_3 = "test accuracy"

    _, ax1 = plt.subplots(figsize=(15, 10))
    ax2 = ax1.twinx()

    l1,=ax1.plot(train_log["NumIters"], train_log["loss"], alpha=0.4)
    l2,=ax1.plot(test_log["NumIters"], test_log["loss"], color = 'g')
    l3,=ax2.plot(test_log["NumIters"], test_log["accuracy"], color = 'r')

    plt.legend([l1, l2, l3],[titile_2, titile_1, titile_3], loc="upper left")

    ax1.set_xlabel(titile_1)
    ax1.set_ylabel(titile_2)
    ax2.set_ylabel(titile_3)

    plt.savefig(logfilename + ".png")    
    plt.show()

if __name__ == '__main__':
    process(sys.argv[1])