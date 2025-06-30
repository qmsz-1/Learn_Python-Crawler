import requests



url1 = "https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=20"
header1 = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0"
}
cookie1 = {
    "Cookie": 'll="118281"; bid=cfuQOmIdgG8; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1751009968%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D; _pk_id.100001.4cf6=24117e039a74a845.1751009968.; _pk_ses.100001.4cf6=1; ap_v=0,6.0; __utma=30149280.983894470.1751009968.1751009968.1751009968.1; __utmb=30149280.0.10.1751009968; __utmc=30149280; __utmz=30149280.1751009968.1.1.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=223695111.913925212.1751009968.1751009968.1751009968.1; __utmb=223695111.0.10.1751009968; __utmc=223695111; __utmz=223695111.1751009968.1.1.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __yadk_uid=u9MZP32r8YROoXh9DWakgMFsyUXW9nbQ; _vwo_uuid_v2=DD7DACA0E0E521044AF8603B71552A1CD|a5630eb51a1c1d2ec70036f4e6bec276; _TDID_CK=1751009970991; 6333762c95037d16=oQj8rx3xc25Zm4c3Iu1ScK1J8hA9CD1zHCRCUIZnIItC1Ym9HtO9OrOqm%2Bhu6%2F8R1V6AuRdlgol2hCe%2Fvl8kJtuapwSmj6oxz5BtpqofLMkfmf8%2FRENTogiqJ2ktyjOjhmfjie8WpHnTbl62XHE6NoHukiSI89v7%2BvivoOX6ddxujWbQ3aHCJeg1trO4k%2BxYFQPaXGoiX4JykTcDOgOcQQ8avZUvFttsiNnDR4pg8cawMvZOVhJbG8Hf1yuFNpNK%2BFCs%2Be3yrnQVIz6Kklg3RSW2U9nP%2BMwJgz4gGPZIXksCohlSJM4CfA%3D%3D'
}
resp = requests.get(url1, headers = header1, cookies = cookie1)

a = 0
for i in range(20):
    a += 20
    param1 = {
    "type": "24",
    "interval_id": "100:90",
    "action": "",
    "start": a,
    "limit": 20
}
    url1 = "https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start={}&limit=20".format(a)
    resp = requests.get(url1, headers = header1, cookies = cookie1, params = param1)
    print(resp.json())

print(a)
resp.close()
