from selenium import webdriver 
import getpass
from selenium.webdriver.common.action_chains import ActionChains
import time 

username = input('Username: ')
password = getpass.getpass(prompt='Password: ', stream=None)

chrome = webdriver.Chrome()
chrome.maximize_window() #starts chrome in maximized window
url = ('https://www.instagram.com/accounts/login/?source=auth_switcher') 

def url_name(url): 
	chrome.get(url)
	time.sleep(4) 

def login(username, your_password):
	# finds the username box 
	time.sleep(4)
	usern = chrome.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input')
	# sends the entered username 
	usern.send_keys(username)
	time.sleep(4)
	usern.send_keys("\ue004")
	
	focused_elem = chrome.switch_to.active_element #switches to next element
	focused_elem.send_keys(your_password)
	
	#{ finds the password box 
	# passw = chrome.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input')
	# sends the entered password 
	# passw.send_keys(your_password)}

	# finds the login button 
	log_cl = chrome.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button')

	log_cl.click() # clicks the login button 
	time.sleep(4);not_now = chrome.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]');not_now.click();time.sleep(4)

def search_user(username):
	search_box=chrome.find_element_by_xpath('/html/body/div[1]/section/div/div[1]/div/div[2]/input')
	search_box.send_keys(username)
	time.sleep(4)
	search_result=chrome.find_element_by_xpath('/html/body/div[1]/section/div/div[1]/div/div[2]/div[2]/div[2]/div/a')
	search_result.click()
	time.sleep(4)
	msg_button=chrome.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/button')
	msg_button.click()
	time.sleep(4)

def logout():
	profileUrl='https://www.instagram.com/'+username
	url_name(profileUrl)
	settings_button=chrome.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/div/button')
	settings_button.click()
	time.sleep(3)
	logout_opt=chrome.find_element_by_xpath('/html/body/div[4]/div/div/div/button[9]')
	logout_opt.click()

def dm():
    direct=chrome.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[1]/a');direct.click();time.sleep(4);mess=chrome.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]');mess.click();time.sleep(2);

def like():	#autolikes the currently loaded all posts ...
    actionchains = ActionChains(chrome);posts = chrome.find_elements_by_css_selector("[class^=_9AhH0]");time.sleep(4)
    for post in posts:
    	actionchains.double_click(post).perform()
    # first_img = chrome.find_element_by_class_name('_9AhH0');time.sleep(4);actionchains = ActionChains(chrome);actionchains.double_click(first_img).perform()
    # sec_img=('/html/body/div[1]/section/main/section/div[2]/div[1]/div/article[2]/div[1]/div/div/div[2]/div/div/div/div/ul/li[1]/div/div/div/div/div[1]/img')
    
def share_a_post():	#works for single first post to be shared only..
    time.sleep(4)
    postsOption=chrome.find_elements_by_css_selector("[class^=MEAGs]")
    for post in postsOption:
        post.click()
        time.sleep(3)
        sh_button=chrome.find_element_by_xpath('/html/body/div[4]/div/div/div/button[4]')
        sh_button.click()
        time.sleep(3)
        sh_button_direct=chrome.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/div[1]')
        sh_button_direct.click()
        time.sleep(4)
        search_box=chrome.find_element_by_xpath('/html/body/div[5]/div/div[2]/div[1]/div/div[2]/input')
        search_box.send_keys('amanraj')
        time.sleep(5)
        result=chrome.find_element_by_xpath('/html/body/div[5]/div/div[2]/div[2]/div[1]')
        result.click()
        time.sleep(3)
        send_bttn=chrome.find_element_by_xpath('/html/body/div[5]/div/div[1]/div/div[2]/div/button')
        send_bttn.click()
        time.sleep(4)
        

url_name(url)

login(username, password)

def message_first_user(message):
    dm()
    msg_box=chrome.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div/textarea')
    msg_box.send_keys(message)
    time.sleep(2)
    msg_box.send_keys("\ue007")
                

def message_user(search_name):
  
	dm()

	search_user(search_name)
	msg_box=chrome.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div/textarea')

	# msg_list=[str(x) for x in range(5)]
	# msg_list[0]='/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]'
	# msg_list[1]='/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[2]'
	# msg_list[2]='/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[3]'

	msg_list=[str('this is message' + str(x) ) for x in range(5)]

	msg_list[0]='Hey there i\'m using instagram'

	# your_message = 'Hey'
	for your_message in msg_list:
                
                msg_box.send_keys(your_message)
                time.sleep(2)
                msg_box.send_keys("\ue007")
                #presses enter key
                # msg_send=chrome.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/button')
                # msg_send.click()
                time.sleep(2)

def search_user_from_home(search_name):
    searchBox = chrome.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input')
    searchBox.send_keys(search_name)
    time.sleep(3)
    firstRelevantResult = chrome.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]')
    firstRelevantResult.click()
    time.sleep(10)
    # test=chrome.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/a[1]')
    bioURL=chrome.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/a[1]')
    # bioURL=chrome.find_elements_by_css_selector("[class^=yLUwa]")
    time.sleep(8)
    bioURL.click()


# message_first_user()
# search_user_from_home('garyvee')
# like()
# share_a_post()
# dm()
message_user('rishabhk812')
# logout()








