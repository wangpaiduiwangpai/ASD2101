import requests

url = "https://mvwebfs.hw.kugou.com/202407261755/af0c8a8ea69360a6030f3c85316c679d/KGTX/CLTX002/0b3350d8a718666060d33e25ade49a55.mp4"
res = requests.get(url)
open("云悠悠大长腿.mp4", "wb").write(res.content)
