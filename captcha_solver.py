import requests
from bs4 import BeautifulSoup as bs
import csv
import os
import json
from time import sleep
import nodriver as uc
from nodriver import Config

# pip install requests bs4 nodriver
# full documentation available at https://ultrafunkamsterdam.github.io/nodriver/

# place the link that you want to open here (cloudflare protected website)
target_link = "https://..."
s = requests.Session()


async def getPageData():
    global s
    config = Config()
    # add extension if needed, comment below line if you don't want to use captcha solver
    config.add_extension(os.path.join(os.getcwd(), "plugin/2captcha"))
    driver = await uc.start(config=config)
    page = await driver.get(target_link)
    sleep(1)
    # waiting for the page element to be detected to determine that the page finished loading
    while True:
        try:
            success_text = await page.find(text='Any text here to match')
            if not success_text:
                print("Waiting for page to finish loading ...")
                sleep(2)
            else:
                break
        except:
            sleep(1)
    sleep(1)
    try:
        page_html = await page.get_content()
    except:
        print("Failed waiting for the page response, moving to the next")
        return
    soup = bs(page_html, 'html.parser')
    # now you can use beautifulsoup to extract the data you need

    # if you want to continue with requests library with the cookie session of the browser:
    cookies = await driver.cookies.get_all(requests_cookie_format=True)
    for cookie in cookies:
        s.cookies.set_cookie(cookie)
    # now you can use s variable to access pages with browser session
    s.get("", headers={"User-Agent": driver.user_agent})
    driver.stop()


if __name__ == "__main__":
    uc.loop().run_until_complete(getPageData())
