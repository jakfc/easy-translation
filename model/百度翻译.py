import requests
while(1):
  data = {'kw':'shit'}
  data['kw']=input('输入要翻译的单词\n')
  if data['kw']=='quit':
    break
  url = 'https://fanyi.baidu.com/sug'
  headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'}
  response = requests.post(url,data=data,headers=headers)
  word=(response.json()['data'][0]['v'])
  print(word)
