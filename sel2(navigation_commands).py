# opened 1 application using url after that thourh that i have opened one more url
# so 1st page will store in history
#want to go back to that history page then again want to come to leatest page
#this is called navigation
import time

from selenium import webdriver
from  selenium.webdriver.common.keys import  Keys


driver=webdriver.Chrome(executable_path='/home/cbnits/Downloads/chromedriver_linux64/chromedriver')

driver.get('https://www.flipkart.com/')
print(driver.title)
driver.get('https://www.amazon.com/')
time.sleep(5)
print(driver.title)



driver.back() #go to the history page
time.sleep(5)
print(driver.title)

driver.forward() # go to the current page
time.sleep(5)
print(driver.title)



