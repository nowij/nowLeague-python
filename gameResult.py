import time

from selenium.webdriver.common.by import By
from driver import setdriver
from sql import setdb, setcurser

driver = setdriver()
db = setdb()
cursor = setcurser(db)
isComplete = False

# 상세결과 페이지의 데이터를 저장하는 함수
def setgameresult(webaddress):
    driver.get(webaddress)
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
    homeWinPoint = 0
    awayWinPoint = 0
    while count < 7:
        homeLink = '//*[@class="inner_table"]/tbody/tr[1]/td[' + str(count) + ']'
        awayLink = '//*[@class="inner_table"]/tbody/tr[2]/td[' + str(count) + ']'
        homeScore.append(driver.find_element(By.XPATH, homeLink).text)
        awayScore.append(driver.find_element(By.XPATH, awayLink).text)
        count += 1

    # 승점 3점일 경우
    if int(homeSet) >= 3:
        if int(awaySet) <= 1:
            homeWinPoint = 3
        else:
            homeWinPoint = 2
            awayWinPoint = 1

    # 승점 2점, 1점인 경우
    elif int(awaySet) >= 3:
        if int(homeSet) <= 1:
            awayWinPoint = 3
        else:
            homeWinPoint = 1
            awayWinPoint = 2

    datas = []
    data = (homeTeam, gameDate, homeSet,homeScore[0], homeScore[1],
                homeScore[2], homeScore[3],homeScore[4], homeResult, homeWinPoint)
    datas.append(data)
    data = (awayTeam, gameDate, awaySet,awayScore[0], awayScore[1],
                awayScore[2], awayScore[3],awayScore[4], awayResult, awayWinPoint)
    datas.append(data)
    insertQuery = "INSERT INTO NL.TB_GAME_RESULT VALUES(%s,STR_TO_DATE(%s, '%%Y-%%m-%%d'),%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.executemany(insertQuery, datas)
    db.commit()
    datas.clear()

    year = driver.find_element(By.XPATH, '//*[@id="pageheader"]/form/fieldset/div/a/span[1]').text
    data = (year, gameDate, '', homeTeam, awayTeam)
    datas.append(data)
    insertQuery = "INSERT INTO NL.TB_GAME VALUES(%s,STR_TO_DATE(%s, '%%Y-%%m-%%d'),%s,%s,%s)"
    cursor.executemany(insertQuery, datas)
    db.commit()
    datas.clear()
    time.sleep(1)

    driver.back()





