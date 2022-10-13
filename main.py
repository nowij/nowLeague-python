import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

# 시즌 리스트 변수, 링크 변수 선언
seasons = ['001', '002', '003', '004', '005', '006', '007', '008', '009', '010', '011', '012', '013', '014', '015', '016', '017']
round = ['1', '2', '3', '4', '5', '6'];
url = 'https://www.kovo.co.kr/game/v-league/11110_schedule_list.asp?season='

# 실행 시 브라우저 안 열리게 headless 설정
options = webdriver.ChromeOptions()
options.add_argument('--headless')

# 크롬 드라이버 경로 지정
driver = webdriver.Chrome('/Users/jiwon/python/crawling/chromedriver', options=options)
# driver = webdriver.Chrome('/Users/jiwon/python/crawling/chromedriver') # 페이지 이동 확인하고 싶을 때

def initMain(webAddress):
    driver.get(url + season)
    mainXpath = '//*[@id="type1"]/div/table/tbody/tr['
    resultXpath = '/td[10]/a'
    i = 1
    while True:
        main = mainXpath + str(i) + ']'
        try:
            gender = (driver.find_element(By.XPATH, main+'/td[3]')).text
            i += 1
            if gender == '여자':
                href = driver.find_element(By.XPATH, main+resultXpath).get_attribute('href')
                moveResultPage(href)
                time.sleep(3)
        except NoSuchElementException:
            print('element 없음')
            break

def moveResultPage(webAddress):
    driver.get(webAddress)
    temp = (driver.find_element(By.XPATH, '// *[ @ id = "wrp_content"] / article[1] / table / thead / tr / th')).text
    print('페이지 이동 확인 : '+temp)

        # NoAlertPresentException 경고창 관련 명령어를 실행했으나 현재 경고창이 뜨지 않음
        # NoSuchElementException 엘레먼트 접근하였으나 없음
        # TimeoutException 특정한 액션을 실행하였으나 시간이 오래 지나도록 소식이 없음
        # ElementNotInteractableException 엘리먼트에 클릭등을 하였으나 클릭할 성질의 엘리먼트가 아님
        # NoSuchWindowException 해당 윈도우 없음
        # NoSuchFrameException 해당 프레임 없음


for season in seasons:
    if season == '001':
        initMain(url+season)
    else:
        print(url+season) # 페이지 변경으로 소스 변경할 예정


