import requests
import re
from bs4 import BeautifulSoup

url = "https://www.umei.cc/weimeitupian/wenzitupian/"

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0'
}
cookies = {
    "Cookie": '__51uvsct__K0KOUvCHIpTH8Vt6=1; __51vcke__K0KOUvCHIpTH8Vt6=42036666-4d00-5626-9e9f-0cc77fdf4f9c; __51vuft__K0KOUvCHIpTH8Vt6=1751426804442; gxgefecookieinforecord=%2C67-317374%2C61-338399%2C; __vtins__K0KOUvCHIpTH8Vt6=%7B%22sid%22%3A%20%221c078243-23e6-576d-8af7-4c2b6b50af74%22%2C%20%22vd%22%3A%2011%2C%20%22stt%22%3A%2055682%2C%20%22dr%22%3A%209783%2C%20%22expires%22%3A%201751428660121%2C%20%22ct%22%3A%201751426860121%7D'
}

reps = requests.get(url, headers=headers, cookies=cookies)
reps.encoding = "utf-8"
page = BeautifulSoup(reps.text, "html.parser")
ul = page.find("div", class_ = "item_list infinite_scroll", id = "infinite_scroll").find_all("img", class_ = "lazy")
ul1 = [item.get("data-original") for item in ul]

reps.close()
print(ul1)

# obj = re.compile(r'<div class="item masonry_brick">.*?<img class="lazy" data-original="(?P<ul>.*?)" width.*?alt="(?P<name>.*?)"', re.S)
#
#
# a = 2
# for i in range(1, 3):
#     reps = requests.get(url, headers=headers, cookies=cookies)
#     reps.encoding = "utf-8"
#     result = obj.finditer(reps.text)
#     url = f"https://www.umei.cc/weimeitupian/wenzitupian/index_{a}.htm"
#     a += 1
#     for item in result:
#         print(item.group("name"), item.group("ul"))
#     reps.close()