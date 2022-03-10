# 북마크 테이블에 대한 crud기능 처리를 하고 싶음.
# from db import dao
# from 패키지 import 모듈명
# --> 모듈명.함수(), 모듈명.클래스명()

import sys

from db.dao import *

# from 패키지명.모듈명 import 함수명, 클래스명, *
# --> 함수()

if __name__ == '__main__':
    choice = input('cud중 선택1)c, 2)u, 3)d>> ')
    # 모든 입력은 string! "1"
    if choice == '1':
        id = input('id입력>> ')
        name = input('name입력>> ')
        url = input('url입력>> ')
        img = input('img입력>> ')
        vo = (id, name, url, img)
        # create(id, name, url, img)
        create(vo)
    elif choice == '2':
        pass  # id가 1이면, name은 naver2로 변경
    elif choice == '3':
        pass  # id가 1이면 삭제
    else:
        sys.exit(0)  # 프로그램 종료!
