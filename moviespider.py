import requests
from bs4 import BeautifulSoup
import threading
import re,os,sqlite3
moviehtml=[]
conn=sqlite3.connect('E:\demo\db.sqlite3')
cur=conn.cursor()
indexurl=r'http://www.qiaotv.com/dianying/index.html'
homepage='http://www.qiaotv.com{0}'
pages=[indexurl]

def gethtmltext(url):       #获取响应
    try:
        response=requests.get(url,timeout=10)
        response.raise_for_status()
        response.encoding=response.apparent_encoding
        #print(response.status_code)
        return response.text

    except:
        print('请求有误！')
def geturl(html):       #获取电影链接
    #soup=BeautifulSoup(html,'html.parser')
    reg = re.compile(r'<a class="alink" href="(/dianying/.*?/)" title="(.*?)">')
    urllist=reg.findall(str(html))
    #gethtml=soup.find_all('a',class_='alink')
    #with open(r'e:/movies.txt','a') as file:
    for i in urllist:
        #file.write()
        ii=homepage.format(i[0])
        cur.execute(r"insert into movie_demomovielist('link','moviename')values('{0}','{1}');".format(ii,i[1]))
    conn.commit()
def allpage():
    for page in range(988):
        page1=r'http://www.qiaotv.com/dianying/index{0}.html'.format(page)
        pages.append(page1)
    pagelist=set(pages)
    return pagelist
def main():
    x = allpage()
    for x1 in x:
        y = gethtmltext(x1)
        geturl(y)
        print('爬取中，')
if __name__=='__main__':
    try:
        main()
        cur.close()
        conn.close()
    except:
        cur.close()
        conn.close()
    print('爬取结束')