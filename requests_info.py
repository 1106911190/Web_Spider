import requests
url = 'http://www.baidu.com'
page = requests.get(url=url)
code = page.status_code
headers = page.headers
print code
print headers