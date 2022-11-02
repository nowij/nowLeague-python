from selenium import webdriver


def setdriver():
    # 실행 시 브라우저 안 열리게 headless 설정
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    # 크롬 드라이버 경로 지정
    driver = webdriver.Chrome('/Users/jiwon/python/crawling/chromedriver', options=options)
    # driver = webdriver.Chrome('/Users/jiwon/python/crawling/chromedriver') # 페이지 이동 확인하고 싶을 때
    return driver


