from urllib import request
import json
from urllib import parse
import sys
def translateyoudao():
	Request_URL = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=https://www.baidu.com/link"
	form_Data={}
	form_Data['type']='AUTO'
	form_Data['i']="The sole effect that this renaming has is to confuse and waste time"
	form_Data['doctype']='JSON'
	form_Data['xmlversion']='2.1'
	form_Data['keyfrom']='fanyi.web'
	form_Data['ue']='ue:UTF-8'
	form_Data['action']='FY_BY_REALTIME'
	
	
	
	data = parse.urlencode(form_Data).encode('utf-8')
	##转换form data 的格式
	response = request.urlopen(Request_URL,data)
	##传递需要request的网址和数据到response
	html = response.read().decode('utf-8')
	print(html)
	translate_result = json.loads(html)
	translate_result= translate_result['translateResult'][0][0]['tgt']
	print(translate_result)
	

if __name__ == "__main__":
   translateyoudao()
   input()