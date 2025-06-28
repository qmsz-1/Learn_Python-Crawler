from urllib.request import urlopen

url = "https://www.baidu.com"
reps = urlopen(url)


with(open("myXHS.html", mode ="w", encoding ="utf-8")) as f:
    f.write(reps.read().decode("utf-8"))
print("完成")
reps.close()