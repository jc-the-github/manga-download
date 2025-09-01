# import weasyprint
# weasyprint.HTML('https://weebcentral.com/chapters/01J76XZ36BHKNFA0SVP19XVB7C').write_pdf()
from selenium import webdriver
from selenium import *
from time import time
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.support.wait import WebDriverWait
from inputimeout import inputimeout, TimeoutOccurred
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import pdfkit
import re
import requests
from bs4 import BeautifulSoup
from PIL import Image
import os


# import weasyprint
imageNamesArrays = []
amountChaptersToDownload = 25

startingChapterNum = 186
urlToDownloadFrom = "https://weebcentral.com/chapters/01J76XZ8W6EK7BJCR00DYGD7B3"
# do not include space after name
pdfName = "The Batend"

secondstartingChapterNum = 40
secondurlToDownloadFrom = "https://weebcentral.com/chapters/01J76XZ36BKT346FZ5ME3APB0K"
# do not include space after name
secondpdfName = "Sakamoto Days"
do2ndManga = False
# pdfName = ""


# def getFileNames():
#     filePath = "C:\Users\jcsne\OneDrive\Desktop\Programming\manga download"
#     fileType = ".png"
#     paths = []
#     for root, dirs, files in os.walk(filePath):
#         for file in files:
#             if file.lower().endswith(fileType.lower()):
#                 paths.append(os.path.join(root, file))
#     return(paths)

def saveAsPDF(imageNamesArray, currentChapterNum):
    global pdfName
    newNamePDFFile = pdfName + " " + str(startingChapterNum + currentChapterNum)  + ".pdf"
    images = []
    for f in imageNamesArray:
        try:

            images.append(Image.open(f))
        except Exception as e:
            print("Error unable to add image to pdf array: " + str(e))
            print("Unable to add image to pdf array: " + f)
    # images = [
    # Image.open("C:\Users\jcsne\OneDrive\Desktop\Programming\manga download" + f)
    # for f in ["bbd.jpg", "bbd1.jpg", "bbd2.jpg"]
    # ]

    pdf_path = "C:/Users/jcsne/OneDrive/Desktop/Programming/manga download/createdPDFs/" + newNamePDFFile
        
    images[0].save(
        pdf_path, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:]
    )


def changeURLS():
    # print("")
    # go to website
    global urlToDownloadFrom
    newUrl = urlToDownloadFrom
    site = newUrl
    global amountChaptersToDownload
    driver.get(newUrl)

    for i in range(amountChaptersToDownload):
        # newNamePDFFile = "The BATEnd " + str(startingChapterNum + i)  + ".pdf"

        waitFuncSpecified(3)
        html_source = driver.page_source
        soup = BeautifulSoup(html_source, 'html.parser')
        # print(soup)
        img_tags = soup.find_all('img')

        urls = [img['src'] for img in img_tags]

        index = 1
        newImageNameArray = []
        newpath = r"C:/Users/jcsne/OneDrive/Desktop/Programming/manga download/" + pdfName 
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        for url in urls:
            print("hi")
            filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
            if not filename:
                print("Regex didn't match with the url: {}".format(url))
                continue
            newImageNameArray.append(pdfName + "/" +filename.group(1))
            with open(pdfName + "/" + filename.group(1), 'wb') as f:
                if 'http' not in url:
                    # sometimes an image source can be relative 
                    # if it is provide the base url which also happens 
                    # to be the site variable atm. 
                    url = '{}{}'.format(site, url)
                response = requests.get(url)
                f.write(response.content)
        imageNamesArrays.append(newImageNameArray)
        saveAsPDF(newImageNameArray, i)
        # pdfkit.from_url(newUrl, newNamePDFFile)
        # weasyprint.HTML(newUrl).write_pdf(newNamePDFFile)
        # go to next chapter
        element = '/html/body/main/section[1]/div/div[1]/button[6]'
        
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
            (By.XPATH, element))).click()
        waitFuncSpecified(10)
        newUrl = driver.current_url
        site = newUrl
        print("new url: " + newUrl)
    f = open("lastURLtoContinueFrom.txt", "r+")
    cont = f.read()
    f.write(cont + "\n" + pdfName + " = " + str(site))

def waitFuncSpecified(waitAmount):
    try:
        time_over = inputimeout(
            prompt='End code? (Input y)', timeout=waitAmount)
        if str(time_over) == "y":
            print("Ending code...")
            exitTime = True
            sys.exit()
    except TimeoutOccurred:
        print("cont")

def performAction(action, searchType, name, keys):
    global driver
    element = ''

    # if searchType == 'CSS_SELECTOR':

    # elif searchType == 'XPATH':
    #     element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
    #         (By.XPATH, name)))

    if action == 'click':
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, name))).click()
    elif action == 'send_keys':
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, name))).send_keys(keys)
    elif action == 'get_attribute':
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, name))).get_attribute(keys)

service = Service()

opts = webdriver.ChromeOptions()
PROXY = '45.90.219.12:4444'
user_agent = 'Mozilla/5.0 CK={} (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'

webdriver.DesiredCapabilities.CHROME['proxy'] = {
    "httpProxy": PROXY,
    "ftpProxy": PROXY,
    "sslProxy": PROXY,
    "proxyType": "MANUAL",

}

webdriver.DesiredCapabilities.CHROME['acceptSslCerts'] = True
opts.add_argument("user-agent="+user_agent)
print(webdriver.DesiredCapabilities.CHROME)

driver = webdriver.Chrome(service=service, options=opts)
changeURLS()
print("Done M8tey~ :DD #1")
if do2ndManga:
    urlToDownloadFrom = secondurlToDownloadFrom
    pdfName = secondpdfName
    imageNamesArrays = []
    startingChapterNum = secondstartingChapterNum

    changeURLS()
    print("Done M8tey~ :DD #2")

# saveAsPDF(["hi"], 2)
# pdfkit.from_url('https://weebcentral.com/chapters/01J76XZ36BHKNFA0SVP19XVB7C', '1.pdf')