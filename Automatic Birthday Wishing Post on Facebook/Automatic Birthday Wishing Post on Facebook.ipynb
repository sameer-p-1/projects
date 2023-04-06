import datetime
from dotenv import load_dotenv
import os

from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.chrome.options import Options 
from selenium.common.exceptions import TimeoutException 
from selenium.webdriver.common.keys import Keys 
import time


friend = None
 

load_dotenv()
usr = os.environ.get('User')
password = os.environ.get('Password')


driver_path = r"C:\Users\HP\Downloads\chromedriver_win32\chromedriver.exe"


chOptions = webdriver.ChromeOptions()

# chOptions.add_argument(r"user-data-C:\Users\user_name\AppData\Local\Google\Chrome\User Data")

driver = webdriver.Chrome(executable_path = driver_path,options = chOptions)
driver.get("https://www.facebook.com/")

time.sleep(3)

#username_field = driver.find_elements_by_xpath('//*[@id ="email"]')
username = driver.find_element(By.NAME, 'email')
username.send_keys(usr)

password_field = driver.find_element(By.ID, 'pass')
password_field.send_keys(password)

submit_button = driver.find_element(By.NAME, 'login')
submit_button.click()

time.sleep(3)

driver.get('https://www.facebook.com/events/birthdays/')

time.sleep(8)

message = "Happy Birthday!!"

while(1):
    try:
        message_fields = driver.find_element(By.XPATH, "//div[@class = '_1mf _1mj']") 
        message_fields.send_keys(message)
        message_fields.send_keys(Keys.RETURN)  
    except Exception as e:
        print("NO Birthdays Today!")
        pass
        break


#message_fields = driver.find_element(By.XPATH, "//div[@class = '_1mf _1mj']")
#message_fields.send_keys(message)
#message_fields.send_keys(Keys.RETURN)
# print(len(message_fields))
# for msg in message_fields:
#     msg.send_keys(message)

element = driver.find_element(By.XPATH, "//div[@class = 'q9uorilb l9j0dhe7 pzggbiyp du4w35lb']")
element.click()
time.sleep(2)

logout = driver.find_elements(By.XPATH,"//div[@data-visualcompletion='ignore-dynamic']")
logout[4].click()

time.sleep(2)

driver.close()