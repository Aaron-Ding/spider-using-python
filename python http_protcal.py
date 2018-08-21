from urllib import request
from urllib import error
from urllib import parse
from http import cookiejar

if __name__ == '__main__':

	login_url = 'https://blog.mimvp.com/wp-login.php'
	
	user_agent = r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
	
	head = {'user-Agent': user_agent, 'Connection': 'keep-alive'}

	Login_Data={}
	
	Login_Data['emp_no']='ithomer'
	Login_Data['redirect_to'] = 'https://blog.mimvp.com/wp-admin/'
	##Login_Data['password']='123456'
	##Login_Data['wp-submit']='登录'
	Login_Data['testcookie']='1'
	Loginpostdata = parse.urlencode(Login_Data).encode('utf-8')
	
	cookie = cookiejar.CookieJar()
	
	handler = request.HTTPCookieProcessor(cookie)
	
	opener = request.build_opener(handler)
	
	req = request.Request(url=login_url, data=Loginpostdata, headers=head)
	
	response = opener.open(req)
	
	html = response.read().decode('utf-8')
	print('testtesttest:%s' % html)
	##