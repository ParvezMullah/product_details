from product_scraper.utils.utils import get_site
from product_scraper.utils.base_scraper import BaseProductScraper

from product_scraper.utils.ur_parts import UrPartsScraper


def scraper_factory(website_url: str) -> BaseProductScraper:
    website_name = get_site(website_url)
    if website_name == "https://www.urparts.com/":
        return UrPartsScraper(website_url)
    raise Exception(f"We Cant Scrape From {website_name}")
