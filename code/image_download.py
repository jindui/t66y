# coding= utf-8
import requests
import os
from multiprocessing import Pool, TimeoutError
from t66y_html import getHtml, getContent
from bs4 import BeautifulSoup
from thread_list import thread_list
import time

current_dir = os.path.dirname(os.path.realpath(__file__))

def searchImage(url):
    """搜索指定页（url）中符合条件的帖子以及内部图片链接地址
        返回的对象{title:[imgPath]}
    """
    result = {}
    for a in thread_list(url):
        soup = BeautifulSoup(getHtml(a["href"]), "lxml")
        imglist = soup.find_all("input", type="image")
        if len(imglist) > 3:
            imagePathAry = [img["src"] for img in imglist]
            result[a["title"]] = imagePathAry
    return result

def markDir(folderName):
    """创建目录"""
    dir_path = current_dir+"/data/" + folderName
    os.mkdir(dir_path)
    return dir_path

def download(dirPath,fileName,url):
    try:
        pic = getContent(url)
    except requests.exceptions.ConnectionError:
    	print '图片无法下载'
    fp = open(dirPath + "/" +fileName, 'wb')
    fp.write(pic)
    fp.close()
    print fileName

if __name__ == "__main__":
    #print ["http://t66y.com/thread0806.php?fid=16&search=&page=%d"%i for i in  range(1,10)]
    result = searchImage("http://t66y.com/thread0806.php?fid=16&search=&page=1")
    print "search over"
    pool = Pool(processes=10)  # start 10 worker processes
    for k, v in result.iteritems():
        dirPath = markDir(k)
        for path in v:
            pool.apply_async(download, (dirPath, os.path.basename(path), path))
    pool.close()
    pool.join()




