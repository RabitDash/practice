import requests
# import re
from bs4 import BeautifulSoup
import time
courl = "https://e-hentai.org/?page={}"

def getContent(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    return soup



def getImage(soup):
    src = soup.find_all('div', {'class': 'it5'})
    name = soup.find_all('div', {'class': 'it2'})
    print(src,name)
    for (i, j) in zip(src, name):
        if (j.find('img') is None) | (i is None):
            continue
        else:
            f.write("name: "+i.find('a').get_text()) # get name
            f.write("title_pic link: "+j.find('img').get('src')) # get title_pic link
            f.write("manga link: "+i.find('a').get('href')) # get manga link
            f.write("\n")
    return None

page_num = 14333
f = open('hentai_log', 'a')
for i in range(1, page_num + 1):
    soup = getContent(courl.format(i))
    print(soup)
    getImage(soup)
    print("fetching content of page{}".format(i))
    time.sleep(1)

# print("total number:{}".format(page_num))
f.close()
