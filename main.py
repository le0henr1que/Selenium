from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get("https://www.google.com.br")
driver.find_element_by_name("q").send_keys("Rua Olivio Basilio Marçal - 420" + Keys.RETURN)
driver.find_element_by_class_name("hide-focus-ring").send_keys( Keys.RETURN)
driver.find_element("Rota").send_keys( Keys.RETURN)