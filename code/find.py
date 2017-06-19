# coding= utf-8
import requests	
from bs4 import BeautifulSoup
from thread_list import thread_list

txt = "1Pondo-072216_344".decode("utf-8")
page_list = [i for i in range(46, 100)]  
result=None
flag = False
for page in page_list:
	list = thread_list("http://t66y.com/thread0806.php?fid=2&search=&page="+str(page))	
	print "search page "+str(page)
	for a in list:
		flag = a["title"].find(txt) !=-1
		if flag:
			result = a
			break
	if flag:
			break		
			
print result

