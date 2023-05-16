import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://finance.naver.com/")
time.sleep(1)

lst1 = []
for i in range(10) : 
    subject = driver.find_element(By.XPATH, f"/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[{i+1}]/th/a").text 
    lst1.append(subject)
print(lst1)


lst2 = []
for i in range(10) :
    nowMoney = driver.find_element(By.XPATH,f"/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[{i+1}]/td[1]").text
    lst2.append(nowMoney) 
print(lst2)

lst3 = []
for i in range(10) : 
    plusMoney = driver.find_element(By.XPATH,f"/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[{i+1}]/td[2]").text
    lst3.append(plusMoney) 
print(lst3)

lst4 = []
for i in range(10) : 
    plusPer = driver.find_element(By.XPATH,f"/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[{i+1}]/td[3]").text
    lst4.append(plusPer)   
print(lst4)

allList = list(zip(lst1,lst2,lst3,lst4))
for i in range(len(allList)) : 
    print(allList[i])