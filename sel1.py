import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/home/cbnits/Downloads/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.amazon.com")


print(driver.title) #Returns Title of the page

print(driver.current_url) #returns the url of the page

#print(driver.page_source) # return the html code for the page

driver.find_element(By.XPATH,'//*[@id="nav-signin-tooltip"]/a/span').click()

time.sleep(10)

#driver.close() #close the browser(close 1 browser at a time)(close currently foccused browser)

#driver.quit() # closes all the browser


time.sleep(50)
print('done')