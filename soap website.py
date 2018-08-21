from urllib import request
from bs4 import BeautifulSoup
import sys
if __name__ == "__main__" :

    download_url = "http://www.biqukan.com/1_1094/" 
    
    head = {}
    
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    
    download_req = request.Request(url = download_url, headers = head)
    
    download_response = request.urlopen(download_req)
    
    download_html = download_response.read().decode('gbk','ignore')
    
    soup_texts = BeautifulSoup(download_html,'lxml')
    
    text = soup_texts.find_all('div',class_ = 'listmain')
    
    texts = BeautifulSoup(str(text),'lxml')
    
    begin_flag = False
    
    for child in texts.dl.children:
        #滤除回车
        if child != '\n':
            #找到《一念永恒》正文卷,使能标志位
            if child.string == u"《一念永恒》最新章节列表": 
                begin_flag = True
            if child.string == u"《一念永恒》正文卷":
                begin_flag = False
            #爬取链接
            if begin_flag == True and child.a != None:
                download_url = "http://www.biqukan.com" + child.a.get('href')
                download_name = child.string
                print(download_name + " : " + download_url)
		input()

				
				
	
           