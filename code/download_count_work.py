# coding= utf-8
import requests
from bs4 import BeautifulSoup
from thread_list import thread_list
from download_count import download_count

list = thread_list("http://t66y.com/thread0806.php?fid=2&search=&page=45")
result = {}
for a in list :
	down_count = download_count(a["href"])
	if down_count != 0 :
		result[a["href"]]=down_count
		print a["href"] + "          "+str(down_count)
print sorted(result.iteritems(), key=lambda d:d[1], reverse = True ) 
