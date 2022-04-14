import urllib.request
from lxml import etree
import youtube_dl
import sys

def iwaradownloader(url):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
    }
    request = urllib.request.Request(url=url,headers=headers)
    response = urllib.request.urlopen(request,timeout=30)
    xmlselector = etree.HTML(response.read().decode('utf-8'))
    author = xmlselector.xpath('//h1[@class]')
    username = str(author[0].text)[0:-9]
    lists = xmlselector.xpath('//h3/a/@href')
    dlist = []
    for a in lists:
        dlist.append("https://ecchi.iwara.tv" + a)
    ydl_opt ={
        'outtmpl': '.\\' + username + '\\' + '%(title)s.%(ext)s',
        'proxy' : 'http://127.0.0.1:7890',
        'format' : 'best'
    }
    with youtube_dl.YoutubeDL(ydl_opt) as ydl:
        result = ydl.download(dlist)

if __name__ =='__main__':
    urls = ["https://ecchi.iwara.tv/users/m9F/videos" , "https://ecchi.iwara.tv/users/Ponkanman/videos"]
    for url in urls:
        iwaradownloader(url)
