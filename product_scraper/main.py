import typer
from product_scraper.utils.scraper_factory import scraper_factory


def scrape_products(website_url: str) -> None:
    scraper_obj = scraper_factory(website_url)
    scraper_obj.scraper_site()


if __name__ == "__main__":
    typer.run(scrape_products)
