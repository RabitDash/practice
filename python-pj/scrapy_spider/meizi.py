import requests
from bs4 import BeautifulSoup
import time
courl = "http://www.mzitu.com/zipai/comment-page-{}/#comments"

def getContent(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    return soup

def getPageNum(soup):
    maxi = 0
    lista = soup.find_all('a', {'class': 'page-numbers'})
    # print(lista)
    for i in lista:
        if i.get_text() is not '':
            tmp = int(i.get_text())
            maxi = max(tmp, maxi)
    # print("page_num={}".format(maxi))
    return maxi # int

def getImage(soup):
    src = soup.find_all('div', {'class': 'comment-body'})
    for i in src:
        f.write(i.find('img').get('src')+'\n')
    return None # list

page_num = getPageNum(getContent(courl.format(1)))
f = open('log', 'a')
for i in range(1, page_num + 1):
    soup = getContent(courl.format(i))
    getImage(soup)
    time.sleep(0.35)

print("total number:{}".format(page_num))
f.close()
