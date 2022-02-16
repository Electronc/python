import requests
import asyncio
from bs4 import BeautifulSoup
from requests_html import AsyncHTMLSession
from pyppeteer import launch
import os


async def main():
    with open('liniki.txt', 'r', encoding='utf8') as fp:
        urls = fp.readlines()
        for URL in urls:
            browser = await launch()
            page = await browser.newPage()
            await page.goto(URL)
            page_content = await page.content()
            ok = BeautifulSoup(page_content,features = "lxml")
            data = ok.find_all("span",class_="core_priceFormat core_cardPriceSpecial")
            for link in data:
                if link['data-price-type'] == "brutto|show_type":
                    cenabrutto = link['data-price']
                    cenanetto = (float(cenabrutto) * 100) / 123
            print(round(cenanetto,2))
            print(cenabrutto)

asyncio.get_event_loop().run_until_complete(main())