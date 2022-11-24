import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(f'{os.getcwd()}/chromedriver')
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('disable-infobars')
options.page_load_strategy = 'eager'
options.add_experimental_option(
    # disable image loading
    "prefs", {"profile.managed_default_content_settings.images": 2}
)
driver = webdriver.Chrome(service=service, options=options)
