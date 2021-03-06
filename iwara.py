import requests
from lxml import etree
import youtube_dl
import sys

def iwaradownloader(url):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
    }
    requests.packages.urllib3.disable_warnings()
    proxies = {
        'http' : 'http://10.10.10.1:7890',
        'https' : 'http://10.10.10.1:7890'
    }
    response = requests.get(url=url,headers=headers,verify=False,proxies=proxies)
    xmlselector = etree.HTML(response.content.decode('utf-8'))
    author = xmlselector.xpath('//h1[@class]')
    username = str(author[0].text)[0:-9]
    lists = xmlselector.xpath('//h3/a/@href')
    dlist = []
    for a in lists:
        dlist.append("https://ecchi.iwara.tv" + a)
    print(dlist)
    ydl_opt ={
        'outtmpl': '.\\' + username + '\\' + '%(title)s.%(ext)s',
        'proxy' : 'http://10.10.10.1:7890',
        'format' : 'best'
    }
    for b in dlist:
        try:
            with youtube_dl.YoutubeDL(ydl_opt) as ydl:
                result = ydl.download((b,))
        except:
            continue


if __name__ =='__main__':
    urls = ["https://ecchi.iwara.tv/users/xyz/videos" , "https://ecchi.iwara.tv/users/xyz/videos?page=1"]
    for url in urls:
        try:
            iwaradownloader(url)
        except:
            continue
