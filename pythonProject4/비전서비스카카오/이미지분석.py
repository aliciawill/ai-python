import sys
import argparse
import requests #알트+엔터
from collections import Counter

API_URL = 'https://dapi.kakao.com/v2/vision/multitag/generate'
MYAPP_KEY = 'd6f791df86f8170b57cb81395f7a424b'

def generate_tag(image_url):
    headers = {'Authorization': 'KakaoAK {}'.format(MYAPP_KEY)}

    try:
        data = {'image_url' : image_url}
        resp = requests.post(API_URL, headers=headers, data=data)
        print(resp)
        resp.raise_for_status()
        print("비전 kakao 서버와 연결 ok..")
        print(resp.content)
        return resp.json()
    except Exception as e:
        print(str(e))
        sys.exit(0)
label_total_eng = []
label_total_kr = []

def arg_add(site):
    parser.add_argument('image_url', type=str, nargs='?',
                        default=site,
                        help='image file to hide faces')

    args = parser.parse_args()

    result_json = generate_tag(args.image_url)
    print(result_json)
    result = result_json['result']
    label_eng = result['label']
    label_kr = result['label_kr']
    print(label_eng)
    print(label_kr)

    label_total_eng.append(label_eng)
    label_total_kr.append(label_kr)

    print(label_total_eng)
    print(label_total_kr)

if __name__ == "__main__":
    sites = [
        'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjAyMTFfMTM3%2FMDAxNjQ0NTQxMzUzMzEy.ihz9DF1aDBi7OvqsxMWjTvwAfD5sgymT2d0kT9BKFzUg.U70Z8i2BTJeHBjz5n4wXNEadE8Z0hkrnDLny718ybyYg.JPEG.ameliepink%2FIMG_9694.jpg&type=a340',
        'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTEyMTNfNjMg%2FMDAxNjM5MzY2MDUyMzQ1.8AXJ-ehrN81cOkH9AfIaJptmWlPVyOGw4udzD7zjSugg.chpkXDwEeoZ6_MWpoqLmdS6z-IY5_gbMOx6wT7EeAlYg.JPEG.tkfkdwlqhouse%2F1639366013093.jpg&type=a340'
        ]
    parser = argparse.ArgumentParser(description='.')
    for site in sites:
        print(site)
        arg_add(site)

    #2차원 리스트를 1차원 리스트로 변환.
    result_eng = []
    result_kr = []
    for li in label_total_eng:
        for l in li:
            result_eng.append(l)

    for li in label_total_kr:
        for l in li:
            result_kr.append(l)

    print(result_eng)
    print(result_kr)

    #최빈도 찾기
    eng_count = Counter(result_eng)
    kr_count = Counter(result_kr)

    print('--eng--', eng_count)
    print('--kr--', kr_count)


   #최빈도를 가지는 값 추출

    print('--counter--', kr_count.most_common(1))
    mode = kr_count.most_common(1)
    print(mode[0][0])