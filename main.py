# 크롬드라이버 위치 : /Users/jiwon/python/crawling/chromedriver
from selenium import webdriver
from selenium.webdriver.common.by import By

# 시즌 리스트 변수, 링크 변수 선언
seasons = ['001', '002', '003', '004', '005', '006', '007', '008', '009', '010', '011', '012', '013', '014', '015', '016', '017']
round = ['1', '2', '3', '4', '5', '6'];
url = 'https://www.kovo.co.kr/game/v-league/11110_schedule_list.asp?season='

# 크롬 드라이버 경로 지정
driver = webdriver.Chrome('/Users/jiwon/python/crawling/chromedriver')

def init(webAddress):
    driver.get(url + season)
    xpath = driver.find_element(By.XPATH, '//*[@id="type1"]/div/table/tbody/tr[2]/td[3]')
    print(xpath.text)

for season in seasons:
    if season == '001':
        init(url+season)
    else:
        print(url+season) # 페이지 변경으로 소스 변경할 예정


