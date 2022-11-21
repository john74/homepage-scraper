import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(f'{os.getcwd()}/chromedriver')
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(service=service, options=options)
