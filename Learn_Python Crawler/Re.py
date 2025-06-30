import re
import requests

url = "https://movie.douban.com/j/chart/top_list?type=20&interval_id=100%3A90&action=&start=0&limit=20"
headers = {
    "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0'
}
cookies = {
    "cookie": 'll="118281"; bid=N2qZJdjxeQ8; __utmc=30149280; __utmz=30149280.1751079672.1.1.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmc=223695111; __utmz=223695111.1751079708.1.1.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_id.100001.4cf6=838c13919e737eb2.1751079708.; __yadk_uid=k3xX3EqRbKn56zbQJjiNkHMsVITPKTqZ; _TDID_CK=1751079710871; 6333762c95037d16=l2C0or0JqZVKcvh5yOdCvMM%2BBbuLgqrM7sgqzjIZrQGJqPcsr4sb9gmCNpOegBTQW%2FRmqseYt6Rxb34HWm0rl6Al2upLAJgPBQx%2Fvuc5F6DFSEt8KRPNmI5y5CDHH43CAInCiCR1edS3AO96vBIotHfidGIKO5DXCR9v6v9PywFZXNj0hXCeTiw9gwIM2eAGbnc6VlbKllEWBQIzWl549O71FwjQHOvtacKv9yxMlUq4IL%2Fd9LvSm9SwtzHb6%2BQBi5R3w%2FAULlfUU%2BD3kvWhTgHrjXO1f9%2B2RKmTj5XEbkFQ%2FW20fQsd7w%3D%3D; _vwo_uuid_v2=DFC27A13BB280438FD0C965BCFABFCA8E|f4677d25760ab05da8b00e7bda886c97; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1751089582%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D; _pk_ses.100001.4cf6=1; ap_v=0,6.0; __utma=30149280.1202855705.1751079672.1751079672.1751089582.2; __utmb=30149280.0.10.1751089582; __utma=223695111.204974105.1751079708.1751079708.1751089582.2; __utmb=223695111.0.10.1751089582'
}
resp = requests.get(url, headers=headers, cookies=cookies)

all_movies = []
obj = re.compile(r'"types":\s*\[(?P<type>.*?)\],\s*"regions":\s*\[(?P<regions>.*?)\],\s*"title":\s*"(?P<title>.*?)".*?"score":\s*"(?P<score>.*?)",\s*"actors":\s*\[(?P<actors>.*?)\]', re.S)
obj_type = re.compile(r'"types":\[(.*?)],')
obj_regions = re.compile(r'"regions":\[(.*?)\],')
obj_title = re.compile(r'"title":"(.*?)"')
obj_score = re.compile(r'"score":"(.*?)"')
obj_actors = re.compile(r'"actors":\[(.*?)\],')
for a in range(0, 200, 20):
    param = {
        "type": "20",
        "interval_id": "100:90",
        "action": "",
        "start": a,
        "limit": 20
    }
    url = "https://movie.douban.com/j/chart/top_list?type=20&interval_id=100%3A90&action=&start={}&limit=20".format(a)
    resp = requests.get(url, headers=headers, cookies=cookies, params=param)
    result = obj.finditer(resp.text)
    for item in result:
        print(item.group("title"), item.group("score"), item.group("type"), item.group("regions"), item.group("actors"))
    # text = resp.text
    # titles = obj_title.findall(text)
    # scores = obj_score.findall(text)
    # types = obj_type.findall(text)
    # regions = obj_regions.findall(text)
    # actors = obj_actors.findall(text)
    # for i in range(len(titles)):
    #     print(f"电影名: {titles[i]}, 评分: {scores[i]}, 类型: {types[i]}, 地区: {regions[i]}, 演员: {actors[i]}")
    # staging = resp.json()
    # all_movies.extend(staging)
    # with open("豆瓣-排行榜-恐怖.txt", "a", encoding="utf-8") as f:
    #     f.write(str(staging) + "\n")
    resp.close()

# with open("豆瓣-排行榜-恐怖-清洗后.txt", "w", encoding="utf-8") as f:
#     for movie in all_movies:
#         title = movie.get("title", "")
#         score = movie.get("score", "")
#         types = ",".join(movie.get("types", []))
#         actors = ",".join(movie.get("actors", []))
#         f.write(f"电影名: {title}, 评分: {score}, 类型: {types}, 演员: {actors}\n")

