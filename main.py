from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome('C:/Path/to/chromedriver')
driver.get("https://www.google.com.br")

driver.find_element_by_name("q").send_keys("Rua Olivio Basilio Marçal - 420" + Keys.RETURN)
driver.find_element_by_class_name("yYlJEf ").send_keys( Keys.RETURN) 
driver.find_element_by_xpath('//*[@id="omnibox-directions"]/div/div[2]/div/div/div[1]/div[2]/button').send_keys( Keys.RETURN)

driver.find_element_by_xpath('//*[@id="omnibox-directions"]/div/div[2]/div/div/div[1]/div[3]/button').send_keys( Keys.RETURN)

driver.find_element_by_xpath('//*[@id="omnibox-directions"]/div/div[2]/div/div/div[1]/div[4]/button').send_keys( Keys.RETURN)

driver.find_element_by_xpath('//*[@id="omnibox-directions"]/div/div[2]/div/div/div[1]/div[5]/button').send_keys( Keys.RETURN)

driver.find_element_by_xpath('//*[@id="omnibox-directions"]/div/div[2]/div/div/div[1]/div[6]/button').send_keys( Keys.RETURN)



#driver.find_element("Rota").send_keys( Keys.RETURN)

#driver.quit()
