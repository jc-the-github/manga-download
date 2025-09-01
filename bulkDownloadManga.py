# from selenium import webdriver
# from selenium import *
# from time import time
# from selenium.webdriver import Keys, ActionChains
# from selenium.webdriver.common.actions.action_builder import ActionBuilder
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.common import NoSuchElementException, ElementNotInteractableException
# from selenium.webdriver.support.wait import WebDriverWait
# from inputimeout import inputimeout, TimeoutOccurred
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import sys


# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.keys import Keys


# # 1. will go to link, 
# # scroll down if necessary
# # save as pdf
# # save to folder
# # repeat above steps for #MangaToDownload
# # send manga to kindle or remarkable if able

# def performAction(action, searchType, name, keys):
#     global driver
#     element = ''

#     # if searchType == 'CSS_SELECTOR':

#     # elif searchType == 'XPATH':
#     #     element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
#     #         (By.XPATH, name)))

#     if action == 'click':
#         WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
#             (By.CSS_SELECTOR, name))).click()
#     elif action == 'send_keys':
#         WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
#             (By.CSS_SELECTOR, name))).send_keys(keys)
#     elif action == 'get_attribute':
#         WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
#             (By.CSS_SELECTOR, name))).get_attribute(keys)


# def waitFuncDefault():
#     try:
#         time_over = inputimeout(
#             prompt='End code? (Input y)', timeout=1)
#         if str(time_over) == "y":
#             print("Ending code...")
#             exitTime = True
#             sys.exit()

#     except TimeoutOccurred:
#         print("cont")


# def waitFuncSpecified(waitAmount):
#     try:
#         time_over = inputimeout(
#             prompt='End code? (Input y)', timeout=waitAmount)
#         if str(time_over) == "y":
#             print("Ending code...")
#             exitTime = True
#             sys.exit()

#     except TimeoutOccurred:
#         print("cont")


# def fromElectronicsCategory():
#     global driver
#     driver.get("https://search.cashamerica.com/#/categories")
#     try:

#         time_over = inputimeout(prompt='End code? (Input y)', timeout=3)
#         if str(time_over) == "y":
#             print("Ending code...")
#             exitTime = True
#             sys.exit()
#     except TimeoutOccurred:
#         print("cont")


# def goToWebsite():
#     # options = webdriver.ChromeOptions()
#     # options.add_experimental_option('prefs', {
#     # "download.default_directory": "C:/Users/jcsne/OneDrive/Desktop/Programming/manga download/downloads", #Change default directory for downloads
#     # "download.prompt_for_download": False, #To auto download the file
#     # "download.directory_upgrade": True,
#     # "plugins.always_open_pdf_externally": True #It will not show PDF directly in chrome
#     # })
#     # driver = webdriver.Chrome(options=options)
#     # global driver
#     driver.get("https://weebcentral.com/chapters/01J76XZ36BHMDJ07F2JBZ3HA76")
#     waitFuncSpecified(100)
#     # waitFuncSpecified(10000)

#     # WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
#     #     (By.CSS_SELECTOR, "body > div.ng-scope > div > div > div.main-search > a"))).click()

#     # click address field
#     # WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
#     #     (By.ID, "address"))).click()
#     # agent = driver.execute_script("return navigator.userAgent")
#     # print('user agent ' + str(agent))

#     # # type in address
#     # WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
#     #     (By.ID, "address"))).send_keys('78741')

#     # # click apply
#     # WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
#     #     (By.CSS_SELECTOR, "body > div.modal.fade.ng-isolate-scope.in > div > div > form > div.modal-footer > button.btn.btn-primary"))).click()

#     # # click music instruments
#     # WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
#     #     (By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[4]/div/a"))).click()

#     # WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
#     #     (By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div[9]/a"))).click()


# def changeCategory():
#     global categoryIndex

#     # general musical instruments
#     if categoryIndex == 0:
#         element = 'body > div.ng-scope > div > div.container-fluid.ng-scope > div > div > div:nth-child(10) > div > a > img'
#         performAction('click', 'CSS_SELECTOR', element, '')

#         waitFuncSpecified(5)
#         element = '/html/body/div[1]/div/div[1]/search-form/form/div/span/button'
#         WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
#             (By.XPATH, element))).click()

