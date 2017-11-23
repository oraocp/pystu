# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# 文件目的：学习Python3中标准urllib库的用法
# 创建日期：2017/11/23

"""
urllib是python2,3的一个获取url(Uniform Resource Locators,统一资源定址器)了，
我们可以利用它来抓取远程的数据进行保存.


演示内容包括：
1. urllib.robotparser解析后代表参数
2. urllib.request.urlopen(url, data=None, [timeout, ]*,
       cafile=None, capath=None, cadefault=False, context=None)
data参数默认为None，当data参数不为空的时候，urlopen（）提交方式为Post


"""

from urllib import robotparser
from urllib.parse import urljoin

# ===================================================================
# 抓取协议robotparser的用法
# ===================================================================

PATHES = [
    '/',
    '/search',
    '/docs/1',
    '/plus/kindeditor',
    '/tags/',
]


def parse_robot(url, agentName):
    parser = robotparser.RobotFileParser()
    parser.set_url(url)
    parser.read()
    print('parser.entries:', str(parser.entries))
    print('allow_all:', str(parser.allow_all))
    print('disallow_all:', str(parser.disallow_all))
    print('crawl_delay:', str(parser.crawl_delay(agentName)))
    print('request_rate:', str(parser.request_rate(agentName)))
    print('mtime:', str(parser.mtime()))
    # 检查路径是否允许抓取，使用正则进行检验
    for path in PATHES:
        print('%s:%s' % (parser.can_fetch(agentName, path), path))


# ===================================================================
#  主函数
# ===================================================================

URL_BASE = 'http://www.iplaypy.com/'
ROBOT_URL = urljoin(URL_BASE, 'robots.txt')
AGENT_NAME = 'IPLAYPYTHON'

if __name__ == '__main__':
    print('解析ROBOT文本...')
    parse_robot(ROBOT_URL, AGENT_NAME)
