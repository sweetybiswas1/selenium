# Explicit Wait :
# always look for the element,,which is displayed or available on the page
# it is completly based on the condition not based on time
# if we have 1o elements,we have to put explicit wait for 10 times bcz we need to define certain condition
'''
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import  Keys

driver = webdriver.Chrome(executable_path='/home/cbnits/Downloads/chromedriver_linux64/chromedriver')
driver.implicitly_wait(5)
driver.maximize_window() # maximize the window

driver.get('https://www.flipkart.com/')

driver.find_element("xpath",'/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input').send_keys('sweetybiswas2927@gmail.com')
driver.find_element("xpath",'/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input').send_keys('sweety123')
driver.find_element('xpath','/html/body/div[2]/div/div/div/div/div[2]/div/form/div[4]/button/span').click()
driver.find_element('xpath','//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input').send_keys('mobiles')
time.sleep(10)
print('done')
#x=driver.find_element(By.XPATH,"//*[@id='container']/div/div[1]/div[1]/div[2]/div[2]/form/div/button")

x=driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[1]/div[2]/div[2]/form/div/button')



print(x.is_displayed()) # returns True/False based of the element status
print(x.is_enabled())
x.click()

print('kkkk')

#x=driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[1]/div[2]/div[2]/form/div/button')


'''


import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import  Keys
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome(executable_path='/home/cbnits/Downloads/chromedriver_linux64/chromedriver')

driver.implicitly_wait(5)

driver.maximize_window() # maximize the window

driver.get('https://www.amazon.in/')

driver.find_element('xpath','//*[@id="nav-link-accountList"]/span').click()



driver.find_element("xpath",'//*[@id="ap_email"]').send_keys('7980681837')
driver.find_element("xpath",'//*[@id="continue"]').click()


driver.find_element('xpath','//*[@id="ap_password"]').send_keys('sweety123')

driver.find_element("xpath",'//*[@id="signInSubmit"]').click()


driver.find_element(By.ID,'twotabsearchtextbox').send_keys('mobiles')

driver.find_element(By.ID,'nav-search-submit-button').click()
# Explicit wait
wait=WebDriverWait(driver,10)

ele=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='p_89/Redmi']/span/a/div/label/i")))
ele.click()

time.sleep(10)

