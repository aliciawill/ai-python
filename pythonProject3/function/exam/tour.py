def spring(month, location):
    # spring(3, '제주도')
    data = str(month) + '월에 ' + location + "에 가요!"
    print(data)


def summer(location, month, price=10000):
    if month == 7:
        price -= 1000
    elif month == 6:
        price -= 2000
    elif month == 8:
        pass
    else:
        price += 2000
    data = str(month) + '월에 ' + location + "를 가는 비용은 " + \
            str(price) + '원입니다.'

    return data

if __name__ == '__main__':
    spring(3, '제주도')

    result = summer('울릉도', 8)
    print(result)

    result2 = summer('울릉도', 6)
    print(result2)
