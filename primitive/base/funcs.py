"""
文档目的：演示Python中函数式编程的概念和用法
创建日期：2017/11/14

演示内容包括：
1. 变量指向函数
   函数名其实就是指向函数的变量

2. 复合函数
   是指能接收函数作参数的函数

3. 内置的map(f, list)复合函数的用法
   它接收一个函数 f 和一个 list，并通过把函数 f 依次作用在 list 的每个元素上，得到一个新的 list 并返回

4. 内置的reduce(f, list, initializer)复合函数的用法
   reduce()函数接收的参数和 map()类似，一个函数 f，一个list，但行为和 map()不同，reduce()传入的函数 f 必须接收两个参数
   reduce()对list的每个元素反复调用函数f，并返回最终结果值

5. 函数闭包的用法
   闭包是指内层函数引用了外层函数的变量，然后返回内层函数的情况 。
   要正确使用闭包，就要确保引用的局部变量在函数返回后不能变。.

6. 装饰器的用法
   包括无参数和有参数装饰器的编写。

7. 偏函数的用法
   functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()
   可以把一个参数多的函数变成一个参数少的新函数，少的参数需要在创建时指定默认值

"""
import math
import time
from functools import reduce, wraps, partial


# ===================================================================
# 高阶函数的定义
# ===================================================================


def _add(x, y, f):
    """
    演示高阶函数的用法
    定义一个函数add，接收x,y,f三个参数
    其中x, y是数值， f是函数
    """
    assert isinstance(y, object)
    return f(x) + f(y)


def sqrt_add(x, y):
    """
    将两个数x和y的平方根相加
    :param x: 数1
    :param y: 数2
    :return: 数1和数2的平方根相和后的结果
    """
    return _add(x, y, math.sqrt)


# ===================================================================
# Python内置高阶函数的用法
# ===================================================================

def _prod(x, y):
    return x * y


def _add2(x, y):
    return x + y


def multiadd(iterable, initializer=0):
    '''
    演示reduce(iterable, initializer)的用法
    :param iterable: 可迭代的数字集合
    :param initializer: 初始参数因子
    :return: 集合数字的
    '''
    return reduce(_add2, iterable, initializer)


def multiply(iterable):
    '''
    演示reduce函数的用法
    :param iterable:
    :return:
    '''
    return reduce(_prod, iterable)


def _is_sqr(x):
    r = int(math.sqrt(x))
    return r * r == x


def filter_sqr(r):
    '''
    演示filter函数的用法
    过滤出集合中平方根是整数的数
    :param r:  集合
    :return: 平方根是整数的数
    '''
    return filter(_is_sqr, r)


def _reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0


"""
在python2中可以自定义排序算法， 在python3中已不可再使用
def sorted_reversed(r):
    '''
    演示自定义排序算法
    :param r:
    :return:
    '''
    return sorted(r, _reversed_cmp)
"""


def calc_sum(lst):
    '''
    演示返回值为函数的情形， 用于延迟计算
    :param lst: 要计算的列表
    :return: 计算和的函数
    '''

    def lazy_sum():
        return sum(lst)

    return lazy_sum


def count():
    '''
    演示函数闭包的用法。
    闭包是指内层函数引用了外层函数的变量，然后返回内层函数的情况 。
    要正确使用闭包，就要确保引用的局部变量在函数返回后不能变。
    :return: 返回分别计算1*1， 2*2， 3*3的3个函数
    '''
    fs = []
    for i in range(1, 4):
        def f(j):
            def g():
                return j * j

            return g

        r = f(i)
        fs.append(r)
    return fs


def _is_not_empty(s):
    '''
    演示匿名函数的编写
    匿名函数可用 lambda表达式来表示, 返回函数时也可返回lambda
    匿名函数有外限制， 就是只能有一个表达式， 不写return
    如本函数为检验字符串是否为空， 对应的lambda表达式为：
    lambda s: s and len(s.strip())>0
    :param s: 表达式
    :return: 是否为空
    '''
    return s and len(s.strip()) > 0


# ===================================================================
# 装饰器
# ===================================================================

def performance(f):
    @wraps(f)
    def fn(*args, **kw):
        start = time.time()
        ret = f(*args, **kw)
        end = time.time()
        print('call %s() in %fs' % (f.__name__, (end - start)))
        return ret

    return fn


@performance
def facotrial(n):
    '''
    演示无参数装饰器的用法
    打印函数执行时间
    :param n: 幂乘的最大值
    :return: 幂乘的结果
    '''
    return reduce(lambda x, y: x * y, range(1, n + 1))


def performance2(unit='ms'):
    '''
    带参数的装饰器函数首先返回一个decorator函数，再让这个decorator函数接收my_func并返回新函数
    <p>注意，@decorator可以动态实现函数功能的增加，但是，经过@decorator“改造”后的函数，和原函数相比，
    函数名不再是f， 而是@performance2中定义的wrapper，这对那些依赖于函数名的代码就会失效
    如果要让调用者看不出一个函数经过了@decorator的“改造”，就需要把原函数的一些属性复制到新函数中
    Python内置的functools可以用来自动化完成这个“复制”的任务</p>
    :param unit: 计量单位
    :return: 记录执行某方法所消耗的时间
    '''

    def perf_decorator(f):
        @wraps(f)
        def wrapper(*args, **kw):
            t1 = time.time()
            r = f(*args, **kw)
            t2 = time.time()
            t = (t2 - t1) * 1000 if unit == 'ms' else (t2 - t1)
            print('call %s() in %f %s' % (f.__name__, t, unit))
            return r

        return wrapper

    return perf_decorator


@performance2('ms')
def facotrial2(n):
    '''
    演示带参数装饰器的用法
    打印函数执行时间
    :param n: 幂乘的最大值
    :return: 幂乘的结果
    '''
    return reduce(lambda x, y: x * y, range(1, n + 1))


# ===================================================================
# 偏函数
# ===================================================================

int2 = partial(int, base=2)

'''
在Python2中，使用cmp函数来自定义比较大小，则
sorted_ignore_case = functools.partial(sorted, cmp=lambda s1, s2: cmp(s1.upper(), s2.upper()))
在Python3中，可直接使用key来指定排序前，键值要执行的函数， 更加简单
'''
sorted_ignore_case = partial(sorted, key=str.lower)
# ===================================================================
# 主函数
# ===================================================================

if __name__ == "__main__":
    print('sqrt_add(4,81)=', sqrt_add(4, 81))
    print('multiply([2,3,4])=', multiply([2, 3, 4]))
    print('multiadd([2,3,4])=', multiadd([2, 3, 4]))
    print('multiadd([2,3,4], 100)=', multiadd([2, 3, 4], 100))
    # print_iterable(filter_sqr(range(1, 101)))
    print('calc_sum([36, 5, 12, 9, 21])()=', calc_sum([36, 5, 12, 9, 21])())
    f1, f2, f3 = count()
    print('f1()=', f1(), ' f2()=', f2(), ' f3()=', f3())
    _is_not_empty = lambda s: s and len(s.strip()) > 0
    print('_is_not_empty(None) = ', _is_not_empty('TEXT'))
    print('name:', facotrial.__name__, '; facotrial(10)=', facotrial(100))
    print('name:', facotrial2.__name__, ';facotrial2(10)=', facotrial2(100))
    print("int2('1010101') = ", int2('1010101'))
    print(sorted_ignore_case(['bob', 'about', 'Zoo', 'Credit']))
