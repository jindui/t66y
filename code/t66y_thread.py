# coding= utf-8
"""
处理帖子内容
"""
import re
import  time
import requests
from bs4 import BeautifulSoup
from  http import getHtml

def thread_list(url):
	'''
	获取帖子列表
	:param url:
	:return:
	'''
	try:
		soup = BeautifulSoup(getHtml(url),"lxml")
		alist = soup.find_all("a",id=True,target="_blank")
		result = []
		for child in alist:
			result.append({"title":child.text,"href":"http://t66y.com/"+child["href"]})
		return result
	except requests.exceptions.ProxyError:
		print "代理未开启"
	except requests.exceptions.ReadTimeout:
		print "timeout:"+url
	return []
#print soup.prettify("gbk")

def post_date(url):
	'''
	返回帖子发布时间
	:param url:
	:return:
	'''
	soup = BeautifulSoup(getHtml(url), "lxml")
	return post_date_soup(soup)

def	post_date_soup(soup):
	'''
	返回帖子发布时间
	:param soup:
	:return:
	'''
	try:
		txt = soup.find("div", class_="tipad").text
		list = re.findall(r"\d{4}-\d+-\d+", txt)
		if len(list) == 1:
			return list[0]
	except :
		print "日期读取错误"
	return '1900-01-01'


if __name__ == "__main__":
	date = post_date("http://t66y.com/htm_data/16/1706/2476086.html")
	print time.strftime('%Y-%m-%d',time.localtime(time.time()))
	print date