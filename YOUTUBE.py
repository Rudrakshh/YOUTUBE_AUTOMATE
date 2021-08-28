from sys import maxsize
from selenium import webdriver
import pyautogui
import time
print("YOU CAN WATCH ANY 5 MINUTE YOUTUBE VIDEO")
print()
print("ENTER VIDEO U WANT TO WATCH:-")
name1=input()
driver=webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://www.youtube.com/")
driver.maximize_window()
searchbox=driver.find_element_by_id("search")
searchbox.send_keys(name1)
entersearch=driver.find_element_by_xpath('//*[@id="search-icon-legacy"]/yt-icon')
entersearch.click()
time.sleep(5)
pyautogui.moveTo(511,362)
pyautogui.click()
searchbox.send_keys(name1)
time.sleep(500)
driver.quit()
