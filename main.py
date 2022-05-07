# Module for HTTP requests
import requests

# WebScraping Package
from bs4 import BeautifulSoup

# Scraping google searches Package
from googlesearch import search

# Search for a question
query = "Which of the following is the last step in the exchange between a web browser and a database?"

for j in search(query, tld="co.in", num=10, stop=10, pause=2):
    print(j)
