from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from password import log_password
from emailstore import email_test
from selenium. webdriver. common. keys import Keys
import pickle
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path=r"C://Users//TSS//Desktop//Aututest//chromedriver.exe",options=options)
driver.get(url='http://tutorialsninja.com/demo/index.php?route=account/login')
time.sleep(10)
try:
    driver.delete_all_cookies() 
    time.sleep(10)
    for cookie in pickle.load(open(f'{email_test}_cookies', 'rb')):
        driver.add_cookie(cookie)
    time.sleep(10)   
    driver.refresh()
    # email_field = driver.find_element(By.ID,"input-email")
    # email_field.send_keys(email_test)
    # pass_field = driver.find_element(By.ID,"input-password")
    # pass_field.send_keys(log_password)
    # pass_field.send_keys(Keys.ENTER)
    # time.sleep(5)
    # pickle.dump(driver.get_cookies(), open (f"{email_test}_cookies", "wb"))
except Exception as ex:
    print(ex)
       
