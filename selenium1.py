from selenium import webdriver
from getpass import getpass

from  selenium.webdriver.common.by import By
username=input("Enter your username : ")
password=getpass("Enter your password : ")

driver=webdriver.Chrome("C:\\webdriver\\chromedriver.exe")
driver.get("http://localhost/capstone_CancerF/capstone_Cancer/index.php")

username_textbox=driver.find_element(By.ID,"username")
username_textbox.send_keys(username)
password_textbox=driver.find_element(By.ID,"login-password")
password_textbox.send_keys(password)

login_button=driver.find_element_by_id("login-btn").click()

login_button.submit()