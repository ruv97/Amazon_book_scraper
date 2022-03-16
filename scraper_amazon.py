from urllib import response
import requests
from flask import request
from constants import(
    today_date
)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd
import time

s = Service("/home/ruwini/chromedriver_linux64/chromedriver")
driver = webdriver.Chrome(service=s)

driver.get('https://www.amazon.in/')

details_list = []

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
from csv import DictReader

with open('test_1.csv','r') as read_obj:
    csv_dict_reader = DictReader(read_obj)
    for row in csv_dict_reader:

        driver.find_element(By.ID,'twotabsearchtextbox').send_keys(row['title'])
        driver.find_element(By.ID,'nav-search-submit-button').click()
        time.sleep(0.5)
        driver.find_element(By.XPATH,'//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[3]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span').click()
        time.sleep(0.5)
                
        url = driver.current_url

        response = requests.get(url, headers=headers)
        page_contents = response.text

        doc = BeautifulSoup(page_contents, 'html.parser')

        title = doc.select("#tmmSwatches")

        print(title)

        driver.find_element(By.ID,'twotabsearchtextbox').clear()
        
        # response = requests.get(url, headers=headers)
        # page_contents = response.text

        # doc = BeautifulSoup(page_contents, 'html.parser')

        # title = doc.find(id='price')
       
        # print(title)
        