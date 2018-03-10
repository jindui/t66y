# coding= utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import requests
import os
import json
import datetime
from multiprocessing import Pool, TimeoutError
from http import getHtml, getContent
from bs4 import BeautifulSoup
from t66y_thread import thread_list,post_date_soup
import threadpool

current_dir = os.path.dirname(os.path.realpath(__file__))

def searchImage(url,date):
    '''
    搜索指定页（url）中符合条件的帖子以及内部图片链接地址
        返回的对象{title:[imgPath]}
    :param url:
    :param date: 指定发布帖日期
    :return:
    '''
    today = datetime.datetime.now().strftime("%Y-%m-%d")

    for a in thread_list(url):

            soup = BeautifulSoup(getHtml(a["href"]), "lxml")
            if post_date_soup(soup) >= date:
                pdate=post_date_soup(soup)
                if pdate >today :
                    pdate=today

                imagePathAry=[]
                imglist = soup.find_all("input", type="image")
                if len(imglist) > 3:
                    for img in imglist:
                   #     if(len(img["src"])) > 5:
                            imagePathAry.append(img["src"])
                num = a["href"].split('/')[-1]
                dir_path = current_dir + "/data/" + pdate
                dir_path = markDir(dir_path)
                dir_path = markDir(dir_path + "/" + num.split('.')[0])
                downloadmuimage(dir_path, a["title"],imagePathAry)
                   # imagePathAry = [img["src"] for img in imglist]
                result[a["title"]] = imagePathAry

    return result

def downloadmuimage(dir_path,title,imagePathAry):
    print dir_path
    markreadme(dir_path,title)
    pool = threadpool.ThreadPool(10)
    fucimagelist=[]
    for image in imagePathAry:
        fucimagelist.append(([dir_path,image],None))
    requests = threadpool.makeRequests(download, fucimagelist)
    [pool.putRequest(req) for req in requests]
    pool.wait()
    pool.dismissWorkers(10, do_join=True)



    # return

def markreadme(dirPath,text):
    fp = open(dirPath + "/" + "readme.txt", 'w')
    fp.write(text)
    fp.close()
def markDir(dir_path):
    """创建目录"""
    if(os.path.exists(dir_path)):
        return dir_path
    else:
        os.mkdir(dir_path)
    return dir_path


def download(dirPath,url):
    try:
        pic = getContent(url)
    except requests.exceptions.RequestException as e:
    	print '图片无法下载'
        print e
        return 0
    file_name = url.split('/')[-1]
    fp = open(dirPath + "/" +file_name, 'wb')
    fp.write(pic)
    fp.close()
    print file_name

if __name__ == "__main__":
    result = {}
    for url in ["http://t66y.com/thread0806.php?fid=16&search=&page=%d"%i for i in range(1,3)]:
        print "read %s"%url
        today=datetime.datetime.now().strftime("%Y-%m-%d")
        #today=u"2018-03-08"
        result = dict(result, **searchImage(url,today))
    with open(today+'.json', 'w') as fp:
        json.dump(result, fp)






