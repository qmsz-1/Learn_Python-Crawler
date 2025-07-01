import requests
from bs4 import BeautifulSoup

url = "http://www.xinfadi.com.cn/getCat.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"
}
a = 1186
b = 1186
prams = {
    "limit": "",
    "current": "",
    "pubDateStartTime": "",
    "pubDateEndTime": "",
    "prodPcatid": "",
    "prodCatid": "",
    "prodName": ""
}


prodname = []
for i in range(1):
    prams["prodCatid"] = a
    reps = requests.post(url, headers=headers, data=prams)
    # print(reps.text)
    page = BeautifulSoup(reps.text, "html.parser")
    result = page.find(name = 'list', attrs= {'prodName'})
    if result:
        for item in result.find_all(name='prodName'):
            prodname = item.find('prodName').text
            prodname.append(prodname)
    a += 1
    print(prodname)
    reps.close()



