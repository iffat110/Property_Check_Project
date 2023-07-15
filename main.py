import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

header = {
    "User-Agent" : "YOUR USER-AGENT",
    "Accept" : "YOUR ACCEPT LANGUAGE"
}

response = requests.get("https://www.zillow.com/new-york-ny/rentals/?"
           "searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%"
           "22north%22%3A41.002734484292795%2C%22east%22%3A-73.4399776308594%2C%22south%22%3A40.39156689207836%"
           "2C%22west%22%3A-74.51938436914065%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%"
           "3A%7B%22max%22%3A394828%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%"
           "2C%22mp%22%3A%7B%22max%22%3A2000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%"
           "3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%"
           "7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%"
           "22regionSelection%22%3A%5B%7B%22regionId%22%3A6181%2C%22regionType%22%3A6%7D%5D%7D", headers=header)

data = response.text
soup = BeautifulSoup(data, "html.parser")

all_links_element = soup.find_all(name="a",class_="StyledPropertyCardDataArea-c11n-8-89-0__sc-yipmu-0 gZUDVm property-card-link")
links = []
for all_link in all_links_element:
    href = all_link["href"]
    print(links)
    if "https" not in href:
        links.append(f"https://www.zillow.com{href}")
    else:
        links.append(href)

all_address_element = soup.find_all(name="address")
addresses = []
for address in all_address_element:
    area = address.getText()
    addresses.append(area)

rent = []
all_rent = soup.find_all(name="span", class_ ="PropertyCardWrapper__StyledPriceLine-srp__sc-16e8gqd-1 iMKTKr")
for renting in all_rent:
    amount = renting.getText()
    rent.append(amount)


service = Service(executable_path='YOUR PATH')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

for n in range(len(links)):
    driver.get("GOOGLE FORM LINK")
    time.sleep(5)

    address = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    price = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    link = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    submit_button = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div/span/span")

    address.send_keys(addresses[n])
    price.send_keys(rent[n])
    link.send_keys(links[n])
    submit_button.click()













