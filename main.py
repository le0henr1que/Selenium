from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
import re
import json
from datetime import datetime
from collections import Counter as cnt

driver = webdriver.Chrome('C:/Path/to/chromedriver')
driver.get("https://www.google.com.br")
time.sleep(10)
driver.find_element_by_name("q").send_keys("Rua Olivio Basilio Marçal - 420" + Keys.RETURN)
time.sleep(10)

driver.find_element_by_xpath('/html/body/div[7]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[2]/div/div[1]').click()
time.sleep(15)
temp = driver.find_elements_by_xpath('/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[5]/div/div/div[3]/div[1]')[0].text


driver.find_element_by_xpath('//*[@id="omnibox-directions"]/div/div[2]/div/div/div[1]/div[2]/button').send_keys( Keys.RETURN)
time.sleep(5)
tempa = driver.find_elements_by_xpath('/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[5]/div/div/div[1]/div[1]')[0].text

driver.find_element_by_xpath('//*[@id="omnibox-directions"]/div/div[2]/div/div/div[1]/div[3]/button').send_keys( Keys.RETURN)
time.sleep(5)
tempb = driver.find_elements_by_xpath('/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[7]/div/div/div[3]/div[1]')[0].text


driver.find_element_by_xpath('//*[@id="omnibox-directions"]/div/div[2]/div/div/div[1]/div[4]/button').send_keys( Keys.RETURN)
time.sleep(5)
tempc = driver.find_elements_by_xpath('/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[5]/div/div/div[3]/div[1]')[0].text

print("--------------------------------------------Calculo de tempo até em casa-------------------------------------")
print("Recomendado:" + temp  )
print(" ")
print("Carro:" + tempa )
print(" ")
print("Trem:" + tempb )
print(" ")
print("Andando:" + tempc )



#driver.quit()
