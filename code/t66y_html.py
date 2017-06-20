# coding= utf-8
import requests
proxies = {
        "http": "http://127.0.0.1:1080",
}

def getHtml(url):
    """获取html文本内容"""
    r = requests.get(url, proxies=proxies)
    r.encoding = 'gbk'
    return  r.text

def getContent(url):
    """获取二进制内容"""
    r = requests.get(url, proxies=proxies)
    return r.content