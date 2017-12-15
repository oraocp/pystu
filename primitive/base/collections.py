"""
文档目的：演示Python中集合的用法
创建日期：2017/12/14

演示内容包括：
"""

import math
from django.core.paginator import Paginator, EmptyPage


# ====================================================================
# 　～ 列表相关函数操作

def list_demo():
    L = ['spam', 'eggs', 'eat', 'more', 'easy']
    print('Length(L)=%i' % len(L))
    print('Legnth(L)/2.ceil=%i' % math.ceil(len(L) / 2))
    print('Legnth(L)/2.floor=%i' % math.floor(len(L) / 2))
    for i, s in enumerate(L):
        print('L[%i]=["%s"]' % (i, s))


# ====================================================================
# 　～ 分页列表相关函数操作

def Paginator_demo():
    NUM = []
    for i in range(1, 26):
        NUM.append(i * i)
    print(NUM)
    pages = Paginator(NUM, 10)
    print("Total pages is %i" % pages.num_pages)
    p = pages.page(pages.num_pages)
    print("The Last page startindex=%i, endindex=%i, counts=%i" % (p.start_index(), p.end_index(), len(p.object_list)))
    try:
        pages.page(pages.num_pages + 1)
        print('Error')
    except EmptyPage:
        print('Get the %ith Pages raises EmptyPage Expection.' % (pages.num_pages + 1))


# ===================================================================
# 主函数
# ===================================================================

if __name__ == "__main__":
    list_demo()
    Paginator_demo()
