from nbformat import read
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import numpy as np
import time
from termcolor import colored


ids = ["16","17", "18", "19", "22", "26"]
open_link = 1

# Read password in pas.txt

f = open('pas.txt', 'r')
for line in f.readlines():
    passw = line.strip().split(',')
print(colored("Password taken", 'red'))


#Initializing Browser with options

options = webdriver.ChromeOptions() 
options.add_argument("user-data-dir=C:\\Users\\YOURUSERNAMEWINDOWS\\AppData\\Local\\Google\\Chrome\\User Data")
options.add_argument("profile-directory=Profile 1")

browser = webdriver.Chrome(executable_path=r".\\chromedriver.exe", chrome_options=options, service_args='')
channel = "Link of the server and channel"
browser.get(channel)
print(colored("Browser opened", 'green'))

time.sleep(1.5)

#Login

try:
    login = browser.find_element("xpath",'//*[@id="app-mount"]/div[2]/div/div/div/section/div/div[2]/div/div/div[2]/div[2]').text == 'Please log in again.'
    browser.find_element("xpath",'//*[@id="app-mount"]/div[2]/div/div/div/section/div/div[2]/div/div/div[3]/button[1]').click()
    time.sleep(2)
    browser.find_element("xpath",'//*[@id="app-mount"]/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/div[1]/div/div[2]/input').send_keys('yyxxzn@gmail.com')
    browser.find_element("xpath",'//*[@id="app-mount"]/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/div[2]/div/input').send_keys(passw)
    browser.find_element("xpath",'//*[@id="app-mount"]/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/button[2]').click()
    print(colored("Logged in", 'red'))
    time.sleep(2)

except:
    print(colored("Login not needed", 'red'))


#Closing Dividers

for i in range(1, 2):
        try:
            browser.find_element("xpath","/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[1]/nav/div[4]/ul/li[" + str(i) + "]/div/div[1][@aria-expanded = 'true']")
            browser.find_element("xpath","/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[1]/nav/div[4]/ul/li[" + str(i) + "]").click()
            print(colored("Closing Dividers", 'blue'))
        except:
            print(colored("No dividers to close", 'blue'))
            pass

try:
    browser.find_element("xpath",'/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[1]/nav/div[4]/ul/li[8]').click()
except:
    pass

#Main program

while(open_link):
    for i in range(0, 5):
        xpath = '//*[@id="channels"]/ul/li[' + ids[i] + ']/div/div/a'
        link = browser.find_element("xpath", xpath)
        attr = link.get_attribute("aria-label")
        if (attr.split()[0] == 'unread,'):
            print(colored("Found link, opening it", 'green'))
            browser.find_element("xpath", '/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[1]/nav/div[4]/ul/li['+ ids[i] + ']').click()
            time.sleep(0.5)
            try:
                try:
                    link_to_click = browser.find_element("xpath","/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[3]/div[2]/main/div[1]/div/div/ol/li[last()]/div/div[2]/article/div/div/div[1]/a")
                    link_to_click_alt = browser.find_element("/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[3]/div[2]/main/div[1]/div/div/ol/li[49]/div/div[2]/article/div/div/div[2]/a")
                except:
                    pass
                try:
                    browser.find_element("xpath","/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[3]/div[2]/main/div[1]/div/div/ol/li[last()]/div/div[2]/article/div/div/div[1]/a").click()
                except:
                    pass
                try:
                    browser.find_element("/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[3]/div[2]/main/div[1]/div/div/ol/li[49]/div/div[2]/article/div/div/div[2]/a").click
                    #/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[3]/div[2]/main/div[1]/div/div/ol/li[50]/div/div[2]/article/div/div/div[1]/a
                except:
                    pass                                      
                amz = browser.find_element("xpath","/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[3]/div[2]/main/div[1]/div/div/ol/li[last()]/div/div[2]/article/div/div/div[1]/a").get_attribute("href")
                amz = amz[8:14]
                if (amz == 'amazon'):
                    print(colored("Amazon Link", 'green'))
                    link_to_click.click()
                    time.sleep(0.5)
                    try:
                        browser.find_element("xpath",'//*[@id="app-mount"]/div[4]/div[2]/div/div/form/div[2]/div/div').click()
                    except:
                        pass
                    time.sleep(2)
                    #amz_auto(amz)
                else:
                    link_to_click.click()
                    time.sleep(0.5)
                    try:
                        browser.find_element("xpath",'//*[@id="app-mount"]/div[4]/div[2]/div/div/form/div[2]/div/div').click()
                    except:
                        pass
                    time.sleep(2) 
            except:
                print(colored("No link in message", 'red'))
            
            back = 1
            while(back):
                try:
                    browser.find_element("xpath",'/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[1]/nav/div[4]/ul/li[8]').click()
                    print(colored("Back to Discord", 'green'))
                    back = 0
                except:
                    pass


