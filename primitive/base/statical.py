"""
文档目的：演示Python中的统计模块的用法
创建日期：2017/11/16

演示内容包括：
1. 平均数
2. 中位数
3. 高低中位数
4. 总体方差 = 总体标准差^2
5. 样本方差 = 样本标准差^2

"""

import math
from fractions import Fraction as F
from statistics import mean, median, median_low, median_high, pvariance, pstdev

# ======定义测试数据======== #
data = [i for i in range(1, 5)]
data2 = [i for i in range(1, 6)]
dataF = [F(3, 7), F(1, 21), F(5, 3), F(1, 3)]


def calc_mean():
    print('测试平均数 ...')
    print("sum(data)/len(data)=", sum(data) / len(data))
    print("mean(data)=", mean(data))
    print("mean(dataF)=%4.2f" % mean(dataF))
    print('')


def calc_median():
    print('测试中位数 ...')
    print("median(data)=%4.2f" % median(data))  # [1,2,3,4]取中间两数平均值
    print("median(data2)=%4.2f" % median(data2))  # [1,2,3,4,5]取中间值
    print("median(dataF)=%4.2f" % median(dataF))
    print('')

    print('测试高、低中位数 ...')
    print("median_low(data)=%4.2f" % median_low(data))  # [1,2,3,4]取中间小值2
    print("median_high(data)=%4.2f" % median_high(data))  # [1,2,3,4]取中间大值3
    print("median_low(data2)=%4.2f" % median_low(data2))  # [1,2,3,4,5]取中间小值3
    print("median_high(data2)=%4.2f" % median_high(data2))  # [1,2,3,4,5]取中间大值3
    print("median_grouped(dataF)=%4.2f" % median(dataF))
    print('')


def calc_pvariance():
    print('测试总体方差 ...')
    '''
    data=[1,2,3,4] 均值为2.5
    '''
    print((sum([(x - 2.5) ** 2 for x in data]) / len(data)))
    print("pvariance(data)=%4.2f" % pvariance(data))
    print("pvariance(data, mu)=%4.2f" % pvariance(data, mean(data)))
    print("pvariance(data, 12)=%4.2f" % pvariance(data, 12))  # 计算时并不会用给出的平均数值

    print("pvariance(data2)=%4.2f" % pvariance(data2))
    print("pvariance(data2, mu)=%4.2f" % pvariance(data2, mean(data)))
    print("pvariance(dataF)=%4.2f" % pvariance(dataF))
    print('')


def calc_pstdev():
    print('测试总体标准差 ...')
    print("pstdev(data)=sqrt(pvariance(data))=%4.2f" % math.sqrt(pvariance(data)))
    print("pstdev(data)=%4.2f" % pstdev(data))
    print("pstdev(data, mu)=%4.2f" % pstdev(data, mean(data)))
    print("pstdev(data, 12)=%4.2f" % pstdev(data, 12))  # 计算时并不会用给出的平均数值
    print("pstdev(data2)=%4.2f" % pstdev(data2))
    print("pstdev(data2, mu)=%4.2f" % pstdev(data2, mean(data)))
    print("pstdev(dataF)=%4.2f" % pstdev(dataF))
    print('')


if __name__ == "__main__":
    calc_mean()
    calc_median()
    calc_pvariance()
    calc_pstdev()
