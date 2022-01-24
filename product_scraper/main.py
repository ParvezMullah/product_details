import typer
import time
from product_scraper.utils.scraper_factory import scraper_factory


def scrape_products(website_url: str) -> None:
    begin = time.time()
    scraper_obj = scraper_factory(website_url)
    scraper_obj.scraper_site()
    end = time.time()
    print(f"Total runtime of the program is {end - begin}")


if __name__ == "__main__":
    typer.run(scrape_products)
