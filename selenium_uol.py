from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://www.uol.com.br")

driver.find_element_by_xpath("/html/body/header/div[2]/div/div[3]/div/div/input").click()

element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "searchForm"))
)

form = driver.find_element_by_id("searchForm")
elem = form.find_element_by_name("q")
elem.clear()
elem.send_keys("a vida")
elem.send_keys(Keys.RETURN)

element = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gs-webResult"))
)

resultados = driver.find_elements_by_css_selector(".gs-webResult")

for item in resultados:
    titulo = item.find_element_by_css_selector(".gs-title").text
    print(titulo)