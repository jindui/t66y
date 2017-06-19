# coding= utf-8
import requests	
import os
from bs4 import BeautifulSoup
from thread_list import thread_list


current_dir = os.path.dirname(os.path.realpath(__file__))
list = thread_list("http://t66y.com/thread0806.php?fid=16&search=&page=1")	
for a in list:
	proxies = {
	  "http": "http://127.0.0.1:1080",
	}	
	r = requests.get(a["href"], proxies=proxies)
	r.encoding='gbk'
	soup = BeautifulSoup(r.text,"lxml")
	imglist = soup.find_all("input",type="image")	
	if len(imglist)>3:
		dir_path = current_dir+"/data/"+a["title"]
		os.mkdir(dir_path)
		i=0
		print a["title"]
		for img in imglist :
			try:
				pic= requests.get(img["src"], timeout=10)
			except requests.exceptions.ConnectionError:
				print '图片无法下载'
				continue
			fp = open(dir_path+"/"+str(i) + '.jpg','wb')
			fp.write(pic.content)
			fp.close()
			i+=1
