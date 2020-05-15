'''
file name: HW2.py
autor: medulka
created: 2020-05-14
updated: 2020-05-15

Requirement:
Use your preferred test automation tool to automate test case: 
Go to your favorite e-shop, navigate to some category and add two most expensive items 
to the shopping cart from this category. 
Provide code from implementation.

'''

# I am in the virtual environment AT

from selenium import webdriver
#from selenium.webdriver.chrome.options import Options  
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from time import sleep
#import pandas as pd

driver = webdriver.Chrome()
driver.get("https://www.benu.cz/merck/")
select = Select(driver.find_element_by_name("select-sort"))
select.select_by_value('sort-price-desc')

#print('Sleeping...')
sleep(5)
#print('Sleep done')

for i in range(10):
    driver.find_element_by_css_selector('body').send_keys(Keys.ARROW_DOWN)

products = driver.find_elements_by_css_selector('div.products-list > ul.products > li')
products = products[:2]

top_products = []

for p in products:
    p_name = p.find_element_by_css_selector('span.name').text
    p_price = p.find_element_by_css_selector('p.price > strong').text
    #print(f'product: {p_name!r} {p_price!r}')
    top_products.append((p_name, p_price))
    p_buy = p.find_element_by_css_selector('p.buy > button')
    #print(f'Clicking on {p_buy!r} {p_buy.text!r}')
    p_buy.click()
    sleep(1)
    driver.find_element_by_css_selector('body').send_keys(Keys.ARROW_DOWN)
    driver.find_element_by_css_selector("a.pdbox__close").click()

driver.get("https://www.benu.cz/kosik/")

#driver.quit() # close the browser
