from constants import(
    today_date
)
import csv
from time import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from csv import DictReader
from selenium.webdriver.common.by import By
import pandas as pd
import time
class crawledArticle():
    def __init__(self,price):
        self.price=price
class b:
    def article(self):
        a = []
        options = Options()
        options.headless = False
        options.add_experimental_option("detach", True)
        browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        browser.maximize_window()
        url = "https://www.amazon.in"
        browser.get(url)

        with open('books_goodreads.csv','r') as read_obj:
            csv_dict_reader = DictReader(read_obj)
            for row in csv_dict_reader:
                browser.find_element(By.ID,'twotabsearchtextbox').send_keys(row['title'])
                time.sleep(2)
                browser.find_element(By.ID,'nav-search-submit-button').click()

                
                browser.implicitly_wait(5)
                
                details = {}
                
                url=browser.find_element_by_xpath('.//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]').get_attribute('href')
                
                browser.get(url)
                
                details['title'] = row['title']
                
                try:
                    p=browser.find_element_by_xpath('.//span[@id="price"]').text
                    details['paperbook_price'] = float(p[1:])
                except NoSuchElementException:
                    details['paperbook_price'] = float(0)

                try:
                    audible_price=browser.find_element(By.XPATH,'.//span[@class="audible_mm_price"]').text
                    details['audible_price'] = float(audible_price[1:])
                except NoSuchElementException:
                    audible_price = float(0)
                    details['audible_price'] = audible_price
                    

                
                try:
                    kindle_price = browser.find_element(By.XPATH,'//*[@id="a-autoid-5-announce"]/span[2]/span').text
                    details['kindle_price'] = float(kindle_price[1:])
                except NoSuchElementException:
                    kindle_price = float(0)
                    details['kindle_price'] = kindle_price
                    

                    
                try:
                    hardcover_price = browser.find_element(By.XPATH,'//*[@id="a-autoid-6-announce"]/span[2]/span').text
                    details['hardcover_price'] = float(hardcover_price[1:])
                except NoSuchElementException:
                    hardcover_price = float(0)
                    details['hardcover_price'] = hardcover_price
                    
                try:
                    category = browser.find_element(By.XPATH,'//*[@id="wayfinding-breadcrumbs_feature_div"]/ul').text
                    details['category'] = category
                except NoSuchElementException:
                    category = 'N/A'
                    details['category'] = category
                    
                try:
                    description = browser.find_element(By.XPATH, '//*[@id="bookDescription_feature_div"]/div/div[1]/span/p').text
                    details['description'] = description
                except NoSuchElementException:
                    description = 'N/A'
                    details['description'] = description
                    
                a.append(details)
                
                try:
                    rating=browser.find_element(By.XPATH, './/span[@id="acrCustomerReviewText"]').text
                    details['number_of_ratings'] = rating
                except NoSuchElementException:
                    details['number_of_ratings'] = "N/A"
                
                try:
                    avg_rating = browser.find_element(By.XPATH, '//*[@id="acrPopover"]').text
                    details['avg_rating'] = avg_rating
                except NoSuchElementException:
                    avg_rating = 'N/A'
                    details['avg_rating'] = avg_rating
                    
                try:
                    delivery_info = browser.find_element(By.XPATH, '//*[@id="mir-layout-DELIVERY_BLOCK-slot-DELIVERY_MESSAGE"]').text
                    details['delivery_info'] = delivery_info
                except NoSuchElementException:
                    delivery_info = 'N/A'
                    details['delivery_info'] = delivery_info
                    
                try:
                    merchant_info = browser.find_element(By.XPATH, '//*[@id="merchant-info"]/a[1]').text
                    details['merchant_info'] = merchant_info
                except NoSuchElementException:
                    merchant_info = 'N/A'
                    details['merchant_info'] = merchant_info
                
                browser.find_element(By.ID,'twotabsearchtextbox').clear()
           
            a = pd.DataFrame(a)
            a.to_csv('books_amazon.csv')
            b = pd.read_csv("books_goodreads.csv")
            
            c = pd.merge(a, b, on='title')
            c.set_index('title', inplace=True)
            c.to_csv('books_amazon_goodreads_{}.csv'.format(today_date)
                
fetcher = b()
