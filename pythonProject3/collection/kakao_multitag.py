import sys
import requests

API_URL = 'https://dapi.kakao.com/v2/vision/multitag/generate'
MYAPP_KEY = 'b9ca7e6fcb8da3719636ca6542de8a8a'

def generate_tag(image_url):
    headers = {'Authorization': 'KakaoAK {}'.format(MYAPP_KEY)}

    try:
        data = { 'image_url' : image_url}
        resp = requests.post(API_URL, headers=headers, data=data)
        #resp.raise_for_status()
        result = resp.json()['result']
        print(result)
        print(type(result))
        if len(result['label_kr']) > 0:
            # if type(result['label_kr'][0]) != str:
            #     result['label_kr'] = map(lambda x: str(x.encode("utf-8")), result['label_kr'])
            #     print(result['label_kr'])
            print("이미지를 대표하는 태그는 \"{}\"입니다.".format(','.join(result['label_kr'])))
        else:
            print("이미지로부터 태그를 생성하지 못했습니다.")

    except Exception as e:
        print(str(e))
        sys.exit(0)

if __name__ == "__main__":
    img_url = 'http://t1.daumcdn.net/alvolo/_vision/openapi/r2/images/08.jpg'
    generate_tag(img_url)