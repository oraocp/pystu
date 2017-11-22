"""
文档目的：演示Python中lambda表达式的概念和用法
创建日期：2017/11/14

演示内容包括：
1. lambda表达式的概念
lambda只是一个表达式，函数体比def简单很多。
lambda表达式是起到一个函数速写的作用。允许在代码内嵌入一个函数的定义。
lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。

2.lambda表达式的用法

"""
from functools import reduce


def factorial(n):
    '''
    求数n的阶乘
    :param n: 数n
    :return:  数n的阶乘
    '''
    return reduce(lambda x, y: x * y, range(1, n + 1))


if __name__ == "__main__":
    print('factorial(10)=', factorial(10))
