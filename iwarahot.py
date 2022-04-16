import requests
from lxml import etree
import youtube_dl
import sys

def hoturl(url):
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
    }
    requests.packages.urllib3.disable_warnings()
    proxies = {
        'http' : 'http://127.0.0.1:7890',
        'https' : 'http://127.0.0.1:7890'
    }
    urlpage = requests.get(url=url,headers=headers,verify=False,proxies=proxies)
    xmlselector = etree.HTML(urlpage.content.decode('utf-8'))
    hoturl = xmlselector.xpath('/html/body/div/main/div[1]/article/header/figure/a/@href')
    username = xmlselector.xpath('/html/body/div/main/div[1]/article/section[1]/a/div')
    return[hoturl[0],username[0].text]
def iwarahot():
    url = "https://oreno3d.com/?sort=hot"
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36",
        "Referer":"https://oreno3d.com/"
    }
    requests.packages.urllib3.disable_warnings()
    proxies = {
        'http' : 'http://127.0.0.1:7890',
        'https' : 'http://127.0.0.1:7890'
    }
    hotpage = requests.get(url=url,headers=headers,verify=False,proxies=proxies)
    xmlselector = etree.HTML(hotpage.content.decode('utf-8'))
    hostlist = xmlselector.xpath('//article/a/@href')
    return hostlist

def iwaradownload(url,username):
    ydl_opt ={
        'outtmpl': '.\\' + username + '\\' + '%(title)s.%(ext)s',
        'proxy' : 'http://127.0.0.1:7890',
        'format' : 'best'
    }
    with youtube_dl.YoutubeDL(ydl_opt) as ydl:
        result = ydl.download(url)


if __name__ =='__main__':
    ilist = iwarahot('https://oreno3d.com/?sort=hot')
    for a in ilist:
        b = hoturl(a)
        try:
            iwaradownload((b[0],), b[1])
        except:
            continue
