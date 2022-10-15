import requests as req
import json
import regex as re
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

url = f"https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=en&gl=id&pb=!1m2!1y3349088126500062713!2y10226759696323505906!2m1!1i0!2i100!3e2!4m5!3b1!4b1!5b1!6b1!7b1!5m2!1sCFJFY6agEIujseMP8YOQgAg!7e81"

yello_river = f"https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=en&gl=id&pb=!1m2!1y3349087968132506677!2y15827256252848768519!2m1!2i10!3e1!4m5!3b1!4b1!5b1!6b1!7b1!5m2!1sub9HY4_FGJ223LUPza-ToAo!7e81"


def open_web(self, url):
        self.driver.get(url)
        wait = WebDriverWait(self.driver, MAX_WAIT)

        # wait to load review (ajax call)
        time.sleep(1)

        return 0

def capture_data(url):
    data = req.get(url)
    if data.status_code == 200:
        text = data.text
        text = text.replace(")]}'", "")
        # text = text.replace('null', "none")
        text = json.loads(text)
        return text
    else:
        print("Error")

def dump_json(data):
    
    with open("data.json", "w+") as f:
        json.dump(data, f, indent=4)

def init():
    chrome = webdriver.Chrome("selenium\chromedriver.exe")

def main(url):
    
    for i in range(100,2100,100):
        url = re.sub('!1i\d+', '!1i' + str(i), url)

        print(url)
        data = capture_data(url)
        dump_json(data)
        chrome = webdriver.Chrome("selenium\chromedriver.exe")
        chrome.get(url)
        wait = WebDriverWait(chrome, 5)
        # chrome.quit()

main(url)
# def testaja():
#     url = f"https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=en&gl=id&pb=!1m2!1y3349088126500062713!2y10226759696323505906!2m1!1i0!2i100!3e2!4m5!3b1!4b1!5b1!6b1!7b1!5m2!1sCFJFY6agEIujseMP8YOQgAg!7e81"

#     n = 0
#     while n < 1000:
#         url = re.sub('1i' + str(n-100), '1i' + str(n), url)
#         # print(n)
#         print(url)
#         n += 100
    
    # url = re.sub('!1i\d+', '!li' + str(), url)
    # data = req.get(url)
    # if data.status_code:
    #     print(data.status_code)



# def test():
#     # modify url
#     for i in range(100,2100,100):
#         url = re.sub('li' + str(i), 'li' + str(i+100) + '!', url)
#     # capture data
#     # dump json


    
    # data = capture_data()
    # print(data)
# res = req.get(url)
# print(res.status_code)
# data = res.headers
# print(data["Date "])

# import json
# import regex as re
# re.sub(r"\)]}'", '', data)
# ##load json from file
# with open('f3.txt', encoding='utf-8') as f:
#     data = json.load(f)

# ##show review
# print (data[2][0][3])


### test section

# import requests as req
# import regex as re

# url = f"https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=en&gl=id&pb=!1m2!1y3349088126500062713!2y10226759696323505906!2m1!1i0!2i10!3e2!4m5!3b1!4b1!5b1!6b1!7b1!5m2!1sCFJFY6agEIujseMP8YOQgAg!7e81"

# for i in range(100,2100,100):
#     print (i)
