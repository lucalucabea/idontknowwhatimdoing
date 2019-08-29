from bs4 import BeautifulSoup
import requests
page_link ='https://thesilphroad.com/raid-bosses'
# fetch the content from url
page_response = requests.get(page_link, timeout=5)
# parse html
page_content = BeautifulSoup(page_response.content, "html.parser")

# extract all html elements where raid boss is stored
bossnames = page_content.find_all(class_='boss-name')

# you can also access the main_price class by specifying the tag of the class
# prices = page_content.find_all('div', attrs={'class':'main_price'})
