from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from driver import setdriver
from sql import setdb, setcurser, getquery, getupdatequery

driver = setdriver()
db = setdb()
cursor = setcurser(db)

sql_rows = []


# 년도와 라운드를 저장하는 함수
def setinfo(url, lastindex):
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

        if rndEdDt == '':
            xpath = '//*[@id="type1"]/div/table/tbody/tr[' + str(lastindex-1) + ']/td[1]'
            rndEdDt = driver.find_element(By.XPATH, xpath).text.replace(' ', '')[:-3]

        sql_row = '({},{},{},{})'.format(leagYr, rnd, rndSrtDt, rndEdDt)
        sql_rows.append(sql_row)
        insertQuery = getquery('TB_LEAGUE', sql_rows)
        print('리그정보 ' + insertQuery)
        # cursor.execute(insertQuery)
        # db.commit()

        updateQuery = getupdatequery('TB_GAME', 'RND = '+rnd, 'RND is null')
        print(updateQuery)
        # cursor.execute(updateQuery)
        # db.commit()
        sql_rows.clear()
    except NoSuchElementException:
        print('element 없음')
        return True



