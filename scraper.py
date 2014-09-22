#!/usr/bin/env python
# vim: set fileencoding=utf8 :
import re
import requests
from BeautifulSoup import BeautifulSoup, UnicodeDammit, SoupStrainer

"""Scrapes useful data."""

width = 32
height = 64
user_agent = {"User-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36"}

def scrape(url):
    response = requests.get(url, headers=user_agent)
    root = BeautifulSoup(response.text)

    for node in root.findAll(attrs={'class': re.compile(r".*\bthing\b.*")}):
        print(node)


def main():
    scrape("www.example.com")

if __name__ == '__main__': main()
