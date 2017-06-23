# coding= utf-8
import requests
import os
import json
from multiprocessing import Pool, TimeoutError
from http import getHtml, getContent
from bs4 import BeautifulSoup
from t66y_thread import thread_list,post_date_soup


current_dir = os.path.dirname(os.path.realpath(__file__))

def searchImage(url,date):
    '''
    搜索指定页（url）中符合条件的帖子以及内部图片链接地址
        返回的对象{title:[imgPath]}
    :param url:
    :param date: 指定发布帖日期
    :return:
    '''
    result = {}
    for a in thread_list(url):

            soup = BeautifulSoup(getHtml(a["href"]), "lxml")
            if post_date_soup(soup) == date:
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
    result = {}
    for url in ["http://t66y.com/thread0806.php?fid=16&search=&page=%d"%i for i in range(1,20)]:
        print "read %s"%url
        result = dict(result, **searchImage(url,'2017-06-22'))
    with open('2017-06-22.json', 'w') as fp:
        json.dump(result, fp)






