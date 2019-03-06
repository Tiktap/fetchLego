#coding:utf-8
import urllib.request
from bs4 import BeautifulSoup
page = urllib.request.urlopen('http://www.18pk.com/lego/')#打开网页
htmlcode = page.read()#读取页面源码
soup = BeautifulSoup(htmlcode, 'html.parser')   #文档对象
# 类名为xxx而且文本内容为hahaha的div
for k in soup.find_all('div',class_='d-box-con'):#,string='更多'
    str = k.find_all('div',class_='d-info-cat')
    print(str.name)
#print htmlcode#在控制台输出