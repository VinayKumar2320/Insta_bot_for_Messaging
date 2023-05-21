from selenium import webdriver
from time import sleep
from logindets import email, password


class instabot():
    def open_browser(self):
        driver = webdriver.Firefox()
        driver.get("https://instagram.com")
        sleep(5)
        email_field= driver.find_element('xpath', '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')
        psw_field = driver.find_element('xpath', '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input')
        login_button = driver.find_element('xpath','/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]')
        email_field.send_keys(email)
        psw_field.send_keys(password)
        login_button.click()
        
insta_obj  = instabot()
insta_obj.open_browser()