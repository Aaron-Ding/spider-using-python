from urllib import request
from bs4 import BeautifulSoup
import re 
import sys

if __name__ == "__main__":
    file = open('python爬虫小说.txt', 'w', encoding='utf-8')
    #一念永恒小说目录地址
    target_url = 'http://www.biqukan.com/1_1094/'
    #User-Agent
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    target_req = request.Request(url = target_url, headers = head)
    target_response = request.urlopen(target_req)
    target_html = target_response.read().decode('gbk','ignore')
    #创建BeautifulSoup对象
    listmain_soup = BeautifulSoup(target_html,'lxml')
    charpters = listmain_soup.find_all('div',class_ = 'listmain')
    download_soup = BeautifulSoup(str(charpters),'lxml')
    numbers = (len(download_soup.dl.contents)-1)/2-8  
    index = 1 
    begin_flag = False 
    for child in download_soup.dl.children:
        if child != '\n':
            if child.string == u"《一念永恒》最新章节列表": 
                begin_flag = True
            if child.string == u"《一念永恒》正文卷":
                begin_flag = False
            if begin_flag == True and child.a != None:
                download_url = "http://www.biqukan.com" + child.a.get('href')
                download_req = request.Request(url = download_url, headers = head)
                download_response = request.urlopen(download_req)
                download_html = download_response.read().decode('gbk','ignore')
                download_name = child.string
                zhengwen = BeautifulSoup(download_html,'lxml')
                xiaoshuozhengwen =zhengwen.find_all(id='content', class_= 'showtxt')
                finaltext = BeautifulSoup(str(xiaoshuozhengwen),'lxml')
                write_flag = True
                file.write(download_name + '\n\n')
                for writeintext in finaltext.div.text.replace('\xa0',''):	
                    if writeintext == 'h':
                        write_flag = False 
                    if write_flag == True and writeintext != '':
                        file.write(writeintext)
                    if write_flag == True and writeintext =='\r':
                        file.write('\n')
                file.write('\n\n')
                sys.stdout.write("已下载:%.3f%%" % float(index/numbers) + '\r')
                sys.stdout.flush()
                index += 1
    file.close()