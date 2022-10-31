from selenium import webdriver
import pymysql as sql

def driverSetting():
    # 실행 시 브라우저 안 열리게 headless 설정
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    # 크롬 드라이버 경로 지정
    driver = webdriver.Chrome('/Users/jiwon/python/crawling/chromedriver', options=options)
    # driver = webdriver.Chrome('/Users/jiwon/python/crawling/chromedriver') # 페이지 이동 확인하고 싶을 때
    return driver

def dbSetting():
    #db 연결
    db = sql.connect(
        user='nl',
        passwd='nowleague',
        host='138.2.121.169',
        db='NL',
        charset='utf8'
    )

    return db

def curserSetting(db):
    cursor = db.cursor(sql.cursors.DictCursor)
    return cursor
