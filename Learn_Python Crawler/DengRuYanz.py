import requests


session = requests.Session()


url = "https://passport.17k.com/ck/user/login"
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0'
}
cookies = {
    "Cookie": 'GUID=d8c50cdf-fba2-42be-b787-8fd6978ae12d; sajssdk_2015_cross_new_user=1; BAIDU_SSP_lcr=https://cn.bing.com/; Hm_lvt_9793f42b498361373512340937deb2a0=1751438052; HMACCOUNT=CA7E2F9E4F595636; acw_tc=1a0acafa17514380580045666e909ceb7e100afd0b0bd70288f8b00e933780; c_channel=0; c_csc=web; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22d8c50cdf-fba2-42be-b787-8fd6978ae12d%22%2C%22%24device_id%22%3A%22197c9d7c9d8197-057a141cd5b905-4c657b58-2073600-197c9d7c9d9a69%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22d8c50cdf-fba2-42be-b787-8fd6978ae12d%22%7D; Hm_lpvt_9793f42b498361373512340937deb2a0=1751439402; tfstk=gKunQf1tEDrClH9TXVaB0w4x9ZKTRya7fYQ8ezeybRy_eBwLpbkoZjrzTwkKj8DZIJz8J2LoqRzUVDe8p84oNxA9HELxOXa7uKpvkpDRb9UbaWzPePragzVEjUI2JXa7zdBGC87SOvMVhBkUzC4aZ7Qzz8kz71y_N7WUawRMsRNR49yzzNPaGS_zzzkzQOy_azPEUkRi_jYlz-0r5VJO4wrlmz9E7Wq33XyE9cgZytexTmQRyJV3x6hUIa7rS0cGM3eec1e7JJGgtYTfRyro42UZ8d8zumMirozD2BZEZcD7JVRPY-oKpPuEm_7rsy2g25r1Kd2qRfub7lL2ifuspXgiw_8z6xeZO2zkuIa38Jzg14p188mZ42EQP9JuFVcZ80jzmGS4sf_7_Q3GVgZU152Ab2e2Nez8qodMsitQY5NpHCAGVgZU152vsCjfdkP_9KC..'
}
data = {
    "loginName": "13343518974",
    "password": "ming@@di1326."
}

reps = session.post(url, data = data, headers=headers, cookies=cookies)
# print(reps.text)
resp = session.get("https://user.17k.com/ck/author2/shelf?page=1&appKey=2406394919")
# print(resp.json())
result = resp.json()
result1 = result["data"]
for it in range(len(result1)):
    result2 = result1[it]
    print(result2["bookName"], result2["authorPenName"], result2["coverImg"])


resp.close()
reps.close()


