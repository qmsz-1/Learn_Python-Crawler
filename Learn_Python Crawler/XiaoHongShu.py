import requests

url1 = "https://www.xiaohongshu.com/explore"
header1 = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0"
}
cookie1 = {
    "Cookie": 'abRequestId=fd9a3d5d-cca8-5474-93cb-3792a7112e92; webBuild=4.68.0; a1=197aee95af9r25081qqlnz7koh8y7kkvaw4t1db1050000132796; webId=245f5dfb6e874b9ad54f7c2fcd2c4cfc; gid=yjW0ddDJDj0SyjW0ddj20EfDijFJ28YyAA1I4y8uWTlxY928vWTThy888yqJWjK8i4qi0S0J; xsecappid=xhs-pc-web; web_session=040069b64866f323ef78f7486b3a4b4d4f4eb6; acw_tc=0a00d90517510080149324959e6cbc4964d4684aa44e22248878b57f9461cd; loadts=1751008690838; unread={%22ub%22:%22685673bc000000001203ebde%22%2C%22ue%22:%2268440dd8000000002100157a%22%2C%22uc%22:25}; websectiga=634d3ad75ffb42a2ade2c5e1705a73c845837578aeb31ba0e442d75c648da36a; sec_poison_id=b632618c-52f6-4331-9905-3d0810b33856'
}

reps = requests.get(url1, headers = header1, cookies = cookie1)
print(reps.text)
reps.close()