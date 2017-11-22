"""
文档目的：演示Python中数字类型函数的用法
创建日期：2017/11/14

注： 不可命名为numbers, 会与标准库中名字重名， 影响使用

演示内容包括：
1.整数
Python可以处理任意大小的整数，当然包括负整数
十六进制用0x前缀

2.浮点数
浮点数也就是小数，之所以称为浮点数，是因为按照科学记数法表示时，一个浮点数的小数点位置是可变的，
比如，1.23x10^9和12.3x10^8是相等的

整数和浮点数在计算机内部存储的方式是不同的，整数运算永远是精确的（除法难道也是精确的？是的！），
而浮点数运算则可能会有四舍五入的误差。

3.布尔值
布尔值和布尔代数的表示完全一致，一个布尔值只有True、False两种值，要么是True，要么是False
布尔值可以用and、or和not运算。

4.空值
空值是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值。

"""

_max_thresholds = 0x23
_high_temperature = 36.23


def handle_inter():
    print("max_thresholds = ", _max_thresholds)
    # 整数相除会得到浮点数
    print("11 / 4 = ", 11 / 4)
    print("11 % 4 = ", 11 % 4)
    print("2.5 + 10/4 = ", 2.5 + 10 / 4)


def handle_float():
    print("_high_temperature = ", _high_temperature)


def handle_bool():
    print("(20==2*10) = ", (20 == 2 * 10))
    a = True
    print("(a and 'a=T' or 'a=F')=", a and 'a=T' or 'a=F')
    print("('a=T' or 'a=F')=", 'a=T' or 'a=F')


if __name__ == "__main__":
    handle_inter()
    handle_float()
    handle_bool()
