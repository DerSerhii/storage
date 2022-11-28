""" Using Selenium Webdriver and BeautifulSoup """

import datetime

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from colorama import Fore

# settings driver
driver = ChromeService(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
# options.add_argument('headless')

# settings browser
URL = 'https://slovnyk.ua/index.php'


def get_soup_ukr_word(word: str) -> BeautifulSoup:
    t0 = datetime.datetime.now()

    session = webdriver.Chrome(service=driver, options=options)
    session.get(URL)
    session.implicitly_wait(0.5)

    input_word = session.find_element(by=By.XPATH, value='//*[@id="swrd"]')
    input_word.send_keys(word, Keys.ENTER)

    soup = BeautifulSoup(session.page_source, 'lxml')
    session.quit()

    dt = datetime.datetime.now() - t0
    print(Fore.RED + f"Done in {dt.total_seconds():.2f} sec.")

    return soup.find('div', class_='table-wrap')


result = get_soup_ukr_word("спати")
print(Fore.LIGHTGREEN_EX, result.text)
