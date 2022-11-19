import requests
from lxml import etree
import os
from time import sleep

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}

hero_list_url = 'https://pvp.qq.com/web201605/js/herolist.json'
hero_list_resp = requests.get(hero_list_url, headers=headers)


for h in hero_list_resp.json():
    ename = h.get('ename')
    cname = h.get('cname')
    skin_name = h.get('skin_name')
    print("skin name: ", skin_name)
    if "|" in skin_name and skin_name is not None:
        skin_name = h.get('skin_name').split("|")
        print(skin_name)
    # else:
    #     skin_name = h.get('skin_name').split("|")
    #     print(skin_name)
    # for i, name in enumerate(skin_name):
    #     print(i, name)
    if not os.path.exists(cname):
        os.mkdir(cname)
        for i, name in enumerate(skin_name):
            resp = requests.get(
                f'https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/523/523-bigskin-{i + 1}.jpg',
                headers=headers)
            with open(f'{cname}/{name}.jpg', 'wb') as f:
                f.write(resp.content)
            print(f'{name} download')
            sleep(1)




