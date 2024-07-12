import requests
from bs4 import BeautifulSoup


def scrape_amazon_for_me(url):
    """This function will scrap the amazon.in."""
    # Send a request to the URL
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Example: Scraping product title
    title_element = soup.find('span', {'id': 'productTitle'})
    title = title_element.get_text().strip() if title_element else 'No title found'

    # Example: Scraping product price
    price_element = soup.find('span', {'id': 'priceblock_ourprice'})
    price = price_element.get_text().strip() if price_element else 'No price found'

    # Print scraped data
    print(f"Title: {title}")
    print(f"Price: {price}")


if __name__ == "__main__":
    # Example URL of a product on Amazon.in
    product_url = 'https://www.amazon.in/s?k=men+watches&crid=DGFYQAKEVXDT&sprefix=men+watches%2Caps%2C202&ref=nb_sb_noss_1'
    scrape_amazon_for_me(product_url)