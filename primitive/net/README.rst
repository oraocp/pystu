（一）urllib库的使用

urllib包主要模块有：
1.urllib.request -----用于打开 URL网址；
2.urllib.error ---------定义了常见的urllib.request会引发的异常；
3.urllib.parse---------用于解析 URL；

robotparser解析抓取协议，可以用来读取robots文本的格式和内容，
用函数方法检查给定的User-Agent是否可以访问相应的网站资源
解析依据为：
http://www.robotstxt.org/norobots-rfc.txt

简单的来说，robots.txt文件是每个网站都应该有的，指引蜘蛛抓取和禁止抓取的一个文本格式的文件，
一些合法的蜘蛛或者叫爬虫，都是遵守这个规则的，可以控制他们的访问

(二) requests库的使用