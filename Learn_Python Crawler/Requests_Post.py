import requests

url1 = "https://fanyi.baidu.com/sug"
header1 = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0"
}
cookie1 = {
    "Cookie": 'BAIDUID_BFESS=2F90FDFC3EFCB25E3CE8E4DA8BA53FB6:FG=1; BIDUPSID=2F90FDFC3EFCB25E3CE8E4DA8BA53FB6; PSTM=1750992932; BDRCVFR[BIVAaPonX6T]=-_EV5wtlMr0mh-8uz4WUvY; H_PS_PSSID=62325_63144_63326_63582_63579_63618_63638_63647_63654_63691_63725_63718_63752_63757_63775; BA_HECTOR=0l2l2gah0h8l2ga004a08484ak85861k5s1tl24; ZFY=MLAl671ufpnddh:BhQrtKUk2O5ooYo7YrplPA3ujrcHc:C; __bid_n=197b0311e2d6128a4d1e6b; ab_sr=1.0.1_ZTEwZGY1ZWViNjI0YTY4MWFjOTg3YjI1NWUxMWQ5MDEyNzY0Y2VmMDE3ODZlNTc4NmRkM2U4YTJlOGVjODM1YThiN2FkMzU1NTQwYjUzMDMzZDhhMzBhMjRiOTdkZGE5MDM0MzVlOTRlMGU0NDZmOGJmMjhiYTRhZTNhNTYyZGIwNWE0N2IwODA1NzA0Y2I2OWI1NzVmMzU3MGVkMmEyYmM4MWZmNjVlYjIwMWIxODdjMjYyOTcyOTI3ZTVlNTdkMzQ2Y2U5YTU5MTJlMzIwYTU5NThmMTI5MDU4NDBiNDU=; RT="z=1&dm=baidu.com&si=e92e3ebb-c19e-4072-865f-42fcf9554ca7&ss=mcegw9oc&sl=5&tt=9kl&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=ulk"'
}
s = input("输入你要翻译的单词:")
dat = {
    "kw": s
}

resp = requests.post(url1, data = dat, headers = header1, cookies = cookie1)
print(resp.json())
resp.close()