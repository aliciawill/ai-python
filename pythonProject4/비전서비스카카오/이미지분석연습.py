import sys
import argparse
import requests #알트+엔터(cmd+1)
from collections import Counter

#kakao연결 + 신청해놨던 키.
url = 'https://dapi.kakao.com/v2/vision/multitag/generate'
key = 'b9ca7e6fcb8da3719636ca6542de8a8a'

sites = ['https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjAyMTFfMTM3%2FMDAxNjQ0NTQxMzUzMzEy.ihz9DF1aDBi7OvqsxMWjTvwAfD5sgymT2d0kT9BKFzUg.U70Z8i2BTJeHBjz5n4wXNEadE8Z0hkrnDLny718ybyYg.JPEG.ameliepink%2FIMG_9694.jpg&type=a340',
         'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTEyMTNfNjMg%2FMDAxNjM5MzY2MDUyMzQ1.8AXJ-ehrN81cOkH9AfIaJptmWlPVyOGw4udzD7zjSugg.chpkXDwEeoZ6_MWpoqLmdS6z-IY5_gbMOx6wT7EeAlYg.JPEG.tkfkdwlqhouse%2F1639366013093.jpg&type=a340'
         ]

# site = 'http://blogfiles.naver.net/MjAxOTAzMjdfMjUz/MDAxNTUzNjY0NzE0NzQx.A2lS1g4f1FWiZ2u90J5qVXLiyZ5ChwO8Xm8JMfMNzl0g.sGG7AnxpvNFQmc9BBuybQtzl4L9KVITVLO6aDQxfT8wg.PNG.rac008282/%B3%AA_%C8%A5%C0%DA_%BB%EA%B4%D9.E286.190322.720p-NEXT.mp4_000127060.png'
for site in sites:
    parser = argparse.ArgumentParser(description='.')
    parser.add_argument('image_url', type=str, nargs='?',
                            default=site,
                            help='image file to hide faces')

    args = parser.parse_args()

    head = {'Authorization':'KakaoAK {}'.format(key)}
    data = {'image_url': args.image_url}

    result = requests.post(url, headers=head, data=data)
    # print(result)
    print(result.content)
    json = result.json()
    result_json = json['result']
    data = result_json['label']
    print(data)



