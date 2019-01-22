# import os
# import request
# filesInDirectory =  os.listdir("pieces")    # directory data
# for i in filesInDirectory:                  
#     print("Piece : - ", i)





# import requests
# response = requests.get('http://abhinavkumar.ml')
# print (response.headers)





import requests
from bs4 import BeautifulSoup

url = 'http://192.168.0.3:8888'

payload = "{}"
headers = {
        "Host": "192.168.0.3:8888",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Referer": "192.168.0.3:8888",
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": "17",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Cache-Control": "no-cache",
        "Pragma": "no-cache",
    }
response = requests.post(url, headers=headers, data=payload)