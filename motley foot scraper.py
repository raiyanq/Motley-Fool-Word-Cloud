#import appropriate libraries for web scraping and data science
from urllib.request import Request, urlopen
import numpy as np
from bs4 import BeautifulSoup as soup
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

#Go through the first 10 pages of Motely Fool
for i in range(10):
	#Send a request to the url
	url = 'https://www.fool.ca/recent-headlines/' + '/page/' + str(i) + '/'
	
	req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})
	#Get the web page
	webpage = urlopen(req).read()
	page_soup = soup(webpage, "html.parser")
	containers = page_soup.findAll("p","promo")
	#Go through all the headlines 
	for container in containers:
		#Split the Headline
		list_words= str(container).split()
		for word in list_words:
			#Fidn the stock ticker symbols
			if (word.startswith("(TSX:") or word.startswith("(NYSE:")):
				word.replace(",","")
				word.replace(".","")
				print(word)
				f= open("headlines.txt","a+")
				f.write(str(word))	

				text = open('headlines.txt').read()

# Generate a word cloud image
wordcloud = WordCloud().generate(text)

# Display the generated image:
# the matplotlib way:
image = wordcloud.to_file("wordcloud.png")


# lower max_font_size
wordcloud = WordCloud(max_font_size=40).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()