from selenium.webdriver.common.by import By
from driverAndSql import driverSetting, dbSetting, curserSetting

driver = driverSetting()
db = dbSetting()
cursor = curserSetting(db)

# 년도와 라운드를 저장하는 함수
def leagueAndRoundInfo(url, lastIndex):
    driver.get(url)
    xpath = '//*[@id="pageheader"]/form/fieldset/div/a/span[1]'
    leagYr = driver.find_element(By.XPATH, xpath).text

    xpath = '//*[@class="wrp_date"]/form/fieldset/a[2]/span[1]'
    rnd = driver.find_element(By.XPATH, xpath).text

    xpath = '//*[@id="type1"]/div/table/tbody/tr[1]/td[1]'
    rndSrtDt = driver.find_element(By.XPATH, xpath).text.replace(' ', '')[:-3]

    xpath = '//*[@id="type1"]/div/table/tbody/tr[' + str(lastIndex) + ']/td[1]'
    print(xpath)
    rndEdDt = driver.find_element(By.XPATH, xpath).text.replace(' ', '')[:-3]
    print(rndEdDt)
    if rndEdDt == '':
        xpath = '//*[@id="type1"]/div/table/tbody/tr[' + str(lastIndex-1) + ']/td[1]'
        rndEdDt = driver.find_element(By.XPATH, xpath).text.replace(' ', '')[:-3]
    print(leagYr, rnd, rndSrtDt, rndEdDt)
