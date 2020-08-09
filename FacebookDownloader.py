#Imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import getpass
import time



#Define Functions
def downloadPhoto():
    #Function to open actions menu and download the photo.
    actionsMenu = browser.find_element_by_xpath("//div[@class='btwxx1t3 j83agx80 hybvsw6c ll8tlv6m']//div[@class='nqmvxvec j83agx80 jnigpg78 cxgpxx05 dflh9lhu sj5x9vvc scb9dxdr odw8uiq3']//div[@aria-label='Actions for this post']")
    browser.execute_script("arguments[0].click()", actionsMenu)

    download = browser.find_element_by_xpath('//a[contains(@class, "oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 j83agx80 p7hjln8o kvgmc6g5 oi9244e8 oygrvhab h676nmdw cxgpxx05 dflh9lhu sj5x9vvc scb9dxdr i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l bp9cbjyn dwo3fsh8 btwxx1t3 pfnyh3mw du4w35lb")]')
    download.click()



def navigateNextPhoto():
    #Function to navigate to the next photo if there is one.
    nextPhoto = browser.find_element_by_xpath("//div[@aria-label='Next photo']")
    browser.execute_script("arguments[0].click()", nextPhoto)
    time.sleep(2)



#Parameters
facebookUsername = input("Username:")
facebookPassword = getpass.getpass("Password:")
facebookURLextension = input("URL extension:")



#Variables
fullFacebookURL = "https://www.facebook.com/" + facebookURLextension
lastPhoto = False



#Set Browser options 
option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})



#Instantiate Browser using options
browser = webdriver.Chrome(chrome_options=option)



#Go to Facebook and login.
browser.get("http://www.facebook.com")

username = browser.find_element_by_name("email")
username.send_keys(facebookUsername)

password = browser.find_element_by_name("pass")
password.send_keys(facebookPassword + Keys.RETURN)



#Go to profile page, then photos page, then open the first photo.
browser.implicitly_wait(5)

profilePage = browser.find_element_by_xpath('//a[@href="'+fullFacebookURL+'"]')
profilePage.click()

photosPage = browser.find_element_by_xpath('//a[@href="'+fullFacebookURL+'/photos"]')
photosPage.click()

firstPhoto = browser.find_element_by_xpath('//a[contains(@href, "/photo.php?fbid")]')
firstPhoto.click()



#Download photos!
while(lastPhoto == False):
    downloadPhoto()
    navigateNextPhoto()