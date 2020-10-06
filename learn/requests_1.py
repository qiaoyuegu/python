import requests

target = 'http://www.jingxinfz.compattern/page/pattern.html'
req = requests.get(url=target)
print(req.text)
