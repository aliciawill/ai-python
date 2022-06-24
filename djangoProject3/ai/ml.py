import pymysql
db = pymysql.connect(
                    host='database-1.cgind9azzzrj.ap-northeast-2.rds.amazonaws.com',
                    port=3306,
                    user='root',
                    passwd='himedia00-=',
                    db='shop',
                    charset='utf8'
                    )

# Cursor Object 가져오기
cursor = db.cursor()
print('커서연결됨. ', cursor)
sql = "insert into test_member values (null, 'haha', 'haha', 'haha')"

cursor.execute(sql)
db.commit()
print('전송함')
db.close()