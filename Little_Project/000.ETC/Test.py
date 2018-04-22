#coding:utf-8

import urllib.request
import webbrowser as web


url = 'https://fd.zaih.com/column/article/70000038528912897591'

def getHtml(url):
    page=urllib.request.urlopen(url)
    html=page.read().decode(encoding='utf-8',errors='strict')
    return html


open ('317.html','w',encoding = 'utf-8').write(getHtml(url))

web.open_new_tab('317.html')

