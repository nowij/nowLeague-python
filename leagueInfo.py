import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from driver import setdriver
from sql import setdb, setcurser

driver = setdriver()
db = setdb()
cursor = setcurser(db)

datas = []


# 년도와 라운드를 저장하는 함수
def setinfo(url, lastindex, season, round):
    driver.get(url)
    xpath = '//*[@id="pageheader"]/form/fieldset/div/a/span[1]'
    leagYr = driver.find_element(By.XPATH, xpath).text

    xpath = '//*[@class="wrp_date"]/form/fieldset/a[2]/span[1]'
    rnd = driver.find_element(By.XPATH, xpath).text

    try:
        xpath = '//*[@id="type1"]/div/table/tbody/tr[1]/td[1]'
        rndSrtDt = driver.find_element(By.XPATH, xpath).text.replace(' ', '')[:-3]

        xpath = '//*[@id="type1"]/div/table/tbody/tr[' + str(lastindex) + ']/td[1]'
        rndEdDt = driver.find_element(By.XPATH, xpath).text.replace(' ', '')[:-3]

        while rndEdDt == '':
            lastindex -= 1
            xpath = '//*[@id="type1"]/div/table/tbody/tr[' + str(lastindex) + ']/td[1]'
            rndEdDt = driver.find_element(By.XPATH, xpath).text.replace(' ', '')[:-3]

        year = leagYr.split(sep=' ')[1]

        if (season == '001'):
            rndSrtDt = year + '-' + rndSrtDt.replace('.', '-')
            rndEdDt = year + '-' + rndEdDt.replace('.', '-')
        else:
            firstYear = year.split(sep='-')[0]
            secondYear = year.split(sep='-')[1]
            months = []
            months.append(int(rndSrtDt.split(sep='.')[0]))
            months.append(int(rndEdDt.split(sep='.')[0]))

            # 각 라운드 시작 날짜와 종료 날짜 계산
            for i in range(2):
                if (i == 1):
                    if (int(round) == 1):
                        rndSrtDt = firstYear + '-' + rndSrtDt.replace('.', '-')
                    elif (int(round) > 1 and 9 < months[i] < 13):
                        rndSrtDt = firstYear + '-' + rndSrtDt.replace('.', '-')
                    else:
                        rndSrtDt = secondYear + '-' + rndSrtDt.replace('.', '-')
                else:
                    if (months[i-1] == months[i] and int(round) < 3):
                        rndEdDt = firstYear + '-' + rndEdDt.replace('.', '-')
                    elif (int(round) > 1 and 9 < months[i] < 13):
                        rndSrtDt = firstYear + '-' + rndSrtDt.replace('.', '-')
                    else:
                        rndEdDt = secondYear + '-' + rndEdDt.replace('.', '-')

        data = (leagYr, rnd, rndSrtDt, rndEdDt)
        datas.append(data)
        insertQuery = "INSERT INTO NL.TB_LEAGUE VALUES(%s,%s,STR_TO_DATE(%s, '%%Y-%%m-%%d'),STR_TO_DATE(%s, '%%Y-%%m-%%d'))"
        cursor.executemany(insertQuery, datas)
        db.commit()
        datas.clear()
        time.sleep(1)

        updateQuery = "UPDATE NL.TB_GAME SET RND = %s WHERE RND = ''"
        cursor.execute(updateQuery, rnd)
        db.commit()
    except NoSuchElementException:
        print('===== LeagueInfo And GameInfo Complete... =====')
        return True
