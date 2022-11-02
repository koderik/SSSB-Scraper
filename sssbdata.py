import time
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import json


def sssbdata():
    url = "https://sssb.se/soka-bostad/sok-ledigt/lediga-bostader/?pagination=0&paginationantal=1000"
    options = webdriver.ChromeOptions()
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--incognito")
    options.add_argument("--headless")
    driver = webdriver.Chrome("/usr/local/bin/chromedriver", options=options)

    driver.get(url)
    time.sleep(3)  # experiment with timer to fetch all the data
    page = driver.page_source

    soup = BeautifulSoup(page, "html.parser")

    data = soup.find("div", {"data-logic": "sok.listor.js"})
    appartment_urls = data.find_all("h3", {"class": "ObjektTyp"})

    appartments = data.find_all("div", {"class": "media"})
    appartments_dataframe = pd.DataFrame(
        columns=["address", "size", "rent", "personer", "dagar","time", "url"]
    )
    for appartment in appartments:

        # find address in appartment
        addressdata = appartment.find("h4")

        url = addressdata.find("a").get("href")
        address = addressdata.find("a").text
        appartmentdata = appartment.find("div", {"class": "ObjektDetaljer span6"})
        price = appartmentdata.find("dd", {"class": "ObjektHyra"}).text
        # format price as integer

        price = price.replace("kr", "").strip(" ")

        size = appartmentdata.find("dd", {"class": "ObjektYta"}).text
        # format size string to integer
        size = size.replace("m²", "")
        intresse = appartmentdata.find(
            "dd", {"class": "ObjektAntalIntresse hidden-phone"}
        ).text
        # split intresse in to intresse and antalintresserade
        dagar, personer = intresse.split(" ")
        # remove paranthesis and "st" from personer
        antalintresserade = personer.replace("(", "").replace("st)", "")
        # get today date with hours and minutes
        tid = time.strftime("%Y-%m-%d %H:%M")
       

        adf = pd.DataFrame.from_records(
            [
                {
                    "address": address,
                    "size": size,
                    "rent": price,
                   "personer": antalintresserade,
                    "dagar": dagar,
                    "time": tid,   
                    "url": url,
                }
            ]
        )
        # add queuedf datafram as column to adf

        # concatenate the dataframes
        appartments_dataframe = pd.concat([appartments_dataframe, adf])

    return appartments_dataframe

    driver.quit()

    return appartment_dict


