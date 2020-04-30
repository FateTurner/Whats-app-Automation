from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#Whatsapp

user = str(input("Type who you want to send to:\n"))
message = str(input("Type what you want to send:\n"))
l = int(input("Type how many times you want to send:\n"))

#local path
path  = "C:\Program Files (x86)\chromedriver.exe"

#driver setup
driver = webdriver.Chrome(path)
driver.get("https:web.whatsapp.com")

time.sleep(15)

user_search = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]")
user_search.click()
user_search.send_keys(user)
time.sleep(6)
user_search.send_keys(Keys.ARROW_DOWN)
user_search.click()
time.sleep(6)


box = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")
for i in range(l):
    box.send_keys(message, "\n")
box.send_keys(Keys.RETURN)
