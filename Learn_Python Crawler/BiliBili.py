import requests
import re
import json
from pprint import pprint

def GetResponse(url):
    heders = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "referer": "https://www.bilibili.com/"

    }
    cookies = {
        "Cookie": "buvid3=94F6429F-D0DE-0B8A-1807-C7B9A8C35BF350936infoc; b_nut=1751612650; bsource=search_bing; _uuid=C7B21A14-11014-7FD3-10E86-83732217819F50469infoc; enable_web_push=DISABLE; buvid_fp=83c569b6879149d455f85b51e3d82202; buvid4=A70EAFD0-ACBF-20E4-6372-B33CE9A193C553431-025070415-0ErssgXsihQdphGXBh9%2FJGdkjanXQHNL7lGDTZKTuzrzSjxT3ms0krl6ptTDI2l%2F; bmg_af_switch=1; bmg_src_def_domain=i1.hdslb.com; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NTE4NzE4NTQsImlhdCI6MTc1MTYxMjU5NCwicGx0IjotMX0.t-uL1f_uktefU_XWiw4rZf-pQojUWaBVcJZiSXW_6gQ; bili_ticket_expires=1751871794; rpdid=0zbfVGpy9i|18X03IhaV|34|3w1UxAt3; b_lsid=98B35B11_197D49292C9; SESSDATA=0ca57d23%2C1767171608%2C79e20%2A72; bili_jct=56cef254b62e9c6d363a4f5cc91977a1; DedeUserID=324541991; DedeUserID__ckMd5=e7a083e2af4d7237; sid=4ldn8s29; CURRENT_FNVAL=2000; home_feed_column=4; browser_resolution=967-954; header_theme_version=CLOSE"
    }

    resp = requests.get(url = url, headers = heders, cookies = cookies)

    return resp
    resp.close()

def GetVideoInfo(link):
    resp = GetResponse(link)
    response = resp.text
    result = re.findall(r'<script>.*?window.__playinfo__=(.*?)</script>', response, re.S)[0]
    name = re.findall(r'"videoData".*?"title":"(?P<name>.*?)","pubdate"', response, re.S)[0]
    json_data = json.loads(result)
    # pprint(json_data)
    audio = json_data['data']['dash']['audio'][0]['baseUrl']
    video = json_data['data']['dash']['video'][0]['baseUrl']
    # print(name)
    # print("音频", "\n" ,audio)
    # print("视频", "\n" ,video)
    return name, audio, video
    resp.close()

def Save_audio(title, audio, video):
    audio_resp = GetResponse(url=audio).content
    with open("BiliBili\\" + title + ".mp3", "wb")as audio:
        audio.write(audio_resp)


def Save_video(title, audio, video):
    video_resp = GetResponse(url=video).content
    with open("BiliBili\\" + title + ".mp4", "wb")as video:
        video.write(video_resp)

if __name__ == "__main__":
    a = 0
    for a in range(1, 10):
        link = f"https://www.bilibili.com/video/BV1633MzTEtZ?vd_source=514b958d7dadbb77e6038c81656cb811&p={a}&spm_id_from=333.788.videopod.episodes"
        name, audio, video = GetVideoInfo(link)
        Save_audio(title = name, audio = audio, video = video)
        print(a)
    print("下载完成")