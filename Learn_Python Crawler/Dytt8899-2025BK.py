import requests
import re

url = "http://www.dytt8899.com/"
headers = {
    "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0'
}
cookies = {
    "Cookie": 'UM_distinctid=197c03223d23df-08f3862dacdcc2-4c657b58-1fa400-197c03223d367d; CNZZDATA1281410151=1620753063-1751276201-%7C1751276240'
}

resp = requests.get(url, headers=headers, cookies=cookies)
resp.encoding = 'gb2312'

obj1 = re.compile(r'2025必看热片.*?<ul>(?P<ul>.*?)<ul>', re.S)
obj2 = re.compile(r"<a href='(?P<href>.*?)'", re.S)
obj3 = re.compile(r'<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<xzdz>.*?)">magnet')
result1 = obj1.finditer(resp.text)
for it in result1:
    ul = it.group("ul")
    result2 = obj2.finditer(ul)
    # print(ul)
    resp.close()
    for item in result2:
        href = item.group("href").strip("/")
        url_ture = url + href
        # print(url_ture)
        resp_ture = requests.get(url_ture, headers = headers, cookies = cookies)
        resp_ture.encoding = 'gb2312'
        result3 = obj3.finditer(resp_ture.text)
        for item3 in result3:
            xzdz = item3.group("xzdz")
            print(xzdz)
        resp_ture.close()
resp.close()