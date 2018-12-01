#import appropriate libraries for web scraping and data science
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup as soup
import pandas as pd
import matplotlib.pyplot as plt

for i in range(5):

#Open a connection to retreive the page and close connection after
	url = 'https://www.fool.ca/recent-headlines/' + '/page/' + str(i) + '/'
	print(url)
	req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})
	webpage = urlopen(req).read()
	
	page_soup = soup(webpage, "html.parser")
	containers = page_soup.findAll("p","promo")

	for container in containers:
		print(container)


#Scrape the HTML of the Harry Rosen New Products Page for information on brand, product name and price
#page_soup = soup(page_html, "html.parser")
#containers = soup.find_all("p", "promo")

