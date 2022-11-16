from selenium.webdriver.common.by import By

import sql
from driver import setdriver
from sql import setdb, setcurser, getquery

driver = setdriver()
db = setdb()
cursor = setcurser(db)
year = driver.find_element(By.XPATH, '//*[@id="pageheader"]/form/fieldset/div/a/span[1]').text

def setGameInfo(date,home,away):
    sql_rows = []
    sql_row = '({},{},{},{},{})'.format(year, date, '', home, away)
    sql_rows.append(sql_row)
    insertQuery = getquery('TB_GAME', sql_rows)
    print('게임정보 ' + insertQuery)
    # cursor.execute(insertQuery)
    # db.commit()
    return True


def setGameInfo(table, column):
    pk = sql.getselectquery(table, column)
