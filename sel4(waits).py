#sychronization problem in automation : in  automation ,execution happen top to buttom ,
# at the time of execution particular line of the script is requried some element to perform that task
# by the time element is not availble,scipt will not wait for that element,imediatly jump for the next statement,then it will throuh an exception 'no such element'/'element not available'
#  there 2 diffent type of pages,1 part of code need to interact with page1,other part need to interact with page2,when we try to execute 2nd part of our code by that time 2nd page is not available
# it will not wait for the 2nd page it will directly go and execute 2nd code and will through an error
#this is the problem of synchronization ,basically balancing between the code,excecution also response of application
#there are 2 ways to overcome this problem : 1.we can make our application faster(this is not on our hands.network issu or other issue,more people accessing our application)
#but we can control our code(execution)
# 2.we can wait for same time:
#whichever statement is looking for certain element,we can just insert some wait command
#and specify some time
# Waits: Implicit Wait, Explicit Wait

# Implicit wait :

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import  Keys

driver = webdriver.Chrome(executable_path='/home/cbnits/Downloads/chromedriver_linux64/chromedriver')

driver.get('https://www.flipkart.com/')
# print(driver.title)
driver.implicitly_wait(10) #aplicable for all the elements of the page,we can specify this implicit wait 1 time in our script at the bigining and it will applicable for all elements,whichever element is taking time

assert 'Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, Books & More. Best Offers!' in driver.title

driver.find_element("xpath",'/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input').send_keys('sweetybiswas2927@gmail.com')
driver.find_element("xpath",'/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input').send_keys('sweety123')
driver.find_element('xpath','/html/body/div[2]/div/div/div/div/div[2]/div/form/div[4]/button/span').click()


#in implicit wait,within the given time if page is not loaded or element not present then it will through an exception

