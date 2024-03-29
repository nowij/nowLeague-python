import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from gameResult import setgameresult
from driver import setdriver
from leagueInfo import setinfo

# 시즌 리스트 변수, 링크 변수 선언
seasons = ['001', '002', '003', '004', '005', '006', '007', '008', '009', '010', '011', '012', '013', '014', '015', '016', '017', '018']
rounds = ['1', '2', '3', '4', '5', '6']
url = 'https://www.kovo.co.kr/game/v-league/11110_schedule_list.asp?season='
driver = setdriver()


def initmain(url,season):
    webaddress = url + season
    for round in rounds:
        mainXpath = webaddress + '&team=&yymm=&r_round=' + round
        driver.get(mainXpath)
        mainXpath2 = '//*[@id="type1"]/div/table/tbody/tr['
        resultXpath = '/td[10]/a[contains(text(), "상세결과")]'
        i = 1
        while True:
            main = mainXpath2 + str(i) + ']'
            try:
                gender = (driver.find_element(By.XPATH, main + '/td[3]')).text
                i += 1
                if gender == '여자':
                    href = driver.find_element(By.XPATH, main + resultXpath).get_attribute('href')
                    setgameresult(href)
            except NoSuchElementException:
                print('===== [' + season + '] ' + round + 'Round Complete... And LeageInfo Start(' + str(i) + ') =====')
                if i > 1:
                    if setinfo(mainXpath, i-1, season, round):
                        time.sleep(2)
                        break
                    break
                print(">>>>> [" + season + "] " + round + "Round End...  Next Season/Round >>>>>")
                break

        # NoAlertPresentException 경고창 관련 명령어를 실행했으나 현재 경고창이 뜨지 않음
        # NoSuchElementException 엘레먼트 접근하였으나 없음
        # TimeoutException 특정한 액션을 실행하였으나 시간이 오래 지나도록 소식이 없음
        # ElementNotInteractableException 엘리먼트에 클릭등을 하였으나 클릭할 성질의 엘리먼트가 아님
        # NoSuchWindowException 해당 윈도우 없음
        # NoSuchFrameException 해당 프레임 없음


for season in seasons:
    initmain(url,season)