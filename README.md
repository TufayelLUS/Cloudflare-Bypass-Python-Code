# Cloudflare Bypass Python Code
This template repository contains Python code that implements nodriver library to load websites and solve(manually/automated) captcha that fail with selenium/undetected chromedriver<br>
Nodriver library is an official successor of undetected chromedriver library that gets rid of relying on webdriver files completely. This is also capable of convincing websites as a regular browser so that the bot detection ratio is minimal. In many websites, undetected chromedriver fails to pass Cloudflare browser verification. In those cases, nodriver does wonders and can load such websites easily. As an automation software developer, I used this library in my client projects that have Cloudflare protection and it helps in my process.

# Installation command
<pre>pip install nodriver</pre>

# Concept
You can use nodriver to load a website and get its source code. An example code can be like below
<pre>
import nodriver as uc
from bs4 import BeautifulSoup as bs
driver = await uc.start()
page = await driver.get("https://google.com")
text = await page.get_content()
soup = bs(text, 'html.parser')
print(soup.find("body").text)
driver.stop()
</pre>


# Documentation Page Link for nodriver Library
<a href="https://ultrafunkamsterdam.github.io/nodriver/">Click here</a>

# How to set 2captcha api key?
Put this in
<code>https://github.com/TufayelLUS/Cloudflare-Bypass-Python-Code/blob/main/plugin/2captcha/common/config.js</code> file's <b>apiKey</b> placeholder. The rest of the extension operation is automated.
If you want to enable/disable other 2captcha auto-detection, you can do so in the same config file.
