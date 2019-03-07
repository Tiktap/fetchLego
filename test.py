#coding:utf-8
import urllib.request
from bs4 import BeautifulSoup
class LogoItem:       # 定义父类
   def log(self):
 	  print(self.name)

page = urllib.request.urlopen('http://www.18pk.com/lego/')#打开网页
htmlcode = page.read()#读取页面源码
soup = BeautifulSoup(htmlcode, 'html.parser')   #文档对象
# s = soup.find(text='Heading')
# while getattr(s, 'name', None) != 'ul':
#     s = s.next
# 类名为xxx而且文本内容为hahaha的div



for j in soup.find_all('div',class_='d-box'):#,string='更多'
    k = j.find('div',class_='d-box-con');
    img = j.find('img');
    imageUrl = img.get('src');
    print(imageUrl)
    code = k.find(text='编号');
    item = LogoItem()
    price = k.find(text='换算价格');
    item.price = '0';
    item.brickCount = '0';
    if price:
   	   item.price = price.next;

    brickCount = k.find(text='积木数');
    if brickCount:
       item.brickCount = brickCount.next;

    item.imageUrl = imageUrl;

    publishYear = k.find(text='发售年份');
    item.publishYear = publishYear.next;
    

    item.code = code.next;
    name = k.find('a',class_='d-con-title');
    item.name = name.next;
    message = '''
				Name %s:
				Code:%s
				Price:%s
				Url:%s
				Year:%s
				'''%(item.name,item.code,item.price,item.imageUrl,item.publishYear);
    print(message)
#print htmlcode#在控制台输出