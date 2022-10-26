import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import pymysql as sql

# 시즌 리스트 변수, 링크 변수 선언
seasons = ['001', '002', '003', '004', '005', '006', '007', '008', '009', '010', '011', '012', '013', '014', '015', '016', '017']
rounds = ['1', '2', '3', '4', '5', '6']
url = 'https://www.kovo.co.kr/game/v-league/11110_schedule_list.asp?season='

# 실행 시 브라우저 안 열리게 headless 설정
options = webdriver.ChromeOptions()
options.add_argument('--headless')

# 크롬 드라이버 경로 지정
driver = webdriver.Chrome('/Users/jiwon/python/crawling/chromedriver', options=options)
# driver = webdriver.Chrome('/Users/jiwon/python/crawling/chromedriver') # 페이지 이동 확인하고 싶을 때

#db 연결
db = sql.connect(
    user='nl',
    passwd='nowleague',
    host='138.2.121.169',
    db='NL',
    charset='utf8'
)

cursor = db.cursor(sql.cursors.DictCursor)

def initMain(webAddress):
    for round in rounds:
        driver.get(webAddress + '&team=&yymm=&r_round=' + round)
        mainXpath = '//*[@id="type1"]/div/table/tbody/tr['
        resultXpath = '/td[10]/a'
        i = 1
        while True:
            main = mainXpath + str(i) + ']'
            try:
                gender = (driver.find_element(By.XPATH, main + '/td[3]')).text
                i += 1
                if gender == '여자':
                    href = driver.find_element(By.XPATH, main + resultXpath).get_attribute('href')
                    moveResultPage(href)
                    time.sleep(1)
            except NoSuchElementException:
                print('element 없음')
                break

def moveResultPage(webAddress):
    driver.get(webAddress)
    gameDate = driver.find_element(By.XPATH, '//*[@id="wrp_content"]/article[1]/table/thead/tr/th').text.split(sep='/')
    gameDate = gameDate[0][0:-4].replace('  ', '').replace('년', '-').replace('월', '-').replace('일', '')
    homeResult = driver.find_element(By.XPATH, '//*[@class="first team"]/p[1]').text
    homeTeam = driver.find_element(By.XPATH, '//*[@class="first team"]/p[2]/span[2]').text
    homeSet = driver.find_element(By.XPATH, '//*[@class="lst_recentgame lst_result mt10"]/tbody/tr/td[2]/p[2]').text
    awayResult = driver.find_element(By.XPATH, '//*[@class="team"]/p[1]').text
    awayTeam = driver.find_element(By.XPATH, '//*[@class="team"]/p[2]/span[2]').text
    awaySet = driver.find_element(By.XPATH, '//*[@class="lst_recentgame lst_result mt10"]/tbody/tr/td[4]/p[2]').text
    homeScore = []
    awayScore = []
    count = 2
    while count < 7:
        homeLink = '//*[@class="inner_table"]/tbody/tr[1]/td[' + str(count) + ']'
        awayLink = '//*[@class="inner_table"]/tbody/tr[2]/td[' + str(count) + ']'
        homeScore.append(driver.find_element(By.XPATH, homeLink).text)
        awayScore.append(driver.find_element(By.XPATH, awayLink).text)
        count += 1

    sql_rows = []
    sql_row = '({},{},{},{},{},{},{},{},{})'.format(homeTeam, gameDate, homeSet, homeScore[0], homeScore[1], homeScore[2], homeScore[3], homeScore[4], homeResult)
    sql_rows.append(sql_row)
    sql_row = '({},{},{},{},{},{},{},{},{})'.format(awayTeam, gameDate, awaySet, awayScore[0], awayScore[1],awayScore[2], awayScore[3], awayScore[4], awayResult)
    sql_rows.append(sql_row)
    insertQuery = 'INSERT INTO NL.TB_GAME_RESULT VALUES ' + ','.join(sql_rows)
    print(insertQuery)
    driver.back()
    #cursor.execute(insertQuery)
    #db.commit()

        # NoAlertPresentException 경고창 관련 명령어를 실행했으나 현재 경고창이 뜨지 않음
        # NoSuchElementException 엘레먼트 접근하였으나 없음
        # TimeoutException 특정한 액션을 실행하였으나 시간이 오래 지나도록 소식이 없음
        # ElementNotInteractableException 엘리먼트에 클릭등을 하였으나 클릭할 성질의 엘리먼트가 아님
        # NoSuchWindowException 해당 윈도우 없음
        # NoSuchFrameException 해당 프레임 없음


for season in seasons:
    # 한 페이지 테스트용으로 if문 설정 한 것 나중에 삭제
    if season == '001':
        initMain(url+season)
    else:
        print()