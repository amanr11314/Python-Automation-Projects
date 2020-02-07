from selenium import webdriver 
import getpass
from selenium.webdriver.common.action_chains import ActionChains
import time 

uid=input('UID ')
password=getpass.getpass(prompt='Password: ', stream=None)

chrome = webdriver.Chrome()
url = ('https://uims.cuchd.in/uims/') 

def url_name(url): 
	chrome.get(url)
	time.sleep(4)

def login(username,pwd):
    uid_field=chrome.find_element_by_xpath('/html/body/form/div[4]/div/div/div[2]/div/input[1]')
    uid_field.send_keys(username)
    uid_field.send_keys("\ue004") #presses tab key automatically
    focused_elem = chrome.switch_to.active_element #switches focus to next element
    focused_elem.click()
    time.sleep(5)

    pwd_field=chrome.find_element_by_xpath('/html/body/form/div[4]/div/div/div[2]/div/input[1]')
    pwd_field.send_keys(pwd)

    loginButton=chrome.find_element_by_xpath('/html/body/form/div[4]/div/div/div[2]/div/input[2]')
    loginButton.click()
    time.sleep(4)

def menu_click():
    bttn=chrome.find_element_by_xpath('/html/body/form/div[4]/header/div[1]/div')
    bttn.click()
    option=[x for x in range(10)]
    option[0]='/html/body/form/div[4]/div[1]/div/div[1]/ul/li[1]/a'
    option[1]='/html/body/form/div[4]/div[1]/div/div[1]/ul/li[2]/a'
    option[2]='/html/body/form/div[4]/div[1]/div/div[1]/ul/li[3]/a'
    attendance = chrome.find_element_by_xpath(option[2])
    time.sleep(5)
    attendance.click()

url_name(url)
login(uid, password)
menu_click()

