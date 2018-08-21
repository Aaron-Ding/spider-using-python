import re
import urllib.request
import urllib.error
import urllib.parse
from urllib import request 

sum = 0 
def savepic(url,page):
	##result = {}
	html1=urllib.request.urlopen(url).read()
	html1=str(html1)
	pat1=r'<div id="plist".+? <div class="page clearfix">'
	print(pat1)
	result1=re.compile(pat1).findall(html1)
	result1=result1[0]
	imgur2 = r'<img width="200" height="200" data-img="1" src="//(.+?\.jpg)">|<img width="200" height="200" data-img="1" data-lazy-img="//(.+?\.jpg)">'
	imagelist = re.compile(imgur2).findall(result1)
	x = 1
	
	global sum	
	for imageurl in imagelist:
		imagename = 'books\\'+str(page)+'.' +str(x)+'.jpg'
		print(imagename)
		if imageurl[0]!= '':
			imageurl = 'http://'+imageurl[0]
			print(imageurl)
		else:
			imageurl = 'http://'+imageurl[1]

		print('start loading the pictures page=%d'%(page))
		
		try:
			urllib.request.urlretrieve(imageurl,filename=imagename)
		except urllib.error.URLError as e: 
			if hasattr(e,'code') or hasattr(e,'reason'):
				x+=1
		print('save pic complete')
		x+=1
		sum+=1
if __name__ == "__main__":
	for i in range (1,3):
		url='https://list.jd.com/list.html?cat=1713,3287,3797&page='+str(i)
		savepic(url,i)
print("total pictures = %d"%sum)
		
		
		