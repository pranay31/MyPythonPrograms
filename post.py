import requests
"""url = 'http://httpbin.org/post'
files = {'file': open('apis/report.xls', 'rb')}

r = requests.post(url, files=files)
print r.text"""


r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=London&APPID={APIKEY}')
print(r.json())