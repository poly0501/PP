from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from pymongo import MongoClient
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

from pymongo import MongoClient
from pprint import pprint

def parse(data_string):
    if data_string == "":
        curr = None
    else:
        data_list = data_string.split()
        if len(data_list) == 2:
            n = str(data_list[1])
            dan = str(data_list[2])
        elif len(data_list) == 3:
            n = str(data_list[1])
            dan = str(data_list[2])
        elif len(data_list) == 4:
            n = str(data_list[1])
            dan = str(data_list[2])
        elif len(data_list) == 5:
            n = str(data_list[1])
            dan = str(data_list[2])
        else:
            curr = None
    return curr


def p_lot(data_string):
    if data_string == "":
        curr = None
    else:
        data_list = data_string.split()
        #print(data_list)
        numer = str(data_list[1])
    return numer


def p_price(data_string):
    t=0
    n=len(data_string)
    if data_string == "":
        curr = None
    else:
        for i in data_string:
            if i !="\n":
                t+=1
            else:
                break
    data_string = data_string[0:t]
    # print(t)
    # print(data_string)
    return (data_string)

def isbavl(nasv,dan):
    if (nasv == "Площадь"):
        nasv = 'square'
        #     вставить
    elif (nasv == "Этажей"):
        nasv = 'floors'
        #     вставить
    elif (nasv == "Этаж"):
        nasv = 'floor'
        #     вставить
    else:
        nasv = None
        dan = None
    return (nasv, dan)






def p_dann(data_string):
    t=0
    n=len(data_string)
    if data_string != "":
        for i in data_string:
            if i !="\n":
                t+=1
            else:
                break
        nasv = data_string[0:t]
        dan = data_string[t+1:n]
        # print(nasv,dan)
    return isbavl(nasv,dan)




chrome_options=Options()
#chrome_options.add_argument('start-maximized')
#chrome_options.add_argument('--headless')

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://freedome-realty.ru/')
print('Открыта главная страница')
time.sleep(3)
click = driver.find_element_by_xpath("//div[@class='header_filter-item-wrap']/img[1]")
click.click()
chose_1 = driver.find_elements_by_xpath("//div[@class='header_filter_select open']/div[@class='header-filter_select-wrap']/ul[1]/li")
print(len(chose_1))
for ch in chose_1:
    #print(ch.get_attribute('href'))
    print(f"{ch.text} - {ch.get_attribute('data-id')}")
#n = str(input("Введите номер, выбранной группы:"))
n = str(38)
fin = driver.find_element_by_xpath("//div[@class='header_filter-item header_filter-search-btn']/button[1]")
#chose_1 = driver.find_element_by_xpath("//div[@class='header_filter_select open']/div[@class='header-filter_select-wrap']/ul[1]/li[@data-id]={n}")
#print(fin.text)
#fin.click
chose_1 = driver.find_elements_by_xpath("//div[@class='header_filter_select open']/div[@class='header-filter_select-wrap']/ul[1]/li")
for ch in chose_1:
    #print(ch.get_attribute('href'))
    if ch.get_attribute('data-id') == n:
        #driver.get(ch.get_attribute('href'))
        print('https://freedome-realty.ru' + ch.get_attribute('href'))
        driver.get('https://freedome-realty.ru' + ch.get_attribute('href'))
        break
#chose_1.click()
# next = driver.find_element_by_xpath("//div[@class='offers__footer b-show']/div[@class='container']/a[@class='go-to show']")
last_page = driver.find_element_by_xpath("//div[@class='pagination']/div[@class='container']/ul[1]/li[last()]").text
print(last_page)
# next_2 = next.text


informazia = []
page = 1
for page in range(int(last_page)):
    links = driver.find_elements_by_xpath("//div[@class='container']/div[@class='row']/div[@class='col-xs-12 col-md-6 col-lg-4 col-xl-3']/div[1]/a[@class='offer__info']")
    for link in links: #упрощённая версия того, что должно быть
        print("00000000000000")
        href = link.get_attribute('href')
        driver.get(href)
        name = driver.find_element_by_xpath("//div[@class='obj-section_title']").text
        print(name)
        time.sleep(1)
        driver.back()
        time.sleep(1)
    #   то, что должно быть(сбор данных)
    # for link in links:
    #     vacancy_data = {}
        #link = i.find_element_by_xpath("//div[1]/a[@class='offer__info']")
        # print(link.get_attribute('href'))
        # driver.get(link.get_attribute('href'))
        # name = driver.find_element_by_xpath("//div[@class='obj-section_title']").text
        # adress = driver.find_element_by_xpath("//div[@class='obj-section_adress']").text
        # metro = driver.find_element_by_xpath("//div[@class='obj-section_metro']").text
        # lot = driver.find_element_by_xpath("//div[@class='obj-card_heading']/div[@class='obj-card_id']").text
        # lot = p_lot(lot)
        #
        # price = driver.find_element_by_xpath("//div[@class='obj-card_value rent']/span[@class='val']").text
        # #print(price)
        # price = p_price(price)
        # #     вставить много
        #
        # #price_USD = driver.find_element_by_xpath("//div[@class='obj-card_value rent']/span[@class='val usd']").text
        # za_metr = driver.find_element_by_xpath("//div[@class='obj-card_footage-price']").text #почистить (56 250₽ за м2)
        #
        # dann = driver.find_elements_by_xpath("//div[@class='obj-card_info']/div[2]/div[@class='obj-card_props']/div[@class='obj-card_prop']")
        # # dann = driver.find_elements_by_xpath(
        # #     "//div[@class='obj-card_info']/div[2]/div[@class='obj-card_props']/div[@class='obj-card_prop']/div[@class='val']")
        # for dan in dann:
        #     d = dan.text
        #     d = p_dann(d) #функцию, которая будет разделять эл
        #     print(d)
        #back_page = driver.find_element_by_xpath("//ol[@class='breadcrumb']/li[3]/a[1]")
        #driver.get(back_page.get_attribute('href'))
    page += 1
    print (f"https://freedome-realty.ru/baza-nedvizhimosti/kommercheskaya-nedvizhimost/?PAGEN_1={page}")
    driver.get(f"https://freedome-realty.ru/baza-nedvizhimosti/kommercheskaya-nedvizhimost/?PAGEN_1={page}")
    # print('https://freedome-realty.ru' +  next.get_attribute('href'))
    # next = driver.find_element_by_xpath("//div[@class='container']/a[@class='go-to show']").text
    # print(next)