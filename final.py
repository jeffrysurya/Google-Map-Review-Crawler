from random import randint
import requests as req
import time
import regex as re

def get_data():
    n = 0
    page_size = 100
    url = "https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=en&gl=id&pb=!1m2!1y3349088126500062713!2y10226759696323505906!2m2!1i0!2i100!3e2!4m5!3b1!4b1!5b1!6b1!7b1!5m2!1sCFJFY6agEIujseMP8YOQgAg!7e81"
    while n < 1000:
        modifed_url = re.sub('!1i\d+', '!1i' + str(n), url)
        print(modifed_url)
        captured_data = req.get(modifed_url)
        wait = randint(2, 10)
        time.sleep(wait)
        print ("wait for : ", wait)
        if captured_data.status_code == 200:
            print(captured_data.status_code)
            n += page_size
            cleaned_data = clean_data(captured_data)
            filename = str(n)
            save_data(cleaned_data, filename)
        else:
            print ("Error : ", captured_data.status_code)
        

def clean_data(data):
    cleandata = data.text
    cleandata = re.sub(r"\)]}'", "", cleandata, 0, re.MULTILINE)
    cleandata = re.sub("null", '""', cleandata)
    return cleandata

def save_data(savedata, filename):
    with open(filename + '.txt', "w", encoding='utf_8') as f:
        f.write(savedata)


get_data()