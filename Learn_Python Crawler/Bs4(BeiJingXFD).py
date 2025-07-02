import requests
from bs4 import BeautifulSoup
import re

url = "http://www.xinfadi.com.cn/getCat.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"
}
a = 1
b = 1186
prams = {
    "limit": "",
    "current": a,
    "pubDateStartTime": "",
    "pubDateEndTime": "",
    "prodPcatid": "",
    "prodCatid": b,
    "prodName": ""
}

obj = re.compile(r'"id".*?"prodName":"(?P<name>.*?)",.*?"prodCat":"(?P<type>.*?)","prodPcatid".*?'
                 r'"avgPrice": "(?P<price>.*?)"', re.S)

for i in range(1, 5):
    # prams["current"] = a
    prams["prodCatid"] = b
    reps = requests.post(url, headers=headers, data=prams)
    result_json = reps.json()
    # result = obj.finditer(reps.text)
    for item in result_json.get('list', []):
        print(item.get('prodName'), item.get('prodCat'), item.get('avgPrice'))
    # for it in result:
    #     print(it.group("name"), it.group("type"))
    # a += 1
    b += 1
    # print(a)
    # print(prodname)
    reps.close()