#         scrollPages()
#         driver.back()
#         driver.back()
#         # waitFuncSpecified(50000)
#     # video games
#     elif categoryIndex == 1:
#         element = '/html/body/div[1]/div/div[2]/div/div/div[4]/div/a/img'
#         WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
#             (By.XPATH, element))).click()

#         element = 'body > div.ng-scope > div > div.container-fluid.ng-scope > div > div > div:nth-child(9) > a > div > h3'
#         performAction('click', 'CSS_SELECTOR', element, '')
#         print("wgy")

#         scrollPages()
#         driver.back()
#         driver.back()
#     # # general clothes and shoes
#     # elif categoryIndex == 2:
#     #     element = '/html/body/div[1]/div/div[2]/div/div/div[3]/div/a/img'
#     #     WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
#     #         (By.XPATH, element))).click()

#     #     waitFuncSpecified(5)
#     #     element = '/html/body/div[1]/div/div[1]/search-form/form/div/span/button'
#     #     WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
#     #         (By.XPATH, element))).click()

#     #     scrollPages()
#     #     driver.back()
#     #     driver.back()

#     # computer equipment
#     elif categoryIndex == 3:
#         element = '/html/body/div[1]/div/div[2]/div/div/div[4]/div/a/img'
#         WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
#             (By.XPATH, element))).click()

#         element = '/html/body/div[1]/div/div[3]/div/div/div[2]/a/div/h3'
#         WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
#             (By.XPATH, element))).click()

#         waitFuncSpecified(10)


#         scrollPages()
#         driver.back()
#         driver.back()

#     elif categoryIndex == 4:
#         # click electronics
#         element = '/html/body/div[1]/div/div[2]/div/div/div[4]/div/a/img'
#         WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
#             (By.XPATH, element))).click()

#         # click search bar
#         waitFuncSpecified(5)
#         # element = '/html/body/div[1]/div/div[3]/div/div/div[2]'
#         element = '/html/body/div[1]/div/div[1]/search-form/form/div/span/button'
#         WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
#             (By.XPATH, element))).click()

#         scrollPages()
#         driver.back()
#         driver.back()

# def scrollPages():

#     global categoryIndex
#     global pageScrollAmount
#     currentPageScrollAmount = pageScrollAmount
#     WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
#         (By.XPATH, '//*[@id="radiusRadios-499"]'))).click()

    
#     for i in range(currentPageScrollAmount):
#         # copy listing info
#         # body > div.ng-scope > div > div > div.container-fluid > div
#         # /html/body/div[1]/div/div/div[2]/div/div[2]/div[1]
        
#         # if i > 79:
#             saveHTML()
#             print("should b e scrolling")
#             WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
#             (By.CSS_SELECTOR, "body > div.ng-scope > div > div > div.container-fluid > div > div.col-xs-12.col-sm-9.no-float > div:nth-child(2) > ul > li.next > a"))).click()

#         # else:
#         #     waitFuncSpecified(1)

#         #     WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
#         #     (By.CSS_SELECTOR, "body > div.ng-scope > div > div > div.container-fluid > div > div.col-xs-12.col-sm-9.no-float > div:nth-child(2) > ul > li.next > a"))).click()


# def saveHTML():
#     global categories
#     fileName = categories[categoryIndex]
#     fileName = 'unsorted HTML Data/' + \
#         str(categories[categoryIndex]) + 'PawnHTML.txt'

#     waitFuncSpecified(1)
#     newPawnListingsHTML = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
#         (By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[2]/div[1]"))).get_attribute('outerHTML')

#     # save to file
#     # first read contents
#     pawnListingsHTMLFile = open(
#         fileName, 'r', encoding="utf8")
#     pawnListingsHTML = pawnListingsHTMLFile.read()
#     pawnListingsHTMLFile.close()

#     # add to contents
#     pawnListingsHTML += "\n"
#     pawnListingsHTML += str(newPawnListingsHTML)
#     print("huh " + pawnListingsHTML)

#     # write to contents
#     pawnListingsHTMLFile = open(fileName, 'w', encoding="utf8")
#     pawnListingsHTMLFile.write(str(pawnListingsHTML))
#     pawnListingsHTMLFile.close()


# # Vars
# service = Service()

