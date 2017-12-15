"""
文档目的：演示Python中字符串函数的用法
创建日期：2017/11/14

演示内容包括：
1. 转义字符串
2. raw字符串
"""

# 使用转义字符\来表示普通字符。 常用的转义字符有\n\t
__trans_str = "Python was started in 1989 by \"Guido\". \nIs it \\true\\? \tEnd"

# raw字符串, 方法为在多行字符串前面添加r
__raw_str = r"'\"To be, or not to be\": that is the question.\nWhether it\'s nobler in the mind to suffer.'"


def print_str():
    # 直接打印多个字符串， 不换行
    print('trans_str:', __trans_str)
    print('raw_str', ':', __raw_str)


def split_demo():
    # 分解字符串为数组
    str1 = 'AE,CR,DE'
    for s in str1.split(','):
        print(s)


if __name__ == "__main__":
    print_str()
    split_demo()
