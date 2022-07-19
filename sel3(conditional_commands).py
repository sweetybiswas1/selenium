# when we are automating webpages ,we need to verify certain elements ,checkboxes,radio buttons, enabled,selected or not
# is_displayed()
# is_enabled()
# > this both used for any kind of any kind of web elements

# is_selected()
# > used for check boxes and radio buttons
#conditional commands returns boolean value : true.false
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import  Keys

driver = webdriver.Chrome(executable_path='/home/cbnits/Downloads/chromedriver_linux64/chromedriver')

driver.get('https://www.flipkart.com/')
time.sleep(5)

login_page=driver.find_element("xpath",'//*[@id="container"]/div/div[1]/div[1]/div[2]/div[3]/div/div/div/a')
print(login_page.is_displayed())

email=driver.find_element("xpath",'/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input')
print(email.is_displayed()) # returns True/False based of the element status
print(email.is_enabled())

email.send_keys('sweetybiswas2927@gmail.com')


pwd=driver.find_element("xpath",'/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input')
print(pwd.is_displayed()) # returns True/False based of the element status
print(pwd.is_enabled())

pwd.send_keys('sweety123')

driver.find_element('xpath','/html/body/div[2]/div/div/div/div/div[2]/div/form/div[4]/button/span').click()








'''
#driver.get('https://www.amazon.in/')
#driver.find_element(By.XPATH,'//*[@id="nav-signin-tooltip"]/a/span').click()
time.sleep(5)
ele=driver.find_element(By.XPATH,'//*[@id="ap_email"]')
#Will now verify
print(ele.is_displayed()) # returns True/False based of the element status
print(ele.is_enabled())
'''