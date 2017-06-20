# coding= utf-8
import requests
from bs4 import BeautifulSoup
from  t66y_html import getHtml

def thread_list(url):
	try:
		soup = BeautifulSoup(getHtml(url),"lxml")
		alist = soup.find_all("a",id=True,target="_blank")
		result = []
		for child in alist:
			result.append({"title":child.text,"href":"http://t66y.com/"+child["href"]})
		return result
	except requests.exceptions.ProxyError:
		print "代理未开启"
		return []
#print soup.prettify("gbk")

if __name__ == "__main__":
	list = thread_list("http://t66y.com/thread0806.php?fid=2&search=&page=2")
	print len(list)
	print list