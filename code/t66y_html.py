# coding= utf-8
import requests
proxies = {
        "http": "http://127.0.0.1:1080",
}

def getHtml(url,timeout=5):
    """获取html文本内容"""
    r = requests.get(url, proxies=proxies,timeout=timeout)
    r.encoding = 'gbk'
    return  r.text

def getContent(url,timeout=5):
    """获取二进制内容"""
    r = requests.get(url, proxies=proxies,timeout=timeout)
    return r.content