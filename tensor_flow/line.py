import tensorflow as tf
import pandas as pd
import matplotlib
# matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


# python -m pip install pandas -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
# python -m pip install matplotlib -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com

class Solution(object):
    def tensor(self):
        print("tf version: {}".format(tf.__version__))
        data = pd.read_csv("./Income1.csv")
        print(data)
        plt.scatter(data.Education, data.Income)
        plt.show()
        plt.savefig("one.png")


if __name__ == '__main__':
    solution = Solution()
    solution.tensor()
