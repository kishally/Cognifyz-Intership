#Task 1: Build a Web Scraper
'''Develop a web scraper that extracts specific data from websites using libraries like BeautifulSoup or Scrapy. 
This task will improve their knowledge of web scraping techniques and handling HTML/XML data'''

import requests
from bs4 import BeautifulSoup

def scrape_user_input():
    url = input("Enter the website URL (with https://): ").strip()
    tag = input("Enter the HTML tag to extract (e.g., h1, p, a): ").strip()

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for HTTP errors

        soup = BeautifulSoup(response.text, 'html.parser')
        elements = soup.find_all(tag)

        if not elements:
            print(f"No <{tag}> elements found on the page.")
        else:
            print(f"\nFound {len(elements)} <{tag}> tags:\n")
            for idx, element in enumerate(elements, 1):
                text = element.get_text(strip=True)
                if text:
                    print(f"{idx}. {text}")
    except requests.exceptions.RequestException as e:
        print(f"Network/HTTP Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")

scrape_user_input()
