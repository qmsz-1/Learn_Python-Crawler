import requests


url = "https://www.pearvideo.com/video_1801121"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0",
    "referer": url
}


contId = url.split("_")[-1]
Videocont = f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.8468972852302451"


resp1 = requests.get(Videocont, headers=headers)
dic = resp1.json()
srcurl = dic["videoInfo"]["videos"]["srcUrl"]
systemTime = dic["systemTime"]
srcurl = srcurl.replace(systemTime, f"cont-{contId}")
resp2 = requests.get(srcurl, headers=headers)
# print(srcurl)
# print(resp2.status_code)

with open("video.mp4", "wb") as f:
    f.write(requests.get(srcurl).content)
resp1.close()
resp2.close()