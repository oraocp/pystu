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

from urllib import robotparser, request
from urllib.error import URLError
from urllib.parse import urljoin, urlencode

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
# 发起请求，接收响应
# ===================================================================

def download_page(url, encode='utf-8'):
    print('下载页面:', url)
    # 设置Header信息，模拟浏览器， 跳过反爬虫的设置
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
    }
    # 直接用urllib.request模块的urlopen（）获取页面，page的数据格式为bytes类型，需要decode（）解码，转换成str类型
    res = request.urlopen(url, header=header)
    page = res.read()
    page = page.decode(encode)
    print(page)


def post_request(url, data=None):
    print('向页面{%s}发送请求:', url)
    if data:
        print('请求参数为:', data)
    try:
        rpdata = urlencode(data).encode('utf-8')
        req = request.Request(url, data=rpdata)
        content = request.urlopen(req).read().decode('utf-8')
        print('响应结果为：', content)
        return True
    except URLError as e:
        print(e.reason)
        return False


def use_proxy(proxy_addr, url):
    proxy = request.ProxyHandler({'http': proxy_addr})
    opener = request.build_opener(proxy, request.HTTPHandler)
    request.install_opener(opener)
    data = request.urlopen(url).read().decode('utf-8')
    return data


# ===================================================================
# Cookie的使用
# ===================================================================


# ===================================================================
#  主函数
# ===================================================================

URL_BASE = 'http://www.iplaypy.com/'
ROBOT_URL = urljoin(URL_BASE, 'robots.txt')
AGENT_NAME = 'IPLAYPYTHON'

if __name__ == '__main__':
    print('解析ROBOT文本...')
    parse_robot(ROBOT_URL, AGENT_NAME)

    download_page(r'http://www.baidu.com')

    # 提示 UnicodeDecodeError: 'utf-8' codec can't decode byte 0xcd in position 956: invalid continuation byte
    # download_page(r'http://www.163.com')

    download_page(r'http://www.163.com', 'GBK')

    post_request(r'http://www.lagou.com/jobs/positionAjax.json?',
                 data={
                     'first': 'true',
                     'pn': 1,
                     'kd': 'Python'})
