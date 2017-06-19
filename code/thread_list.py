# coding= utf-8
import requests
from bs4 import BeautifulSoup


def thread_list(url):
	proxies = {
	  "http": "http://127.0.0.1:1080",
	}
	try:
		r = requests.get(url, proxies=proxies)
		r.encoding='gbk'
		soup = BeautifulSoup(r.text,"lxml")
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