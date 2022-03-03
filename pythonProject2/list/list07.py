# movie 예매 사이트
seat = [0] * 10
while True:
    print('\n영화예매 사이트입니다.')
    print('-----------------------------')
    print(' ', end='')
    for x in range(0, 10):
        print(x, end='  ')
    print()
    print('-----------------------------')
    print(seat)
    print('-----------------------------')
    no = int(input('예매 좌석번호 선택(종료 -1)>> '))
    if no == -1:
        break
        #몇 좌석 예매가 되었는지 프린트
        #결제금액 한 자라당 1만원해서 프린트
        #좌석 번호 프린트
    else:
        #예매처리
        seat[no] = 1
        #예매가 이미 된 자리라면 재입력하라고 해주세요.!


