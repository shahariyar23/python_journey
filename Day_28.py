# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "beautifulsoup4",
#     "requests",
# ]
# ///

# Day 28: Web Scraping Basics
# Install requests and BeautifulSoup
import requests
from bs4 import BeautifulSoup
# Making HTTP requests

# url = "https://www.google.com"
# response = requests.get(url)
# print(response.status_code)
# print(response.text[:500])


# Parsing HTML

# soup = BeautifulSoup(response.text, "html.parser")
# print(soup.title.text)
# print(soup.find('h1').text)

# Practice: Scrape news headlines, extract data from a simple website

# url = "https://www.bbc.com/news"
# response = requests.get(url)

# soup = BeautifulSoup(response.text, "html.parser")

# headlines = soup.find_all('h2')
# print("BBC news headline: \n")
# for idx, h in enumerate(headlines[:10], 1):
#     print(f"{idx}:   {h.text.strip()}")


url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

author = soup.find_all("small", class_="author")
quotes = soup.find_all("span", class_="text")
print("Qoutes: \n")
for i in range(len(quotes)):
    print(f"{i + 1}. {quotes[i].text.strip()} -> author: {author[i].text.strip()}")
    
import csv

with open("quotes.csv", "w", newline="", encoding="utf-8") as f:
    write = csv.writer(f)
    write.writerow(["Quote", "Author"])
    for i in range(len(quotes)):
        write.writerow([quotes[i].text, author[i].text])
print("Data is save")