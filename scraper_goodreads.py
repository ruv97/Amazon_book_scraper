from constants import (
    today_date,
    password,
    email_address
)
from io import BytesIO
from re import S
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome(executable_path="/home/ruwini/chromedriver_linux64/chromedriver")

driver.get("https://www.goodreads.com/")
 

#click on signin button
driver.find_element_by_xpath('//*[@id="signIn"]/div/div/a').click()

#enter email address and password
driver.find_element_by_xpath('//*[@id="user_email"]').send_keys(email_address)
driver.find_element_by_xpath('//*[@id="user_password"]').send_keys(password)

#click on signin button again 
driver.find_element_by_xpath('//*[@id="emailForm"]/form/fieldset/div[5]/input').click()

#click on MyBooks
driver.find_element_by_xpath('/html/body/div[2]/div/header/div[2]/div/nav/ul/li[2]/a').click()

#---------------------Extract data about books------------------------------------
# Name of the book
# Author
# Average of rating 
# Link for the book

html = driver.page_source
# print(html)

doc = BeautifulSoup(html, 'html.parser')

table = doc.find_all('table', {'id':'books'})[0]
table_rows = table.find_all('tr')
book_list = []

for tr in table_rows[1:]:
    book_dict = {}

    td = tr.find_all('td',{'class':'field title'})[0]
    a_link = td.find('a')
    book_dict['title'] = a_link.get('title')
    

    td = tr.find_all('td', {'class':'field author'})[0]
    a_link = td.find_all('a')[0]
    book_dict['author_name'] = a_link.text

    d = tr.find_all('td', {'class':'field avg_rating'})[0]
    rating_text = d.text
    book_dict['rating'] = rating_text

    book_list.append(book_dict)



books_df = pd.DataFrame(book_list)

books_df.to_csv('books_goodreads.csv',index=None)

