from selenium.webdriver.common.by import By
from driver import setdriver
from sql import setdb, setcurser, getquery

driver = setdriver()
db = setdb()
cursor = setcurser(db)


# 상세결과 페이지의 데이터를 저장하는 함수
def getgameeesult(webaddress):
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
    while count < 7:
        homeLink = '//*[@class="inner_table"]/tbody/tr[1]/td[' + str(count) + ']'
        awayLink = '//*[@class="inner_table"]/tbody/tr[2]/td[' + str(count) + ']'
        homeScore.append(driver.find_element(By.XPATH, homeLink).text)
        awayScore.append(driver.find_element(By.XPATH, awayLink).text)
        count += 1

    sql_rows = []
    sql_row = '({},{},{},{},{},{},{},{},{})'.format(homeTeam, gameDate, homeSet, homeScore[0], homeScore[1],
                                                    homeScore[2], homeScore[3], homeScore[4], homeResult)
    sql_rows.append(sql_row)
    sql_row = '({},{},{},{},{},{},{},{},{})'.format(awayTeam, gameDate, awaySet, awayScore[0], awayScore[1],
                                                    awayScore[2], awayScore[3], awayScore[4], awayResult)
    sql_rows.append(sql_row)
    insertQuery = getquery('TB_GAME_RESULT', sql_rows)
    print(insertQuery)
    driver.back()
    # cursor.execute(insertQuery)
    # db.commit()
