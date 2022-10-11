# -*- coding: utf-8 -*-
from operator import truediv
from webbrowser import Chrome
import pandas as pd
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains



chrome = webdriver.Chrome("selenium\chromedriver.exe")
chrome.get("https://goo.gl/maps/2KJB4Qh5z4bDkhnKA")
time.sleep(5)
xpathreview = "/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[2]/span[2]"

bodyreview = "/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[11]/div[1]"

expandreview = "/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[11]/div[1]/div/div[3]/div[4]/jsl/button"

sorereview = "/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[9]/button[2]"

rating_class = "fzvQIb"
reviewer_class = "d4r55"
bodyreview_class = "MyEned"

scroll = 'div.siAUzd-neVct.section-scrollbox.cYB2Ge-oHo7ed.cYB2Ge-ti6hGc'

def get_rating():
    rating = chrome.find_elements_by_class_name(rating_class)
    for i in rating:
        print(i.text)

def get_reviewer():
    reviewer = chrome.find_elements_by_class_name(reviewer_class)
    for i in reviewer:
        print(i.text)

def get_body_review():
    body = chrome.find_elements_by_class_name(bodyreview_class)
    for i in body:
        if i.text != "":
            print(i.text)
        else :
            print("No review")

def scrolling():
    print ("scrolling time")
    elm = chrome.find_element_by_xpath('//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]')
    last_height = chrome.execute_script("return document.body.scrollHeight")
    last_height2 = chrome.execute_script("return document.body.scrollHeight", elm)
    new_height2 = chrome.execute_script("return arguments[0].scrollHeight", elm)

    print ("last height: ",last_height)
    print ("last height2: ",last_height2)
    print ("new height: ",new_height2)
    number = 0
    while True:
        number = number+1
        side_review = chrome.find_element_by_xpath('//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]')

        chrome.execute_script('arguments[0].scrollBy(0, 904);', side_review)
        time.sleep(2)
        new_height = chrome.execute_script("return arguments[0].scrollHeight", side_review)

        print ("new height: ", new_height)

        if new_height == last_height:
            break
        last_height = new_height


def scroll_test():
    print ("scrolling time")
    elm = chrome.find_element_by_xpath('//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]')

    last_height = chrome.execute_script("return arguments[0].scrollHeight", elm)

    print ("test height 1: ", chrome.execute_script("return arguments[0].scrollHeight", elm))
    print ("test height 2: ", chrome.execute_script("return document.body.scrollHeight", elm))

    number = 0
    while True:
        number = number+1
        scroll_size = chrome.execute_script("return document.body.scrollHeight")
        print ("scroll size: ", scroll_size)
        chrome.execute_script('arguments[0].scrollBy(0,' + str(scroll_size) + ');', elm)
        time.sleep(1)
        new_height = chrome.execute_script("return arguments[0].scrollHeight", elm)
        print ("new height:", new_height)
        print ("last height:", last_height)

        if new_height == last_height:
            break
        last_height = new_height
        print ("number: ", number)







review = chrome.find_element_by_xpath(xpathreview)
print (review.text)
review.click()
time.sleep(3)
sorereview = chrome.find_element_by_xpath(sorereview)
sorereview.click()
time.sleep(3)
change = chrome.find_element_by_xpath("/html/body/div[3]/div[3]/div[1]/ul/li[2]").click()
time.sleep(1)
get_rating()
time.sleep(1)
get_reviewer()
time.sleep(1)
get_body_review()
scroll_test()
# scrolling()
# side_review = chrome.find_element_by_xpath('//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]')
# test = chrome.execute_script("return arguments[0].scrollHeight", side_review )
# print (test)

# hehe = chrome.execute_script("return document.body.scrollHeight", side_review)
# print (hehe)



# expand = chrome.find_element_by_xpath(expandreview)
# expand.click()
# time.sleep(5)
# body = chrome.find_element_by_xpath(bodyreview).text
# print (body)
# time.sleep(5)
# chrome.close()





