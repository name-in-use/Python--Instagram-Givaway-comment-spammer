from selenium import webdriver
import os
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import ui
import random
'''
Christos Karounias IG spammer
'''
class InstaBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.instagram.com/')
        sleep(2)
        # accept cookies
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Accept']")))\
            .click()
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')\
            .send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')\
            .send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(4)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')\
            .click()
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')\
            .click()
        sleep(1)

    def GivawayPost(self):
        
        for y in range(7):
            self.driver.get('GIVAWAY URL')
            sleep_random = random.randint(25,35)
            
            sleep(4)
            # click post's comments
            self.driver.find_element_by_class_name("RxpZH").click()
            for x in range(8):
                self.driver.find_element_by_xpath(
                    "//textarea[@placeholder='Add a comment…']").send_keys('YOUR COMMENT HERE')
                self.driver.find_element_by_xpath(
                    "//*[@id='react-root']/section/main/div/div[1]/article/div[3]/section[3]/div/form/button").click()
                sleep( sleep_random)
        sleep(50)



mybot = InstaBot('INSTAGRAM USERNAME', 'INSTAGRAM PASSWORD')
mybot.GivawayPost()
