from bs4 import BeautifulSoup

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome(
    executable_path="/usr/local/bin/chromedriver", options=options)


url = "https://www.aftonbladet.se/tagg/politik/"
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
headlines = soup.find('body').find_all("h2")

for x in headlines:
    print(x.text.strip())


