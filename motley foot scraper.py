#import appropriate libraries for web scraping and data science
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup as soup
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

for i in range(5):
	url = 'https://www.fool.ca/recent-headlines/' + '/page/' + str(i) + '/'
	
	req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})
	webpage = urlopen(req).read()
	page_soup = soup(webpage, "html.parser")
	containers = page_soup.findAll("p","promo")

	for container in containers:
		print(container)
		f= open("headlines.txt","a+")
		f.write(str(container.getText())) 

text = open('headlines.txt').read()

# Generate a word cloud image
wordcloud = WordCloud().generate(text)

# Display the generated image:
# the matplotlib way:

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

# lower max_font_size
wordcloud = WordCloud(max_font_size=40).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
		