# opts = webdriver.ChromeOptions()
# PROXY = '45.90.219.12:4444'
# user_agent = 'Mozilla/5.0 CK={} (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'

# webdriver.DesiredCapabilities.CHROME['proxy'] = {
#     "httpProxy": PROXY,
#     "ftpProxy": PROXY,
#     "sslProxy": PROXY,
#     "proxyType": "MANUAL",

# }

# webdriver.DesiredCapabilities.CHROME['acceptSslCerts'] = True
# opts.add_argument("user-agent="+user_agent)
# print(webdriver.DesiredCapabilities.CHROME)

# driver = webdriver.Chrome(service=service, options=opts)

# # with webdriver.Chrome() as driver:
# # ---- Start -----
# goToWebsite()
# categoryIndex = 0
# pageScrollAmount = 80
# categories = ['GeneralMusicInstruments', 'VideoGames',
#               'GeneralClothesandShoes', 'ComputerEquipment','GeneralElectronics']
# # CURRENTLY HAVE FIRST TO 80 PAGES AND THEN ANOTHER 160 OR SOMETHING LIKE THAT, 
# # MUST CHANGE
# for i in range(2):
#     # changeCategory()
#     # scrollPages()
#     categoryIndex += 4
#     pageScrollAmount = 185



# # webdriver.DesiredCapabilities.CHROME['proxy'] = {
# #     "httpProxy": PROXY,
# #     "ftpProxy": PROXY,
# #     "sslProxy": PROXY,
# #     "proxyType": "manual",
# # }

# # options.add_argument('--proxy-server=%s' % PROXY)

# # # Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36
# # options.add_argument('--ignore-certificate-errors')
# # options.add_argument('--ignore-ssl-errors')
# # options.add_argument(
# #     "user-agent=Mozilla/5.0 (Windows 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36")
# # driver = webdriver.Chrome(service=service, options=options)


# # main = Main()
# # pawnListingsHTMLFile = open(
# #     'unsorted HTML Data/unsortedPawnHTML.txt', 'r', encoding="utf8")
# # pawnListingsHTML = pawnListingsHTMLFile.read()
# # pawnListingsHTMLFile.close()
# # pawnListingsParser = pawnListingsParser(pawnListingsHTML)

# # main.matchPriceGuidesAndListings(main.parsedPawnListings, "OfferUp")
# # revealed.send_keys('78741')


# # btn btn-primary
# # button = driver.find_element(By.CLASS_NAME, u"form-control ng-pristine ng-valid ng-touched")
# # driver.implicitly_wait(10)
# # ActionChains(driver).move_to_element(button).click(button).perform()


# # driver.find_element(By.NAME, "btnI").click()

# # wait = WebDriverWait(driver, timeout=5000)


# # wait.until(lambda d : revealed.is_displayed())

# # revealed.send_keys("Displayed")
# # assert revealed.get_property("value") == "Displayed"

# # clickable = driver.find_element(By.CSS_SELECTOR, "#gbqfbb")
# # clickable.click()
# # clickable = driver.find_element(By.CSS_SELECTOR, "#gbqfbb")
# # ActionChains(driver)\
# #     .click(clickable)\
# #     .perform()


# # clickable = driver.find_element(by=id, value='gbqfbb')
# # ActionChains(driver)\
# #     .click(clickable)\
# #     .perform()

# # print(driver.title)


# # revealed = driver.find_element(By.CSS_SELECTOR, "#gbqfbb")
# # driver.find_element(By.ID, "gbqfbb").click()

# # driver.find_element(By.ID, "gbqfbb").click()

#     # waitFuncDefault()

#     # click apply button
#     # revealed = driver.find_element(
#     #     By.CSS_SELECTOR, "body > div.modal.fade.ng-isolate-scope.in > div > div > form > div.modal-footer > button.btn.btn-primary")
#     # driver.find_element(
#     #     By.CSS_SELECTOR, "body > div.modal.fade.ng-isolate-scope.in > div > div > form > div.modal-footer > button.btn.btn-primary").click()
#     # errors = [NoSuchElementException, ElementNotInteractableException]
#     # wait = WebDriverWait(
#     #     driver, timeout=2, poll_frequency=.2, ignored_exceptions=errors)
#     # wait.until(lambda d: revealed.send_keys("") or True)
