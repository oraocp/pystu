# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# 文件目的：演示Python中的参数解析类的用法
# 创建日期：2017/11/14
# -------------------------------------------------------------------------

"""
演示内容包括：
$ python prog.py 1 2 3 4
4 （显示最大值）

$ python prog.py 1 2 3 4 --sum
10 （显示求和）

$ python prog.py -h
整数处理函数.

positional arguments:
  N           整数加法器的入参

optional arguments:
  -h, --help  show this help message and exit
  --sum       计算整数和（默认：找到最大值）
"""

from argparse import ArgumentParser


def main():
    # 1.创建解析器
    parser = ArgumentParser(description='整数处理函数.')
    # 2.向解析器中加入参数
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='整数加法器的入参')
    parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max,
                        help='计算整数和（默认：找到最大值）')
    # 3.解析后得到参数对象
    args = parser.parse_args()
    print(args.accumulate(args.integers))


if __name__ == "__main__":
    main()
