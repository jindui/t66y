# coding= utf-8
import requests
from bs4 import BeautifulSoup


def download_count(url):
	proxies = {
	  "http": "http://127.0.0.1:1080",
	}
	
	r = requests.get(url, proxies=proxies)
	r.encoding='gbk'
	soup = BeautifulSoup(r.text,"lxml")

	alist = soup.find_all("a")
	for child in alist:
		if child.text.startswith("http://www.rmdown.com/link.php?hash=") :
			seed = requests.get(child.text, proxies=proxies)
			seedSoup = BeautifulSoup(seed.text,"lxml")
			for contentStr in seedSoup.form.table.tr.td.strings:
				if contentStr.strip().startswith("downloaded:"):
					return int(contentStr.strip()[12:])
	return 0
#print soup.prettify("gbk")

if __name__ == "__main__":
    down_count = download_count("http://t66y.com/htm_data/2/1706/2462520.html")
    print down_count