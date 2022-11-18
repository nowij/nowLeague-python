from selenium.webdriver.common.by import By

import sql
from driver import setdriver
from sql import setdb, setcurser, getquery

driver = setdriver()
db = setdb()
cursor = setcurser(db)


def setgameinfo(date, home, away):
    year = driver.find_element(By.XPATH, '//*[@id="pageheader"]/form/fieldset/div/a/span[1]').text
    print('확인 ' + year)
    sql_rows = []
    sql_row = '({},{},{},{},{})'.format(year, date, '', home, away)
    sql_rows.append(sql_row)
    insertQuery = getquery('TB_GAME', sql_rows)
    print('게임정보 ' + insertQuery)
    # cursor.execute(insertQuery)
    # db.commit()
    return True
