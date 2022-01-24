from product_scraper.utils.base_scraper import BaseProductScraper


class UrPartsScraper(BaseProductScraper):
    def __init__(self, website_url):
        self.website_url = website_url

    def scraper_site(self):
        print(f"Scraping : {self.website_url}")
