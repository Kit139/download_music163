import requests
import re
import os
import time

filename = "音乐\\"
if not os.path.exists(filename):
    os.mkdir(filename)

# 如果需要爬取其他榜单的歌曲,只需要更改id的值
url = "https://music.163.com/discover/toplist?id=3778678"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62"
}
resp = requests.get(url=url,headers=headers)

data_list = re.findall('<li><a href="/song\?id=(\d+)">(.*?)</a>',resp.text)

for id,name in data_list:
    # 引用一个接口
    music_url = f'http://music.163.com/song/media/outer/url?id={id}.mp3'
    # 对于音乐播放地址发送请求,获取二进制数据内容
    music_content = requests.get(url=music_url,headers=headers).content
    with open(filename + name + '.mp3',"wb") as f:
        f.write(music_content)
    # 延时0.5s
    time.sleep(0.5)
    print(id,name)
print("程序结束")
