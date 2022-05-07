# Module for HTTP requests
import requests

# WebScraping Package
from bs4 import BeautifulSoup

# Scraping google searches Package
from googlesearch import search

# Search for a question
query = "Which of the following is the last step in the exchange between a web browser and a database?"


headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}

# For Loop to provide 10 google Query's
for j in search(query, tld="co.in", num=10, stop=1, pause=2):
    soup = BeautifulSoup(requests.get(j, headers=headers).content, 'html.parser')
    for i, (question, answer) in enumerate(
            zip(soup.select('a.SetPageTerm-wordText'), soup.select('a.SetPageTerm-definitionText')), 1):

        # Look for the Question then respond with the Answer
        if query in question.get_text(strip=True, separator='\n'):
            print(answer.get_text(strip=True, separator='\n'))
            break

