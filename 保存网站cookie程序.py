from urllib import request
from http import cookiejar



if __name__ == '__main__':

	filename = 'cookie.txt'
	##声明一个文件用来保存取到的cookie
	cookie=cookiejar.MozillaCookieJar(filename)
	##用MozillaCookieJar就可以把cookie 保存到file里面
	handler = request.HTTPCookieProcessor(cookie)
	##request 一个HTTPCookieProcessor就可以取到网页中的cookie
	opener = request.build_opener(handler)
	
	response = opener.open('https://blog.baidu.com/')
	
	
	cookie.save(ignore_discard=True, ignore_expires=True)
	
	
	