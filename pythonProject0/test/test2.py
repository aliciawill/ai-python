import requests
from bs4 import BeautifulSoup

img = 'main_pack > section.sc_new.sp_nimage._prs_img._imageSearchPC > div > div.photo_group._listGrid > div.photo_tile._grid > div:nth-child(2) > div > div.thumb > a > img'

response = requests.get('https://search.naver.com/search.naver?where=image&sm=tab_jum&query=자동차')

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    img_list = soup.select('img')
    print(len(img_list))
    for x in img_list:
        print(x)
    print(img_list[10]['src'])
    print(img_list[20]['src'])
    print(img_list[22]['src'])

else :
    print(response.status_code)