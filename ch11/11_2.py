# pip install selenium
# pip install webdriver_manager
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

#options = webdriver.ChromeOptions()
#options.add_experimental_option("excludeSwitches", ["enable-logging"])
#browser = webdriver.Chrome(options=options)

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.naver.com/")
time.sleep(2)
driver.find_element(
    By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[1]/ul[2]/li[2]/a").click()
time.sleep(3)

newsTitle = driver.find_element(
    By.XPATH, "/html/body/div[2]/div/section[1]/div[2]/div/div[1]/div[2]/div/div/div[2]/ul[2]/li[1]/a/div[2]/div").text
time.sleep(3)
print(newsTitle)
