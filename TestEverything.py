import requests

url = 'http://www.renren.com/PLogin.do'
data = {
    'email':'13287857692',
    'password':'dongao123'
}
headers = {'user-agent':'Mozilla/5.0'}

session = requests.session()
session.post(url, data = data, headers = headers)

response = session.get('http://www.renren.com/974726184/profile')
with open('爬虫训练/人人网/renrne.html', 'w', encoding='utf-8') as f:
    f.write(response.text)