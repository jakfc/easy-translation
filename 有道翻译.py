import requests
import json
while(1):
	url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
	From_data={'i':'我爱中国','from':'AOTO','to':'AUTO','smartresult':'dict','salt':'15674144656582','sign':'23a854fc2c877678dccd71303d392885','ts':'1567414465658','bv':'a4f4c82afd8bdba188e568d101be3f53','doctype':'json','version':'2.1','keyfrom':'fanyi.web','action':'FY_BY_CLICKBUTTION'}
	From_data['i']=input("输入你要翻译的文字:")
	response = requests.post(url,data=From_data)
	content = json.loads(response.text)
	if From_data['i']=='exit':
		break
	print(content['translateResult'][0][0]['tgt'])