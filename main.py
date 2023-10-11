########################################################
# Gjord av Anton Lövgren
# v0.2 - Hämtar RSS-flöden från olika svenska hemsidor
# Nytt i v0.2:
# Förenklat koden
########################################################
# Att göra:
# * Välja ämne (tex sport, nyheter, ekonomi)
# * Länkar till hemsidor
# * Snygga till utseendet
########################################################

# pip install beautifulsoup4 lxml requests

from bs4 import BeautifulSoup
import requests

# Hämtar URL
url = requests.get("https://rss.aftonbladet.se/rss2/small/pages/sections/senastenytt/")

# Använder BeautifulSoup, låter den veta att det är xml
soup = BeautifulSoup(url.content, 'xml')
items = soup.find_all("item")

# Hämtar varje item (aftonbladets rss är inbyggda i
for item in items:
    title = item.title.text
    description = item.description.text
    link = item.link.text
    print(f"Title: {title}\n\nDescription: {description}\n\nLink: {link}\n\n---------------------------\n\n")