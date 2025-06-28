import requests
import re

url = "https://movie.douban.com/top250"
headers = {
    "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0'
}
cookies = {
    "Cookie": 'll="118281"; bid=N2qZJdjxeQ8; __utmc=30149280; __utmz=30149280.1751079672.1.1.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmc=223695111; __utmz=223695111.1751079708.1.1.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_id.100001.4cf6=838c13919e737eb2.1751079708.; __yadk_uid=k3xX3EqRbKn56zbQJjiNkHMsVITPKTqZ; 6333762c95037d16=l2C0or0JqZVKcvh5yOdCvMM%2BBbuLgqrM7sgqzjIZrQGJqPcsr4sb9gmCNpOegBTQW%2FRmqseYt6Rxb34HWm0rl6Al2upLAJgPBQx%2Fvuc5F6DFSEt8KRPNmI5y5CDHH43CAInCiCR1edS3AO96vBIotHfidGIKO5DXCR9v6v9PywFZXNj0hXCeTiw9gwIM2eAGbnc6VlbKllEWBQIzWl549O71FwjQHOvtacKv9yxMlUq4IL%2Fd9LvSm9SwtzHb6%2BQBi5R3w%2FAULlfUU%2BD3kvWhTgHrjXO1f9%2B2RKmTj5XEbkFQ%2FW20fQsd7w%3D%3D; _vwo_uuid_v2=DFC27A13BB280438FD0C965BCFABFCA8E|f4677d25760ab05da8b00e7bda886c97; ap_v=0,6.0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1751098697%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D; _pk_ses.100001.4cf6=1; __utma=30149280.1202855705.1751079672.1751094730.1751098697.4; __utma=223695111.204974105.1751079708.1751094730.1751098697.4; __utmb=223695111.0.10.1751098697; __utmt=1; _TDID_CK=1751100495214; __utmb=30149280.4.9.1751100504648'
}

resp = requests.get(url, headers=headers, cookies=cookies)
content = resp.text

obj = re.compile(r'<span class="title">(?P<title1>.*?)</span>.*?(?:<span class="title">&nbsp;/&nbsp;(?P<title2>.*?)</span>)?.*?<span class="other">&nbsp;/&nbsp;(?P<title3>.*?)</span>.*?导演: (?P<director>.*?)&nbsp;&nbsp;&nbsp;主演: (?P<actor>.*?)\s*/.*?<br>(?P<year>\d{4})\s*/\s*(?P<country>.*?)\s*/\s*(?P<type>.*?)\s*</p>', re.S)
result = obj.finditer(content)
for item in result:
    print(item.group())

resp.close()