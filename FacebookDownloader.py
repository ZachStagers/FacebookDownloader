#Imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import getpass




#Parameters
facebookUsername = input("Username:")
facebookPassword = getpass.getpass("Password:")
facebookURLextension = input("URL extension:")
fullFacebookURL = "https://www.facebook.com/" + facebookURLextension



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



#Go to your profile page, then photos page, then open the first photo.
browser.implicitly_wait(5)

profilePage = browser.find_element_by_xpath('//a[@href="'+fullFacebookURL+'"]')
profilePage.click()

photosPage = browser.find_element_by_xpath('//a[@href="'+fullFacebookURL+'/photos"]')
photosPage.click()

####Hardcoded for now, need to workout how to open first picture.
firstPhoto = browser.find_element_by_xpath('//a[@href="https://www.facebook.com/photo.php?fbid=10100860349916511&set=t.733485463&type=3"]')
firstPhoto.click()



#Open Actions menu
browser.implicitly_wait(100)
previousURL = browser.current_url

browser.find_element_by_xpath('//a[contains(@href="https://scontent-lht6-1.xx.fbcdn.net")]').click()


#actions = ActionChains(browser)
#actions.send_keys(Keys.TAB * 8)
#actions.send_keys(Keys.RETURN)
#actions.perform()